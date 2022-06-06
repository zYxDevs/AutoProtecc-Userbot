import time
import os
import urllib
import requests

from bs4 import BeautifulSoup
from asyncio import get_event_loop
from pyrogram import (
    Client,
    filters,
    idle,
)
from pyrogram.handlers import MessageHandler
from config import config


APP_ID = int(os.environ.get("APP_ID")) or int(config.APP_ID)
API_HASH = str(os.environ.get("API_HASH")) or str(config.API_HASH)
STRING_SESSION = str(os.environ.get("STRING_SESSION")) or str(config.STRING_SESSION)
DELAY = int(os.environ.get("DELAY")) or int(config.DELAY)
BOT_LIST = {int(x) for x in os.environ.get("BOT_LIST").split()} or {int(config.BOT_LIST).split()}


waifu = Client(
    name="autowaifu_zyxdevs",
    api_id=APP_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
)


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "best_guess": ""}

    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


def get_data(img):
    searchUrl = "https://www.google.com/searchbyimage/upload"
    file_img = {"encoded_image": (img, open(img, "rb")), "image_content": ""}
    response = requests.post(searchUrl, files=file_img, allow_redirects=False)
    if os.path.exists(img):
        os.remove(img)
    if response.status_code == 400:
        return
    return response.headers["Location"]


@waifu.add_handler(
    MessageHandler(
        filters.user(BOT_LIST), filters.group & ~filters.edited & ~filters.forward
    )
)
async def autowaifu(client, message):
    if message.photo:
        if "add" in message.caption.lower():
            img = await message.download()
            fetchUrl = await get_data(img)
            match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
            guess = match["best_guess"]
            if not guess:
                return await message.reply_text("Failed to protecc this waifu.")
            guess = guess.replace("Results for", "")
            await time.sleep(DELAY)
            kek = await message.reply_text(f"/protecc {guess}")
            await time.sleep(DELAY)
            await kek.delete()


async def main():

    await waifu.start()
    print(
        """
-------------------
| System Started! |
-------------------
| By Yoga Pranata |
-------------------
"""
    )
    await idle()


loop = get_event_loop()
loop.run_until_complete(main())
