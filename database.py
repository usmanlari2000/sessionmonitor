from pymongo import MongoClient
from config import MONGODB_URI, MONGODB_DB

mongo = MongoClient(MONGODB_URI)
db = mongo[MONGODB_DB]
sessions_col = db["sessions"]
