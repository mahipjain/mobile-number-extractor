import os
import re

mob_num = re.compile(r'(\+91-)?(\+91)?([7-9]{1})([0-9]{9})')

dir_path = "./dir0/"

for root, dirs, files in os.walk(dir_path):
	for file in files:
		fobj = open(os.path.join(root, file), "r")
		for line in fobj:
			line = line.rstrip()
			for (a,b,c,d) in re.findall(mob_num, line):
				print a + b + c + d
		fobj.close()