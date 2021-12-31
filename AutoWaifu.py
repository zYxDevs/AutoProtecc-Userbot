import time
import io
import os
import urllib
import requests
import aiohttp

from re import findall
from bs4 import BeautifulSoup
from aiohttp import ClientSession
from asyncio import (
    gather,
    get_event_loop,
    sleep,
)
from pyrogram import (
    Client,
    errors,
    filters,
    idle,
)


API_ID = int(os.environ.get("API_ID"))
API_HASH = str(os.environ.get("API_HASH"))
STRING_SESSION = str(os.environ.get("STRING_SESSION"))
DELAY = int(os.environ.get("DELAY"))
BOT_LIST = {int(x) for x in os.environ.get("BOT_LIST").split()}


Waifu = Client(
    STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)


u_ = """Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"""
headers_ = [("User-agent", u_)]


async def ParseSauce(googleurl):
    async with aiohttp.ClientSession(headers=headers_) as session:
        async with session.get(googleurl) as resp:
            source = await resp.read()
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


@Waifu.add_handler(
    MessageHandler(filters.group & ~filters.edited & ~filters.forward), group=0
)
async def autowaifu(client, message):
    if message.photo and message.from_user.id in BOT_LIST:
        img = await message.download()
        fetchUrl = await get_data(img)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        await sleep(DELAY)
        kek = await message.reply_text(f"/protecc {guess}")
        await sleep(DELAY)
        await kek.delete()


async def main():
    session = ClientSession()

    await Waifu.start()
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
