import sys
import re

file_name = ""

if len(sys.argv)>1:
	file_name = sys.argv[1]
else:
	print("Please pass the file name/path as a command line argument..")
	print("eg. python Word-Counter.py /path/to/text-file")
	exit(0)

with open(file_name,'r') as f:
	text = f.read()

words = re.split('\W+', text)

print(words)

print("Number of words in text =",len(words))
