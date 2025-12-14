# 🎙️ AI Voice Assistant Bot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-blue)
![Architecture](https://img.shields.io/badge/Architecture-Client%2FServer-orange)
![Status](https://img.shields.io/badge/Status-Development-green)

**An intelligent voice interface capable of Speech-to-Text recognition, NLP intent analysis, and vocal response generation.**

This project implements a modular **Speech-to-Speech** pipeline. It is designed to bridge the gap between text-based LLMs and natural voice interaction, operating via a telegram interface with a dedicated backend server.

---

## 🧠 Core Architecture

The system processes user interactions in 4 distinct stages:

1.  **👂 Speech Recognition (STT):**
    * Captures audio input (Ogg/WAV) from the Telegram client.
    * Converts speech to text using external APIs or local models.

2.  **🧠 Natural Language Processing (NLP):**
    * Analyzes the transcribed text to identify user **Intents**.
    * Powered by LLMs (e.g., Perplexity AI / OpenAI) to generate context-aware answers.

3.  **🗣️ Text-to-Speech (TTS):**
    * Synthesizes the text response back into human-like audio.

4.  **📡 Client-Server Communication:**
    * **Client (`client/`):** Handles Telegram API updates, audio file management, and user feedback.
    * **Server (`server/`):** Processes heavy logic, manages database models (Django/FastAPI), and handles API integrations.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Bot Framework:** Aiogram (AsyncIO)
* **Backend:** Django / FastAPI (Modular structure)
* **AI Integration:** Perplexity API (LLM), SpeechKit (STT/TTS)
* **Environment Management:** `python-dotenv` for secure credential handling

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/voice_assistant_bot.git](https://github.com/YOUR_USERNAME/voice_assistant_bot.git)
cd voice_assistant_bot

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

TOKEN=your_telegram_bot_token
PERPLEXITY_API_KEY=pplx-your_api_key
# Add other keys if necessary (e.g., DJANGO_SECRET_KEY)

# Navigate to the client folder (or root depending on your entry point)
python client/main.py

voice_assistant_bot/
├── client/              # Telegram Bot Client logic
│   ├── main.py          # Entry point for the bot
│   └── temp/            # Temporary audio storage
├── server/              # Core backend logic
│   ├── bot/             # App specific logic (Django apps)
│   └── audio_responses/ # Generated audio cache
├── assets/              # Images for README
├── config.py            # Centralized configuration loader
├── .env                 # Secrets (Excluded from Git)
└── requirements.txt     # Project dependencies
