# imgurl script version 0.1
# by: Hans K. Nielsen
# hans@rawz0ne.com

# Script to download random images from imgur.com by generating random images urls

# TODO
#
# Add a function to generate urls by an aldorythm you deside and "wordlists".
# 
# Add a feature to output a HTML page with all images included for easy viewing.
#
# Some of the images are dead once, download images test sha256sum of it, if = 9b5936f4006146e4e1e9025b474c02863c0b5614132ad40db4b925a10e8bfbb9 images is dead, deleate and get another one.

# Imports
import string
from types import *
import random

# Variables
LCL = string.ascii_lowercase	# string with all lowercase letters
UCL = string.ascii_uppercase	# string with all uppercase letters

numOfPics = 100	# numbers of pictures to download, need to be able to set this vist a -num xx tag. Default is 100

imgUrl = "http://i.imgur.com/"
ext = ".jpg"

# Debugging:

#print LCL
#print UCL
#print numOfPics


# Functions:

def randomnes(n, LCL, UCL):	# generating random chars for appending the url

	r1 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
	r2 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
	r3 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
	r4 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
	r5 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

	rT = r1 + r2 + r3 + r4 + r5
	return rT


# Main
random = randomnes(numOfPics, LCL, UCL)
print imgUrl + random + ext
