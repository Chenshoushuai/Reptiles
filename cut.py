import sh
def run(number):
	cmd1="ffmpeg -i "+"Obama"+str(number)+".mp4"+" -acodec copy -vn -ar 16000 "+"mp4/Obama"+str(number)+".mp4"
	rs1= sh.run(cmd1)

	cmd2="ffmpeg -i "+"mp4/Obama"+str(number)+".mp4"+" -ar 16000 mp3/Obama"+str(number)+".mp3"
	rs2= sh.run(cmd2)

	cmd3="ffmpeg -i "+"mp3/Obama"+str(number)+".mp3"+" -ar 16000 wav/Obama"+str(number)+".wav"
	rs3= sh.run(cmd3)
def main():
	for i in range():
		run(i)
if __name__ == '__main__':
	main()
