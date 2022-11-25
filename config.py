from os import getenv, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")


APP_ID = int(getenv("APP_ID"))
API_HASH = getenv("API_HASH")
STRING_SESSION = getenv("SESSION_NAME")
DELAY = int(getenv("DELAY", 5))
if CHATS := getenv("CHATS", None):
    CHATS = CHATS.split(" ")
