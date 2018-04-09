import wave
import pylab as pl
import numpy as np
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav

# 打开WAV文档
#f = wave.open(r"1_16.wav", "rb")
f = wave.open(r"arctic_a0002.wav", "rb")
# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# 读取波形数据
str_data = f.readframes(nframes)

out = open('data.txt','w')
print(str_data,file=out)
out.close()

f.close()

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 1
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)

'''(rate,sig) = wav.read("output.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])'''

# 绘制波形
pl.subplot(211) 
pl.plot(time, wave_data[0])
pl.plot(time, wave_data[0])
#pl.subplot(212) 
#pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()