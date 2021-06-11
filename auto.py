# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:02:03 2021
Licensed Under "GPU v3.0"
@author: Kgf123@Github
Copyright (C) 2020-2021 by Kgf123@Github, < https://github.com/Kgf123 >.
"""

import os
import requests
from asyncio import sleep
from bs4 import BeautifulSoup as bs
from telethon import *
import time
from Config import Config
XX = "A qt waifu appeared!"

DELAY = Config.DELAY
API_ID = Config.API_ID
API_HASH = Config.API_HASH
Client = TelegramClient(Config.STRING_SESSION, API_ID, API_HASH)


@Client.on(events.NewMessage(incoming=True))
async def reverse(event):
    if not event.media:
        return
    if not XX in event.text:
        return
    if not event.sender_id == 792028928:
        return
    dl = await Client.download_media(event.media, "resources/")
    file = {"encoded_image": (dl, open(dl, "rb"))}
    grs = requests.post(
        "https://www.google.com/searchbyimage/upload", files=file, allow_redirects=False
    )
    loc = grs.headers.get("Location")
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
    send = await Client.send_message(event.chat_id, f"/protecc {text}")
    await sleep(5)
    os.remove(dl)
Client.start()
print("Started")
Client.run_until_disconnected()
