# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:21:25 2020

@author: BoringClub
"""

import web_scraper as ws
import pandas as pd

path = "E:/Python Development/Dataset/web scraper/chromedriver.exe"


df = ws.get_jobs("data scientist", 15, False, path, 15)


