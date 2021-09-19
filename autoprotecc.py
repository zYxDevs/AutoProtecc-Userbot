# # -*- coding: utf-8 -*-

# @author: zYxDevs
# Licensed Under 'GPU v3.0'
# Copyright (C) 2021 https://github.com/zYxDevs
# This file is part of Project-AutoProtecc.
# Pproject-AutoProtecc must not be copied and/or distributed without the express permission of zYxDevs.
# All rights reserved

import os
import requests
import time
from asyncio import sleep
from bs4 import BeautifulSoup as bs
from pyrogram import Client
from Config import API_ID, API_HASH, STRING_SESSION, DELAY, BOT_LIST

Yoga = Client(STRING_SESSION, api_id=API_ID, api_hash=API_HASH, sleep_threshold=180)

@Yoga.on_message()
async def reverse(client, message):
    if not message.photo:
        return
    if message.user.id in BOT_LIST:
        dl = await Yoga.download_media(message, "resources/")
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
        e = await Yoga.send_message(message.chat.id, f"/protecc {text}")
        await sleep(5)
        e.delete()
        os.remove(dl)

print("[AutoProtecc] From Now and Forever All Harem is Yours. (c) @AutoProtecc")
Yoga.run()
