# -*- coding:UTF-8 -*-
#multi_detect.py

from __future__ import print_function
#__future__ 至少确保在2.1之前版本的Python可以正常运行一些新的语言特性
import speech_segmentation as seg

frame_size = 256
frame_shift =128
sr = 16000

seg_point = seg.multi_segmentation("Obama1.wav",sr,frame_size,frame_shift,plot_seg=True)
print(seg_point)

#multi_segmentation("Obama1.wav",sr=16000,frame_size=256,frame_shift=128,plot_seg=True)
