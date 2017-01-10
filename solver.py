#!/usr/bin/python
import csv
import sys

def usage():
	print 'usage: solver.py -i <word_matrix.csv>'
	sys.exit(1)

def main(argv):
	if (len(argv) != 1):
		usage()
	
	f = open(sys.argv[1], 'rt')
	try:
		reader = csv.reader(f)
		for row in reader:
			print row
	finally:
		f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
