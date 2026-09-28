import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://ru.yougile.com/api-v2")
TOKEN = os.getenv("TOKEN")
COMPANY_ID = os.getenv("COMPANY_ID")
UI_URL = os.getenv("UI_URL", "https://ru.yougile.com/team/")
UI_LOGIN = os.getenv("UI_LOGIN")
UI_PASSWORD = os.getenv("UI_PASSWORD")
UI_PROJECT_URL = os.getenv("UI_PROJECT_URL", "")
