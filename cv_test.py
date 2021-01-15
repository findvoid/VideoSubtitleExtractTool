# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File     : cv_test.py
   Author   : CoderPig
   date     : 2021-01-15 17:23 
   Desc     : 
-------------------------------------------------
"""
import cv2
import config_getter
import os

video_before_dir = os.path.join(os.getcwd(), config_getter.get_config(key="video_before_dir"))
subtitle_after_dir = os.path.join(os.getcwd(), config_getter.get_config(key="subtitle_after_dir"))


def save_image(image, num):
    address = os.path.join(subtitle_after_dir, str(num) + '.jpg')
    cv2.imwrite(address, image)


if __name__ == '__main__':
    videoCapture = cv2.VideoCapture(os.path.join(video_before_dir, "1.flv"))  # 读取视频文件
    success, frame = videoCapture.read()
    i = 0
    timeF = 15  # 帧率
    j = 0
    while success:
        i = i + 1
        if i > 68 * 15:
            if i < 1730 * 15:
                if i % timeF == 0:
                    j = j + 1
                    save_image(frame, j)
                    print("保存图片：{}".format(j))
                success, frame = videoCapture.read()
            else:
                break
        else:
            success, frame = videoCapture.read()
