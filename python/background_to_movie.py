import json

import cv2
import numpy as np
from PIL import Image

fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
video = cv2.VideoWriter("background_output.mp4", fourcc, 24.0, (1920, 1080))

with open("./background_data.json", "r") as f:
	data = json.load(f)

	for i in data:
		print(i)
		if i[0] is None:
			blank = np.zeros((1080, 1920, 3), np.uint8)
			video.write(blank)
			continue

		image = Image.open(i[0])
		if image is None:
			print("image is not found")
			break
		cropped = image.crop((i[1], i[2], i[1]+i[3], i[2]+i[4])).crop((0, 0, 1920, 1080))
		video.write(cv2.cvtColor(np.array(cropped), cv2.COLOR_RGB2BGR))

video.release()
print("written")
