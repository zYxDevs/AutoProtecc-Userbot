from os import getenv, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")


APP_ID = int(getenv("APP_ID"))
API_HASH = getenv("API_HASH")
STRING_SESSION= getenv("SESSION_NAME")
if CHATS := getenv("CHATS", None):
    CHATS = CHATS.split(" ")
if BOT_LIST := getenv("BOT_LIST", None):
    BOT_LIST = BOT_LIST.split(" ")
