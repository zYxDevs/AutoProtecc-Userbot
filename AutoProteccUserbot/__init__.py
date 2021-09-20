import os
import time
from pyrogram.session import Session
from pyrogram import Client, errors

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)
DELAY = os.environ.get("DELAY", None)
BOT_LIST = {int(x) for x in os.environ.get("BOT_LIST", "").split()}

if STRING_SESSION:
    Waifu = Client(Session(STRING_SESSION), api_id=API_ID, api_hash=API_HASH)
else:
    Waifu = Client("userbot", api_id=API_ID, api_hash=API_HASH)
