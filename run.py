#!/usr/bin/env python3
import urllib.request

__author__ = "Keviner123"
__version__ = "0.1.0"
__license__ = "MIT"


def url_is_alive(url):
    request = urllib.request.Request(url)
    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False


def main():
	STARTURL = "https://drod08s-vh.akamaihd.net/i/all/clear/streaming/65/5b6a727d6187ac0c9876fb65/Limbo-III--10-_68d9e80559b9478a96059df5a547361e_,364,576,1128,2392,.mp4.csmil/segment"
	ENDURL = "_3_av.ts"


	for i in range(1, 100):
		if (url_is_alive(STARTURL+str(i)+ENDURL) == True):
			URL = STARTURL+str(i)+ENDURL

			urllib.request.urlretrieve(URL, str(i)+".mp4")


if __name__ == "__main__":
	main()