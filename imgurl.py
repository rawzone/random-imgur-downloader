# imgurl script version 0.1
# by: Hans K. Nielsen
# hans@rawz0ne.com

# Script to download random images from imgur.com by generating random images urls

# TODO
#
#	*	Add a function to generate urls by an aldorythm you deside and "wordlists".
#	*	Add a feature to output a HTML page with all images included for easy viewing.
#	*	Some of the images are dead once, download images test sha256sum of it, if = 9b5936f4006146e4e1e9025b474c02863c0b5614132ad40db4b925a10e8bfbb9 images is dead, deleate and get another one.
#	*	Resize large images after download - Filesize or image size?


# Imports
import string
from types import *
import random
import itertools
import urllib2


# Variables
LCL = string.ascii_lowercase	# string with all lowercase letters
UCL = string.ascii_uppercase	# string with all uppercase letters

numOfPics = 10	# numbers of pictures to download, need to be able to set this vist a -num xx tag. Default is 10

imgUrl = "http://i.imgur.com/" # url of imgur, do not change unless they change there site strugture
ext = ".jpg"	# the images extention to use

dlPath = "./output/"	# The download path to store image files.


# Functions:
def randomnes(numOfPics, LCL, UCL):	# generating numOfPic x urls for images
	rTList = []
	for _ in itertools.repeat(rTList, numOfPics):
		
		r1 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		r2 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		r3 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		r4 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		r5 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

		rT = r1 + r2 + r3 + r4 + r5
		rTE = rT + ext
		rTFull = imgUrl + rTE
		
		rTList.append(rTFull)
	return rTList


def downloadImages(rTList, dlPath):	# downloading iamges from rTList
	url = rTList[1]

	file_name = url.split('/')[-1]
	file_name = dlPath + file_name
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
		break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,
	f.close()


# Main
for i in range(numOfPics):
	rTList = randomnes(numOfPics, LCL, UCL)	# Call to randomnes function to generate rTList, a random list of urls to images.
	downloadImages(rTList, dlPath)
