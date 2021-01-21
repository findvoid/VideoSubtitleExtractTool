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

from idm import IDMan

import cp_utils
import re
import json
import time
import subprocess
import os

# 提取视频信息的正则
play_info_pattern = re.compile(r'window\.__playinfo__=(\{.*?\})</script>', re.MULTILINE | re.DOTALL)
initial_state_pattern = re.compile(r'window\.__INITIAL_STATE__=(\{.*?\});', re.MULTILINE | re.DOTALL)

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Origin': 'https://www.bilibili.com'
}

# Cookies文件
cookies_file = 'bilibili.txt'
flv_player_playurl = 'https://api.bilibili.com/x/player/playurl'


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


# 获取mp4资源数据
def fetch_mp4_data(url):
    if headers.get('Referer') is not None:
        headers.pop('Referer')
    b_video = BVideo()
    resp = r.get(url=url, headers=headers, cookies=cookies)
    print("请求：", resp.url)
    play_info_result = play_info_pattern.search(resp.text)
    if play_info_result is not None:
        data_json = json.loads(play_info_result.group(1))
        b_video.mp4_url = data_json['data']['dash']['video'][0]['baseUrl']
        b_video.wav_url = data_json['data']['dash']['audio'][0]['baseUrl']
    initial_result = initial_state_pattern.search(resp.text)
    if play_info_result is not None:
        data_json = json.loads(initial_result.group(1))
        video_data = data_json['videoData']
        b_video.title = video_data['title']
        b_video.avid = video_data['aid']
        b_video.bvid = video_data['bvid']
        b_video.cid = video_data['cid']
    return b_video


# 获取flv资源数据
def fetch_flv_data(b_video):
    params = {
        'qn': 0,
        'fnval': 0,
        'player': 1,
        'fnver': 0,
        'otype': 'json',
        'avid': b_video.avid,
        'bvid': b_video.bvid,
        'cid': b_video.cid
    }
    resp = r.get(flv_player_playurl, params=params, headers=headers, cookies=cookies)
    print("请求：", resp.url)
    if resp is not None:
        resp_json = resp.json()
        if 'data' in resp_json:
            b_video.flv_url = resp_json['data']['durl'][0]['url']
    return b_video


# 普通方式下载资源
def download_normal(url, referer_url, file_type):
    headers['Referer'] = referer_url
    print("下载：", url)
    resp = r.get(url=url, headers=headers)
    file_name = '{}.{}'.format(str(int(round(time.time() * 1000))), file_type)
    with open(file_name, "wb+") as f:
        f.write(resp.content)
        print("下载完成：", resp.url)
    return file_name


# IDM方式下载
def download_idm(url, referer_url, file_type):
    print("下载：", url)
    file_name = '{}.{}'.format(str(int(round(time.time() * 1000))), file_type)
    downloader = IDMan()
    downloader.download(url, output=file_name, referrer=referer_url)
    print("下载完成：", url)
    return file_name


# 合并音视频
def merge_mp4_wav(video_path, audio_path, output_path):
    print("音视频合并中~")
    cmd = f'ffmpeg -i {video_path} -i {audio_path} -acodec copy -vcodec copy {output_path}'
    subprocess.call(cmd, shell=True)
    print("合并完毕~")


if __name__ == '__main__':
    cookies = http.cookiejar.MozillaCookieJar(cookies_file) \
        if cp_utils.is_dir_existed(cookies_file, mkdir=False) else None
    video_url = input("请输入想下载的视频链接：\n")
    print("提取视频信息...")
    video = fetch_flv_data(fetch_mp4_data(video_url))
    user_choose = input("\n请输入下载资源的序号：\n1、mp4 \n2、flv\n")
    if user_choose == '1':
        mp4_path = download_idm(video.mp4_url, video_url, 'mp4')
        wav_path = download_idm(video.wav_url, video_url, 'wav')
        print("音视频下载完毕，开始合并资源")
        merge_mp4_wav(mp4_path, wav_path, "after_{}.mp4".format(str(int(round(time.time() * 1000)))))
    elif user_choose == '2':
        flv_path = download_idm(video.mp4_url, video_url, 'flv')
    else:
        print("错误输入")
        exit(0)
