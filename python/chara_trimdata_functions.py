import os

import cv2
import numpy as np


def decrease8Colors(img):
	dst = img.copy()
	idx = np.where((0<=img) & (128>img))
	dst[idx] = 64
	idx = np.where((128<=img) & (256>img))
	dst[idx] = 192
	return dst

def decrease256Colors(img):
	dst = img.copy()
	idx = np.where((0<=img) & (64>img))
	dst[idx] = 32
	idx = np.where((64<=img) & (128>img))
	dst[idx] = 96
	idx = np.where((128<=img) & (192>img))
	dst[idx] = 160
	idx = np.where((192<=img) & (256>img))
	dst[idx] = 224
	return dst

def blank(filename):
	return None, None, None

def fixed_position(x, width):
	return lambda filename: (filename, x, width)

def flame_left(filename):
	image = decrease8Colors(cv2.imread(filename))

	for x in range(0, image.shape[1]):
		if x == 0:
			continue
		currentBgr = image[0,x]
		previousBgr = image[0,x-1]
		diff = sum(abs(currentBgr - previousBgr))
		if 0 < diff:
			return filename, x, 575
	return filename, image.shape[1], 575

def flame_right(filename):
	image = decrease8Colors(cv2.imread(filename))

	for x in reversed(range(0, image.shape[1])):
		if x == 0:
			continue
		currentBgr = image[0,x]
		previousBgr = image[0,x-1]
		diff = sum(abs(currentBgr - previousBgr))
		if 0 < diff:
			return filename, x-575, 575
	return filename, image.shape[1], 575

def flame_center(filename):
	image = decrease256Colors(cv2.imread(filename))
	height = image.shape[0]-1

	left = 0
	for x in range(0, image.shape[1]):
		if x == 0:
			continue
		currentBgr = image[height,x]
		previousBgr = image[height,x-1]
		diff = sum(abs(currentBgr - previousBgr))
		if 0 < diff:
			left = x
			break

	right = 0
	for x in reversed(range(0, image.shape[1])):
		if x == 0:
			continue
		currentBgr = image[height,x]
		previousBgr = image[height,x-1]
		diff = sum(abs(currentBgr - previousBgr))
		if 0 < diff:
			right = x-1
			break

	return filename, left, right-left
