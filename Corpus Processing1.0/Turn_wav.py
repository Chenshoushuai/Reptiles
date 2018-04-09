#-*- coding: UTF-8 -*- 
import sh 
import os
def run(number,num):
	cmd1="ffmpeg -i "+"stream/Obama"+str(number)+".mp4"+" -acodec copy -vn -ar 16000 "+"mp4/Obama"+str(num)+".mp4"
	rs1= sh.run(cmd1)
	cmd2="ffmpeg -i "+"mp4/Obama"+str(num)+".mp4"+" -ar 16000 mp3/Obama"+str(num)+".mp3"
	rs2= sh.run(cmd2)
	cmd3="ffmpeg -i "+"mp3/Obama"+str(num)+".mp3"+" -ar 16000 wav/Obama"+str(num)+".wav"
	rs3= sh.run(cmd3)
	cmd4="sox wav/Obama"+str(num)+".wav "+"wav/Obama"+str(num)+"_.wav noisered ../noise/noise.prof 0.3"
	rs4= sh.run(cmd4)
	cmd5= "rm -rf wav/Obama"+str(num)+".wav"
	rs5=sh.run(cmd5)
def main():
	num=1;
	for i in range(210):
		string = "stream/Obama"+str(i)+".mp4"
		if os.path.exists(string)==True:
			run(i,num)
			num=num+1
		else:
			print "没有此文件"
if __name__ == '__main__':
	main()