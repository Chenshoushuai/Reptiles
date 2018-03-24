#speech_segmentation.py
import numpy as np
import voice_activity_detect as vad
import librosa
import matplotlib.pyplot as plt


#Speech segmentation based on BIC
def compute_bic(mfcc_v,delta):
    m, n = mfcc_v.shape
    # print(m, n)

    sigma0 = np.cov(mfcc_v).diagonal()
    eps = np.spacing(1)
    realmin = np.finfo(np.double).tiny
    det0 = max(np.prod(np.maximum(sigma0,eps)),realmin)

    flat_start = 5

    range_loop = range(flat_start,n,delta)
    x = np.zeros(len(range_loop))
    iter = 0
    for index in range_loop:
        part1 = mfcc_v[:, 0:index]
        part2 = mfcc_v[:, index:n]

        sigma1 = np.cov(part1).diagonal()
        sigma2 = np.cov(part2).diagonal()

        det1 = max(np.prod(np.maximum(sigma1, eps)), realmin)
        det2 = max(np.prod(np.maximum(sigma2, eps)), realmin)

        BIC = 0.5*(n*np.log(det0)-index*np.log(det1)-(n-index)*np.log(det2))-0.5*(m+0.5*m*(m+1))*np.log(n)
        x[iter] = BIC
        iter = iter + 1

    maxBIC = x.max()
    maxIndex = x.argmax()
    if maxBIC>0:
        return range_loop[maxIndex]-1
    else:
        return -1


def speech_segmentation(mfccs):
    wStart = 0
    wEnd = 200
    wGrow = 200
    delta = 25

    m, n = mfccs.shape #查看矩阵或者数组的维数

    store_cp = []
    index = 0
    while wEnd < n:
        featureSeg = mfccs[:, wStart:wEnd]
        detBIC = compute_bic(featureSeg, delta)
        index = index + 1
        if detBIC > 0:
            temp = wStart + detBIC
            store_cp.append(temp)
            wStart = wStart + detBIC + 200
            wEnd = wStart + wGrow
        else:
            wEnd = wEnd + wGrow

    return np.array(store_cp)
   #multi_segmentation("Obama1.wav",sr=16000,frame_size=256,frame_shift=128,plot_seg=True)
def multi_segmentation(file,sr,frame_size,frame_shift,plot_seg = False): #plot_seg默认值是False
    y, sr = librosa.load(file, sr=sr)#加载音频文件，返回值：y:音频时间序列，sr:y的采样率
    #梅尔频率倒谱系数
    mfccs = librosa.feature.mfcc(y, sr, n_mfcc=12, hop_length=frame_shift, n_fft=frame_size)


    seg_point = speech_segmentation(mfccs / mfccs.max()) #seg_point是切分点的时间，数组

    seg_point = seg_point * frame_shift  #frame_shift是读框移位，frame_size是框的大小
    seg_point = np.insert(seg_point, 0, 0)
    seg_point = np.append(seg_point, len(y))
    rangeLoop = range(len(seg_point) - 1) #数组长度-1是为下面循环做准备，比如长度是5，5-1=4，0-4还是5个数

    output_segpoint = []
    for i in rangeLoop:
        temp = y[seg_point[i]:seg_point[i + 1]]
        x1, x2 = vad.vad(temp, sr=sr, framelen=frame_size, frameshift=frame_shift)
        if len(x1) == 0 or len(x2) == 0:
            continue
        elif seg_point[i + 1] == len(y):
            continue
        else:
            output_segpoint.append(seg_point[i + 1])

    if plot_seg: #画图的部分
        plt.figure('speech segmentation plot')
        plt.plot(np.arange(0, len(y)) / (float)(sr), y, "b-")

        for i in range(len(output_segpoint)):
            plt.vlines(output_segpoint[i] / (float)(sr), -1, 1, colors="c", linestyles="dashed")
            plt.vlines(output_segpoint[i] / (float)(sr), -1, 1, colors="r", linestyles="dashed")
        plt.xlabel("Time/s")
        plt.ylabel("Speech Amp")
        plt.grid(True)
        plt.show()
    return (np.asarray(output_segpoint) / float(sr))
