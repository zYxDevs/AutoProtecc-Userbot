# # -*- coding: utf-8 -*-

# @author: Kgf123
# Licensed Under 'GPU v3.0'
# Copyright (C) 2021 https://github.com/Kgf123
# This file is part of Project-Autowaifu.
# Pproject-Autowaifu must not be copied and/or distributed without the express permission of Kgf123.
# All rights resrved


import requests
from asyncio import sleep
from bs4 import BeautifulSoup as bs
from pyrogram import *
import time
from Config import Config
import os


DELAY = Config.DELAY
API_ID = Config.API_ID
API_HASH = Config.API_HASH
Client = Client(session_name=Config.STRING_SESSION, api_id=API_ID, api_hash=API_HASH)


@Client.on_message()
async def reverse(client, message):
    if message.photo:

        if message.from_user.id == 792028928:
            dl = await Client.download_media(message, "resources/")
            file = {"encoded_image": (dl, open(dl, "rb"))}
            grs = requests.post(
                "https://www.google.com/searchbyimage/upload",
                files=file,
                allow_redirects=False,
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
            send = await Client.send_message(message.chat.id, f"/protecc {text}")
            await sleep(5)
            os.remove(dl)


print("Bot Started")
Client.run()
