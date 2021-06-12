# # -*- coding: utf-8 -*-

# @author: Kgf123
# Licensed Under 'GPU v3.0'
# Copyright (C) 2021 https://github.com/Kgf123
# This file is part of Project-Autowaifu.
# Pproject-Autowaifu must not be copied and/or distributed without the express permission of Kgf123.
# All rights resrved


import os


class Config:
    # Get these values from my.telegram.org
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")

    # Get this from https://replit.com/@TeamUltroid/UltroidStringSession
    STRING_SESSION = os.environ.get("STRING_SESSION")

    # Time delay in seconds so that it does not seep suspecious. Default = 5s

    DELAY = int(os.environ.get("DELAY"))

    