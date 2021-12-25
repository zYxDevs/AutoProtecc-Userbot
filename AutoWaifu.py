import time
import os
import requests

from bs4 import BeautifulSoup as bs
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
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")
DELAY = int(os.environ.get("DELAY"))
BOT_LIST = 


Waifu = Client(":memory:",
              bot_token=bot_token,
              api_id=api_id,
              api_hash=api_hash,
)


@Waifu.on_message()
async def autowaifu(client, message):
    if message.photo and message.user.id in BOT_LIST:
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
