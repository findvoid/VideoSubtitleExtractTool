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
# from idm import IDMan

url = "https://www.bilibili.com/video/BV1554y1s7qG"
# you_get.load_cookies("bilibili.txt")
# you_get.any_download_playlist(url=url, cookies="bilibili.txt", info_only=False, output_dir=os.getcwd(), merge=True)


if __name__ == '__main__':
    cookies = http.cookiejar.MozillaCookieJar("bilibili.txt")
    # resp = r.get(url=url, headers=headers, cookies=cookies)
    # print(resp.text)
    # downloader = IDMan()
    # download_url = "https://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/35/26/143182635/143182635_da2-1-64.flv?e" \
    #                "=ig8euxZM2rNcNbKBhwdVhoMM7WdVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENv" \
    #                "No8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F" \
    #                "1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1611047620&gen=playurl&os=kodobv&oi=20054" \
    #                "80449&trid=95df7eeb4c384372bf7a106860d1aa3eu&platform=pc&upsig=4e2a26137f1fe3a58cc3255cf3e" \
    #                "c25cc&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=67402819&orderid=0,3&agrr=" \
    #                "1&logo=80000000 "
    # referer_url = "https://www.bilibili.com/video/BV1RJ41177XR"
    # downloader.download(download_url, os.getcwd(), referrer=referer_url)

    download_url = "https://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/35/26/143182635/143182635_da2-1-64.flv?e" \
                   "=ig8euxZM2rNcNbKBhwdVhoMM7WdVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENv" \
                   "No8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F" \
                   "1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1611047620&gen=playurl&os=kodobv&oi=20054" \
                   "80449&trid=95df7eeb4c384372bf7a106860d1aa3eu&platform=pc&upsig=4e2a26137f1fe3a58cc3255cf3e" \
                   "c25cc&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=67402819&orderid=0,3&agrr=" \
                   "1&logo=80000000"
    referer_url = "https://www.bilibili.com/video/BV1RJ41177XR"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
        'Referer': referer_url,
        'Origin': 'https://www.bilibili.com'
    }
    resp = r.get(url=download_url, headers=headers)
    with open("video.flv", "wb+") as f:
        f.write(resp.content)
        f.close()
        print("视频保存成功")
