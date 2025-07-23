from config import INACTIVITY_SECONDS
import time
from database import sessions_col
from gpt_utils import classify_conversation
from utils import format_conversation
from emailer import send_email

def process_sessions():
    now = time.time()

    inactive_sessions = sessions_col.find({
        "last_seen": {"$lte": now - INACTIVITY_SECONDS},
        "history.0": {"$exists": True}
    })

    for session in inactive_sessions:
        phone = session["_id"]
        history = session["history"]

        try:
            summary = classify_conversation(history)
            body = format_conversation(history)
            send_email(f"{phone} - {summary}", body)
            sessions_col.delete_one({"_id": phone})
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    process_sessions()
