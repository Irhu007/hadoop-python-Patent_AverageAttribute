import sys

for line in sys.stdin:
	field = line.strip().split(",");
	if(field[8] and field[8].isdigit()):
		print field[4][1:-1]+"\t"+field[8]
