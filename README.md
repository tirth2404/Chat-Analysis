<div align="center">

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Live-25D366?style=for-the-badge"/>

<br/><br/>

# 📊 WhatsApp Chat Analyzer

### _Turn your chats into insights. Every message tells a story._

<br/>

[![Live Demo](https://img.shields.io/badge/🚀%20Try%20Live%20Demo-25D366?style=for-the-badge&logoColor=white)](https://whatsapp-chatstats.streamlit.app/)

<br/>

</div>

---

## ✨ What is this?

Ever wondered **who texts the most** in your group? Which **day your friends go crazy** with memes? What **emojis define your chat culture**?

**WhatsApp Chat Analyzer** takes your exported `.txt` chat file and transforms it into a beautiful, interactive dashboard — no coding needed, just upload and explore.

> Supports both **personal** and **group** chats · Works with **Hinglish** stopwords · Handles **multiple date formats**

---

## 🎯 Features at a Glance

| Feature | Description |
|---|---|
| 📈 **Message Timelines** | Monthly & daily activity charts |
| 🗺️ **Activity Heatmap** | Busiest days and hours visualized |
| ☁️ **Word Cloud** | Most used words beautifully rendered |
| 😂 **Emoji Analysis** | Top emojis with pie chart breakdown |
| 👥 **Per-User Stats** | Drill down into any individual's activity |
| 🔗 **Link & Media Tracking** | Count of URLs and media messages shared |
| 📅 **Busy Day/Month Maps** | Bar charts for peak activity periods |

---

## 🚀 Try it Live

No setup needed. Just click, upload your chat file, and go:

**👉 [whatsapp-chatstats.streamlit.app](https://whatsapp-chatstats.streamlit.app/)**

---

## 📱 How to Export Your WhatsApp Chat

<table>
<tr>
<td width="50%">

**On Android**
1. Open the chat
2. Tap ⋮ Menu → **More** → **Export chat**
3. Select **Without Media**
4. Save the `.txt` file

</td>
<td width="50%">

**On iPhone**
1. Open the chat
2. Tap the name at the top → **Export Chat**
3. Select **Without Media**
4. Save the `.txt` file

</td>
</tr>
</table>

> 💡 **Tip:** Always choose "Without Media" — it gives cleaner data and a smaller file.

---

## 🖥️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/tirth2404/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer

# 2. Create virtual environment
python -m venv .venv

# 3. Activate it
# Windows:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Launch 🚀
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## 🗂️ Project Structure

```
whatsapp-chat-analyzer/
│
├── app.py               → Streamlit UI & all visualizations
├── preprocessor.py      → Parses raw WhatsApp .txt export into a DataFrame
├── helper.py            → Analytics functions (stats, charts, word cloud)
├── stop_hinglish.txt    → Hinglish stopwords for clean word analysis
├── requirements.txt     → Python dependencies
├── Procfile             → Deployment config
└── setup.sh             → Server setup script
```

---

## 🛠️ Tech Stack

<div>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square"/>
<img src="https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square"/>
<img src="https://img.shields.io/badge/WordCloud-orange?style=flat-square"/>
</div>

---

## 🔧 Troubleshooting

<details>
<summary><b>❌ "Could not parse messages from this file"</b></summary>

- Re-export the chat with **date and time included**
- Make sure you're uploading a `.txt` file, not a zip or other format
</details>

<details>
<summary><b>☁️ Empty word cloud or common words list</b></summary>

- The selected user may have too few text messages
- Most messages might be media notifications (`<Media omitted>`)
</details>

<details>
<summary><b>😶 No emoji chart appearing</b></summary>

- The selected chat or user simply may not contain any emoji messages
</details>

---

## 🔮 Roadmap

- [ ] Sentiment analysis on messages
- [ ] Downloadable PDF/CSV report
- [ ] Language-aware stopword presets
- [ ] Comparative analysis between multiple users
- [ ] Better handling for very large chat files (10k+ messages)

---

## 📄 License

This project is built for **educational and personal use**.

---

<div align="center">

Made with 💚 by [tirth2404](https://github.com/tirth2404)

⭐ **Star this repo if you found it useful!**

</div>