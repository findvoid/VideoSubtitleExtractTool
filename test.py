# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File     : test.py
   Author   : CoderPig
   date     : 2021-01-18 10:32 
   Desc     : 
-------------------------------------------------
"""
import os
from you_get import common as you_get
import requests as r
import json
import http.cookiejar

url = "https://www.bilibili.com/video/BV1554y1s7qG"
# you_get.load_cookies("bilibili.txt")
# you_get.any_download_playlist(url=url, cookies="bilibili.txt", info_only=False, output_dir=os.getcwd(), merge=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36'
}

if __name__ == '__main__':
    cookies = http.cookiejar.MozillaCookieJar("bilibili.txt")
    resp = r.get(url=url, headers=headers)
    print(resp.text)
