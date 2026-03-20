import re
import pandas as pd


HEADER_PATTERN = re.compile(
    r'^\s*\[?\u200e?(?P<date>\d{1,2}[./-]\d{1,2}[./-]\d{2,4})[, ]+\s*'
    r'(?P<time>\d{1,2}:\d{2}(?::\d{2})?\s*(?:[APap]\.?(?:[Mm])\.?)?)\]?\s*[-\u2013]\s*(?P<content>.*)$'
)


def _normalize_time(value):
    value = str(value).strip().upper().replace('.', '')
    value = re.sub(r'\s+', ' ', value)
    return value


def _parse_message_date(date_part, time_part):
    date_part = str(date_part).strip().replace('.', '/').replace('-', '/')
    time_part = _normalize_time(time_part)
    value = f"{date_part}, {time_part}"

    formats = [
        '%d/%m/%Y, %H:%M',
        '%d/%m/%y, %H:%M',
        '%m/%d/%Y, %H:%M',
        '%m/%d/%y, %H:%M',
        '%d/%m/%Y, %I:%M %p',
        '%d/%m/%y, %I:%M %p',
        '%m/%d/%Y, %I:%M %p',
        '%m/%d/%y, %I:%M %p',
        '%d/%m/%Y, %I:%M:%S %p',
        '%d/%m/%y, %I:%M:%S %p',
        '%m/%d/%Y, %I:%M:%S %p',
        '%m/%d/%y, %I:%M:%S %p',
    ]

    for fmt in formats:
        try:
            return pd.to_datetime(value, format=fmt)
        except (ValueError, TypeError):
            continue

    fallback = pd.to_datetime(value, errors='coerce', dayfirst=True)
    if pd.notna(fallback):
        return fallback

    return pd.to_datetime(value, errors='coerce', dayfirst=False)


def _split_user_message(text):
    cleaned = str(text).strip()
    entry = re.match(r'^([^:]+?):\s([\s\S]*)', cleaned)
    if entry:
        return entry.group(1), entry.group(2)
    return 'group_notification', cleaned

def preprocess(data):
    normalized = str(data).replace('\ufeff', '').replace('\u200e', '').replace('\r\n', '\n')
    lines = normalized.split('\n')

    rows = []
    current_date = None
    current_content = []

    for line in lines:
        match = HEADER_PATTERN.match(line)
        if match:
            if current_date is not None:
                rows.append((current_date, '\n'.join(current_content).strip()))

            dt = _parse_message_date(match.group('date'), match.group('time'))
            if pd.isna(dt):
                current_date = None
                current_content = []
                continue

            current_date = dt
            current_content = [match.group('content').strip()]
        else:
            if current_date is not None:
                current_content.append(line)

    if current_date is not None:
        rows.append((current_date, '\n'.join(current_content).strip()))

    if not rows:
        return pd.DataFrame(columns=['date', 'user', 'message', 'only_date', 'year', 'month_num', 'month', 'day', 'day_name', 'hour', 'minute', 'period'])

    df = pd.DataFrame(rows, columns=['date', 'user_message'])
    users, messages = zip(*df['user_message'].apply(_split_user_message))
    df['user'] = list(users)
    df['message'] = list(messages)
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df