#!/usr/bin/python3

# Imports
import random
import subprocess
import urllib.request
import os
import sys


# Variables
numOfPics = 300	# number of pictures to download

imgUrl = 'http://i.imgur.com/'

dlPath = './output/'	# output dir for images

shaSum = '9b5936f4006146e4e1e9025b474c02863c0b5614132ad40db4b925a10e8bfbb9'	# sha256sum of placeholder image from imgur.com

tries = 1

# Functions
def randomnes():	# Function to generate random url to images on imgur.com
	
	ext = '.jpg'

	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	
	r1 = random.choice(chars)
	r2 = random.choice(chars)
	r3 = random.choice(chars)
	r4 = random.choice(chars)
	r5 = random.choice(chars)
	
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


def check_sha256sum(f, shaSum, numOfPics, tries):	# Check sha256sum of downloaded image, check if dead image placeholder downloadet, if so download a replacement image.
	file_name = f
	
	output = subprocess.check_output(['sha256sum', file_name])

	newShaSum = output[:64]	# grap 64 chars of the shasum
	newShaSum = newShaSum.decode('utf-8')	# converting it to a string to compare to shaSum


	# check if new file is a placeholder
	if newShaSum == shaSum:
		print ('Try number:', tries, '- dead image placeholder downloaded...')
		tries += 1

		# Delete image
		os.remove(file_name)
		shortFileName = file_name[9:]
		print ('deleting file', shortFileName, 'and downloading new image...\n')

		# Fetch new image
		rTFull = randomnes()
		local_file_name = downloadImages(rTFull[0], dlPath, rTFull[1])
		check_sha256sum(local_file_name, shaSum, numOfPics, tries)
		
	else:
		print ('Try number:', tries, '- done!\n\n')

		return


def check_output_dir(f):
	outputDir = os.path.dirname(f)
	print ('Checking if output folder exist...')
	if not os.path.exists(outputDir):
		print ('Output dir not found, making one...\n')
		os.makedirs(outputDir)
	else:
		print ('output folder exists...\n')


# Main
check_output_dir(dlPath)
print ('Need to download', numOfPics, 'images...\n')
for i in range(numOfPics):
	rTFull = randomnes()
	local_file_name = downloadImages(rTFull[0], dlPath, rTFull[1])
	check_sha256sum(local_file_name, shaSum, numOfPics, tries)
