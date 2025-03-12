import glob
import json

#filename, x, y, width, height

def blank(filename):
	return None, None, None, None, None

def full_screen(filename):
	return filename, 0, 0, 1920, 1080

def vertical_flame(filename):
	return filename, 656, 0, 608, 1080

def center(radius):
	return lambda filename: (filename, 1920/2 - radius, 1080/2 - radius, radius*2, radius*2)

def quiz_time(half_width, height):
	return lambda filename: (filename, 1920/2 - half_width, 240, half_width*2, height)

functions = [
	{"until":60, "fn": vertical_flame},
	{"until":92, "fn": full_screen},
	{"until":333, "fn": center(128)},
	{"until":1039, "fn": blank},
	{"until":1069, "fn": center(210)},
	{"until":1082, "fn": center(64)},
	{"until":1084, "fn": blank},
	{"until":1613, "fn": center(260)},
	{"until":1650, "fn": full_screen},
	{"until":1710, "fn": quiz_time(160, 540)},
	{"until":1772, "fn": quiz_time(230, 540)},
	{"until":1834, "fn": quiz_time(180, 540)},
	{"until":1900, "fn": quiz_time(360, 840)},
	{"until":2333, "fn": blank},
	{"until":2401, "fn": full_screen},
	{"until":2889, "fn": center(128)},
	{"until":2945, "fn": center(200)},
	{"until":2955, "fn": full_screen},
	{"until":3394, "fn": center(340)},
	{"until":3454, "fn": full_screen},
	{"until":3766, "fn": center(128)},
]

images = glob.glob("./all_flames/*")

data = []
functions_index = 0

for i in range(0, len(images)):
	filename, x, y, width, height = functions[functions_index]["fn"](images[i])
	data.append([filename, x, y, width, height])
	if functions[functions_index]["until"] <= i:
		functions_index+=1
		if len(functions) <= functions_index:
			break

with open("./background_data.json", "w") as f:
    json.dump(data, f, indent="\t")
