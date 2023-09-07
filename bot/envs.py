import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE = os.getenv("DATABASE")
TOKEN = os.getenv("TELEGRAM_TOKEN")
GPT_TOKEN = os.getenv("GPT_TOKEN")
