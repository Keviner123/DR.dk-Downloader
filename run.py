#!/usr/bin/env python3
import urllib.request
import os

__author__ = "Keviner123"
__version__ = "0.1.0"
__license__ = "MIT"


STARTURL = "https://drod01o-vh.akamaihd.net/i/all/clear/streaming/43/5b5fbc1a6187a61a3411b343/Limbo-III--5-_29ac80d1b3c8424fb432bd8aac9e9ecc_,364,576,1128,2392,.mp4.csmil/segment"
ENDURL = "_3_av.ts"

def GetDownloadedClips():
	s = ""
	for root, dirs, files in os.walk("temp"):  
		for filename in sorted(files, key=lambda a: int(a.split(".")[0])):
			s+=str('temp/'+filename+"|")
	return('ffmpeg.exe -i "concat:'+s[:-1]+'" -c copy output.mp4')

def GetUrlIsAlive(url):
    request = urllib.request.Request(url)
    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False

def GetClipAmounts():
	i = 1;
	while(True):
		if (GetUrlIsAlive(STARTURL+str(i)+ENDURL) == False):
			return(i)
		i = i+1

def ClearTemp():
	filelist = [f for f in os.listdir("temp")]
	for f in filelist:
		os.remove(os.path.join("temp", f))
		
def main():
	ClearTemp()

	for i in range(1, GetClipAmounts()):
		if (GetUrlIsAlive(STARTURL+str(i)+ENDURL) == True):
			URL = STARTURL+str(i)+ENDURL
			urllib.request.urlretrieve(URL, "temp/"+str(i)+".mp4")
	os.system((GetDownloadedClips()))
	ClearTemp()
if __name__ == "__main__":
	main()