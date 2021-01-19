# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File     : bilibli_video_download.py
   Author   : CoderPig
   date     : 2021-01-19 15:58 
   Desc     : B站视频下载
-------------------------------------------------
"""
import requests as r
import http.cookiejar
import cp_utils
import re
import json
import time
import subprocess


# B站视频类
class BVideo:
    def __init__(self, title=None, cid=None, bvid=None, avid=None, quality=0, flv_url=None, mp4_url=None, wav_url=None,
                 merge_video=None):
        self.title = title
        self.cid = cid
        self.bvid = bvid
        self.avid = avid
        self.quality = quality
        self.flv_url = flv_url
        self.mp4_url = mp4_url
        self.wav_url = wav_url
        self.merge_video = merge_video


# 提取视频信息的正则
play_info_pattern = re.compile(r'window\.__playinfo__=(\{.*?\})</script>', re.MULTILINE | re.DOTALL)
initial_state_pattern = re.compile(r'window\.__INITIAL_STATE__=(\{.*?\});', re.MULTILINE | re.DOTALL)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Origin': 'https://www.bilibili.com'
}

cookies_file = 'bilibili.txt'  # Cookies文件


# 获取mp4资源数据
def fetch_mp4_data(url):
    if headers.get('Referer') is not None:
        headers.pop('Referer')
    b_video = BVideo()
    resp = r.get(url=url, headers=headers, cookies=cookies)
    play_info_result = play_info_pattern.search(resp.text)
    if play_info_result is not None:
        data_json = json.loads(play_info_result.group(1))
        b_video.mp4_url = data_json['data']['dash']['video'][0]['baseUrl']
        b_video.wav_url = data_json['data']['dash']['audio'][0]['baseUrl']
    initial_result = initial_state_pattern.search(resp.text)
    if play_info_result is not None:
        print(initial_result.group(1))
        data_json = json.loads(play_info_result.group(1))
    return b_video


# 获取flv资源数据


def download(url, referer_url, file_type):
    print("下载：", url)
    headers['Referer'] = referer_url
    resp = r.get(url=url, headers=headers)
    file_name = '{}.{}'.format(str(int(round(time.time() * 1000))), file_type)
    with open(file_name, "wb+") as f:
        f.write(resp.content)
        print("视频保存成功")
    return file_name


def merge_video(video_path, audio_path, output_path):
    cmd = f'ffmpeg -i {video_path} -i {audio_path} -acodec copy -vcodec copy {output_path}'
    print(cmd)
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    cookies = http.cookiejar.MozillaCookieJar(cookies_file) \
        if cp_utils.is_dir_existed(cookies_file, mkdir=False) else None
    video_url = input("请输入想下载的视频链接：\n")
    video = fetch_mp4_data(video_url)
    # video_path = download(video.mp4_url, video_url, 'mp4')
    # audio_path = download(video.wav_url, video_url, 'wav')
    # merge_video(video_path, audio_path, "result.mp4")
