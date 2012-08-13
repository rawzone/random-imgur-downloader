#!/usr/bin/python3.1
# By: Hans K. Nielsen
# hans@rawz0ne.com

# Script for grapping random images of imgur.com

# Imports
import random
import subprocess
import urllib.request
import os


# Variables
numOfPics = 5

imgUrl = "http://i.imgur.com/"

dlPath = "./output/"

shaSum = "9b5936f4006146e4e1e9025b474c02863c0b5614132ad40db4b925a10e8bfbb9"


# Functions
def randomnes():	# Function to generate random url to an images on imgur.com
	
	ext = ".jpg"
	
	r1 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	r2 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	r3 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	r4 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	r5 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	
	rT = r1 + r2 + r3 + r4 + r5
	rTE = rT + ext
	rTFull = imgUrl + rTE

	return (rTFull, rTE)


def downloadImages(rTFull, dlPath, filename):	# Download random generatet image url to ./output folder

	local_file_name = dlPath + filename

	with open(local_file_name, 'wb') as f:
		r = urllib.request.urlopen(rTFull).read()
		f.write(r)
		f.close()

	return local_file_name


def check_sha256sum(f, shaSum):	# Check sha256sum of downloaded image, check if dead image placeholder downloadet, if so download a replacement image.
	file_name = f
	
	output = subprocess.check_output(['sha256sum', file_name])

	newShaSum = output[:64]	# grap 64 chars of the shasum
	newShaSum = newShaSum.decode("utf-8")	# converting it to a string to compare to shaSum


	# check if new file is a placeholder
	if newShaSum == shaSum:
		print ("Dead image placeholder downloaded...")
		# Delete image
		os.remove(file_name)
		print ("Deleting file", file_name, "and downloading new image...\n")


		# Fetch new image
		rTFull = randomnes()
		local_file_name = downloadImages(rTFull[0], dlPath, rTFull[1])
		check_sha256sum(local_file_name, shaSum)
	else:

		return


# Main
rTFull = randomnes()
local_file_name = downloadImages(rTFull[0], dlPath, rTFull[1])
check_sha256sum(local_file_name, shaSum)
