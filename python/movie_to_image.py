import os

import cv2

movie_path = "./mesmerizer.mp4"
save_dir_path = "./all_flames/"

capture = cv2.VideoCapture(movie_path)

os.makedirs(save_dir_path, exist_ok=True)
n = 0

while True:
	ret, frame = capture.read()
	if ret:
		cv2.imwrite(save_dir_path + str(n).zfill(4) + ".png", frame)
		n += 1
	else:
		break
