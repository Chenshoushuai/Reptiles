# -*- coding:UTF-8 -*-

from __future__ import print_function
#__future__ 至少确保在2.1之前版本的Python可以正常运行一些新的语言特性
import speech_segmentation as seg
import sh

frame_size = 256
frame_shift =128
sr = 16000
for i in range(47,101):
    string = "../1/wav/Obama"+str(i)+"_.wav"
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
            #cmd1="ffmpeg -i"+"Obama"+str(i)+".wav"+" -ac 1 -q:a 1 -y Obama"+str(i)+".wav"
            #rs1=sh.run(cmd1)
            cmd="ffmpeg -i "+"../1/wav/Obama"+str(i)+"_.wav"+" -ss 00:"+str(mm)+":"+str(ss)+" -to 00:"+str(M)+":"+str(S)+" -ac 1 -q:a 1 -y  ../1/Wav_crop/Obama"+str(i)+"_"+str(j)+".wav"
            #cmd="ffmpeg -i "+"Obama"+str(i)+".wav"+" -ss 00:"+str(mm)+":"+str(ss)+" -to 00:"+str(M)+":"+str(S)+" -y  ../Wav_crop/Obama"+str(i)+"_"+str(j)+".wav"
            rs= sh.run(cmd)

            cmd1="ffmpeg -i ../1/Wav_crop/Obama"+str(i)+"_"+str(j)+".wav -vol 1000 ../1/Wav_crop/"+str(i)+"_"+str(j)+".wav"
            rs1=sh.run(cmd1)

            cmd2="rm -rf ../1/Wav_crop/Obama"+str(i)+"_"+str(j)+".wav"
            rs2=sh.run(cmd2)