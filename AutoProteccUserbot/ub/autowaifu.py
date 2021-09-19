import time
from pyrogram import filters
import os
from bs4 import BeautifulSoup
import requests
from AutoProteccUserbot import Waifu, DELAY, BOT_LISTA

@Waifu.on_message()
async def autowaifu(client, message):
    if message.photo:

        if message.user.id in BOT_LIST:
            dl = await Waifu.download_media(message, "resources/")
            file = {"encoded_image": (dl, open(dl, "rb"))}
            grs = requests.post(
                "https://www.google.com/searchbyimage/upload",
                files=file,
                allow_redirects=False,
            )
            loc = grs.headers.get("location")
            response = requests.get(
                loc,
                headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
                },
            )
            xx = bs(response.text, "html.parser")
            div = xx.find_all("div", {"class": "r5a77d"})[0]
            alls = div.find("a")
            text = alls.text
            time.sleep(DELAY)
            send = await Waifu.send_message(message.chat.id, f"/protecc {text}")
            await sleep(5)
            os.remove(dl)
