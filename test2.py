# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File     : test2.py
   Author   : CoderPig
   date     : 2021-01-19 15:45 
   Desc     : 
-------------------------------------------------
"""
import requests as r

if __name__ == '__main__':
    download_url = "https://xy183x20x156x106xy.mcdn.bilivideo.cn:4483/upgcxcode/35/26/143182635/143182635_da2-1-30280.m4s?expires=1611049856&platform=pc&ssig=gA5NQ5LBTEJwxC7A2VcmTw&oi=2005480449&trid=753eba3eba17460b8ce60ea848e4b31fu&nfc=1&nfb=maPYqpoel5MI3qOUX6YpRA==&mcdnid=9000114&mid=67402819&orderid=0,3&agrr=1&logo=A0000100"
    referer_url = "https://www.bilibili.com/video/BV1RJ41177XR"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
        'Referer': referer_url,
        'Origin': 'https://www.bilibili.com'
    }
    resp = r.get(url=download_url, headers=headers)
    with open("video.wav", "wb+") as f:
        f.write(resp.content)
        f.close()
        print("视频保存成功")
