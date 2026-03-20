# WhatsApp Chat Analyzer

A Streamlit web app that analyzes exported WhatsApp chats and turns them into useful insights with charts, word clouds, emoji analysis, timelines, and activity maps.

## Overview

This project helps you understand group or personal chat behavior from a WhatsApp export text file. It parses raw chat logs, cleans and structures the messages, and provides interactive analytics in a browser dashboard.

The app supports:
- 24-hour and 12-hour timestamp formats
- Multiple common date formats from WhatsApp exports
- Multi-line messages
- Group notifications and user messages

## Features

- Overall and per-user analysis
- Top statistics:
	- Total messages
	- Total words
	- Media messages shared
	- Links shared
- Monthly and daily message timelines
- Activity maps:
	- Most active day
	- Most active month
	- Weekly heatmap (day vs time period)
- Most busy users (for group chats)
- Word cloud generation
- Most common words list
- Emoji frequency analysis with pie chart

## Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- WordCloud
- URLExtract
- Emoji

## Project Structure

- app.py: Streamlit UI and visualization logic
- preprocessor.py: WhatsApp text parsing and dataframe preparation
- helper.py: analytics functions and chart data builders
- stop_hinglish.txt: stop words used for word filtering
- requirements.txt: Python dependencies
- Procfile, setup.sh: deployment helpers for PaaS platforms

## How to Run Locally

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Start the Streamlit app

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL shown in terminal (usually http://localhost:8501).

## How to Export WhatsApp Chat Data

1. Open a chat in WhatsApp
2. Tap Menu -> More -> Export chat
3. Choose Without Media
4. Save the exported .txt file
5. Upload that file in the app sidebar

Note: Using "Without Media" gives cleaner message analysis.

## Usage Flow

1. Upload WhatsApp exported text file
2. Select user scope:
	 - Overall
	 - A specific participant
3. Click Show Analysis
4. Explore all charts and tables

## Deployment Notes

This repo includes:
- Procfile
- setup.sh

These are useful for simple cloud deployment targets where Streamlit needs a runtime port from environment variables.

## Troubleshooting

- Error: "Could not parse messages from this file"
	- Re-export chat with date and time included
	- Ensure you upload the .txt export file, not another format

- Empty word cloud or common words
	- The selected user may have too little textual content
	- Messages may mostly be media notifications

- No emoji chart shown
	- The selected chat/user may not contain emoji messages

## Future Improvements

- Add language-aware stopword presets
- Sentiment analysis for messages
- Downloadable analytics report (PDF/CSV)
- Comparative analysis between users
- Better handling for very large chat files

## License

This project is provided for educational and personal use.
