# -*- coding:UTF-8 -*-
#multi_detect.py，是运行代码，实现音谱图的识别，语音的切分！  python3 ./multi_detect.py
from __future__ import print_function
#__future__ 至少确保在2.1之前版本的Python可以正常运行一些新的语言特性
import speech_segmentation as seg
import sh 

frame_size = 256
frame_shift =128
sr = 16000
for i in range(1,101):
	string = "Obama"+str(i)+".wav"
	seg_point,num = seg.multi_segmentation(string,sr,frame_size,frame_shift,plot_seg=True)
	print(seg_point)
	print(len(seg_point))
	for j in num:
		if j<len(seg_point)-1:
			#经过浮点数转换
			mm=int(seg_point[j]/60)
			ss=int(((seg_point[j]/60)-mm)*60)
			M=int(seg_point[j+1]/60)
			S=int(((seg_point[j+1]/60)-M)*60)
			cmd="ffmpeg -i "+"Obama"+str(i)+".wav"+" -ss 00:"+str(mm)+":"+str(ss)+" -to 00:"+str(M)+":"+str(S)+" -y ../wav/Obama"+str(i)+"_"+str(j)+".wav"
			rs= sh.run(cmd)
#multi_segmentation("Obama1.wav",sr=16000,frame_size=256,frame_shift=128,plot_seg=True) 
