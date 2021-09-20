import os
import time
from pyrogram import Client, errors

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)
DELAY = os.environ.get("DELAY", None)
BOT_LIST = {int(x) for x in os.environ.get("BOT_LIST", "").split()}

Waifu = Client(STRING_SESSION, session_name=waifu, api_id=API_ID, api_hash=API_HASH)
