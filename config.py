from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

REQUIRED_VARS = ["OPENAI_API_KEY", "EMAIL_FROM", "EMAIL_TO", "EMAIL_APP_PASSWORD", "MONGODB_URI", "MONGODB_DB"]
missing = [v for v in REQUIRED_VARS if not os.getenv(v)]

if missing:
    raise RuntimeError(f"Missing env vars: {', '.join(missing)}")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")

client = OpenAI(api_key=OPENAI_API_KEY)
