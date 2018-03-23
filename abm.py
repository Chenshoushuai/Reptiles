# -*- coding:utf-8 -*-
import urllib2
import re
import urllib
def Get_Url():
    src='https://open.163.com/movie/2013/1/M/1/M9177OLCL_MC9GIV1M1.html'
    content=urllib2.urlopen(src).read()
    dest=re.findall(r"http://open.163.com/movie/.*\.html",content)
    return dest[1:]
def Get_Lesson(src,num):
    content=urllib2.urlopen(src).read()
    l_pattern=re.compile(r"http.*\.m3u8")
    lesson=re.findall(l_pattern,content)
    lesson_src=lesson[0].replace("m3u8","mp4")
    urllib.urlretrieve(lesson_src,"Obama%s.mp4"%(num))

if __name__ == "__main__":
    Lesson_src=Get_Url()
    num=1
    count =1 
    for lesson in Lesson_src:
        if num%2==1:
            Get_Lesson(lesson,count)
            count=count+1
            num=num+1
        else :
            num=num+1
