import glob
import json

import chara_trimdata_functions

functions = [
	{"until":96, "fn": chara_trimdata_functions.blank},
	{"until":333, "fn": chara_trimdata_functions.fixed_position(1112, 575)},
	{"until":576, "fn": chara_trimdata_functions.blank},
	{"until":850, "fn": chara_trimdata_functions.flame_right},
	{"until":1039, "fn": chara_trimdata_functions.flame_left},
	{"until":1069, "fn": chara_trimdata_functions.flame_right},
	{"until":1900, "fn": chara_trimdata_functions.fixed_position(1222, 575)},
	{"until":2147, "fn": chara_trimdata_functions.blank},
	{"until":2333, "fn": chara_trimdata_functions.flame_center},
	{"until":2889, "fn": chara_trimdata_functions.fixed_position(1112, 575)},
	{"until":2909, "fn": chara_trimdata_functions.flame_right},
	{"until":3451, "fn": chara_trimdata_functions.fixed_position(1229, 575)},
	{"until":3704, "fn": chara_trimdata_functions.fixed_position(1112, 575)},
]

images = glob.glob("./all_flames/*")

data = []
functions_index = 0

for i in range(0, len(images)):
	filename, x, width = functions[functions_index]["fn"](images[i])
	data.append([filename,x,width])
	if functions[functions_index]["until"] <= i:
		functions_index+=1
		if len(functions) <= functions_index:
			break

with open("./teto_data.json", "w") as f:
    json.dump(data, f, indent="\t")
