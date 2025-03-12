import gc
import json
import sys

import cv2
import numpy as np
from PIL import Image

fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
video = cv2.VideoWriter("teto_output.mp4", fourcc, 24.0, (905, 1080))

with open("./teto_data.json", "r") as f:
	data = json.load(f)

	for i in data:
		print(i)
		if i[0] is None:
			blank = np.zeros((1080, 905, 3), np.uint8)
			video.write(blank)
			continue

		image = Image.open(i[0])
		if image is None:
			print("image is not found")
			break
		cropped = image.crop((i[1], 0, i[1]+i[2], 1080)).crop((0, 0, 905, 1080))
		video.write(cv2.cvtColor(np.array(cropped), cv2.COLOR_RGB2BGR))

video.release()
print("written")
