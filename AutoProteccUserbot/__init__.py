import os
import time
from pyrogram import Client, errors

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION", None)
DELAY = os.environ.get("DELAY", None)

Waifu = Client(SESSION, api_id=API_ID, api_hash=API_HASH)
