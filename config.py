# config.py
import os
import sys
from dotenv import load_dotenv

# 1. Загружаем .env один раз
load_dotenv()

# 2. Читаем переменные
TOKEN = os.getenv("TOKEN")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

# 3. ВАЛИДАЦИЯ (BigTech Level)

if not TOKEN:
    print("❌ ОШИБКА: Не найден TOKEN в файле .env")
    sys.exit(1)

if not PERPLEXITY_API_KEY:
    print("❌ ОШИБКА: Не найден PERPLEXITY_API_KEY в файле .env")
    sys.exit(1)

# Опционально: другие настройки
# DB_URL = os.getenv("DB_URL", "sqlite:///database.db")