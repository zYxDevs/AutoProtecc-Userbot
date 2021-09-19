# # -*- coding: utf-8 -*-

# @author: zYxDevs
# Licensed Under 'GPU v3.0'
# Copyright (C) 2021 https://github.com/zYxDevs
# This file is part of Project-AutoProtecc.
# Pproject-AutoProtecc must not be copied and/or distributed without the express permission of zYxDevs.
# All rights reserved.


import os
import sys

BOT_LIST = "792028928 1232515770 1964681186"

class Config:
# Get these values from my.telegram.org
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
# Get this from https://replit.com/@YogaPranata1/PyroStringGen
    STRING_SESSION = os.environ.get("STRING_SESSION")
# Time delay in seconds so that it does not seep suspecious. Default = 5s
    DELAY = int(os.environ.get("DELAY", "5"))
# Waifu, Servant, Husbando bot id.
    BOT_LIST = {int(x) for x in os.environ.get("BOT_LIST").split()}
