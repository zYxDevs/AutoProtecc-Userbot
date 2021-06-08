# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:04:21 2021

@author: user
"""

import os

class Config:
    # Get these values from my.telegram.org
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    
    # Get this from https://replit.com/@TeamUltroid/UltroidStringSession
    
    STRING_SESSION = os.environ.get("STRING_SESSION")