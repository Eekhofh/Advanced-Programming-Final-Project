#!/usr/bin/python3
import re

def label_line(line):
	line_dict = {}
	# if line consists of only newline(s): return the line
	if re.match(r'[\n]+', line):
		return line
	
	# if line starts with spaces + 'INT' or 'EXT': label line as S
	elif re.match(r'^     .*INT[\.\- ]', line) or re.match(r'^     .*EXT[\.\- ]', line):
		line = re.sub('^ [ ]+', r'', line)
		line_dict = {'S': line[:-1]}
		return line_dict
	
	# if line starts with 26 spaces and one or more uppercase letters: label line as C
	elif re.match(r'^                          [A-Z]+', line):
		line = re.sub('^ [ ]+', r'', line)
		line_dict = {'C': line[:-1]}
		return line_dict
	
	# if line starts with 16 spaces and one or more other character: label line as D
	# do not create a dictionary, but label the line as follows: 'D' + tab + line
	elif re.match(r'^                [a-zA-Z0-9-.,\']+', line):
		line = re.sub('^ [ ]+', r'', line)
		return 'D \t' + line
	
	# if line consists of 5 spaces at the beginning, one or more uppercase letters, no lowercase letters and ending with a newline:
	# if the length of the line is more than 60 characters or if the 2nd last character is a punctuation mark: label line as M
	# else label line as N
	elif re.match(r'^     [A-Z]+[^a-z]+\n', line):
		if len(line) > 60 or line[-2] in ".?!":
			line = re.sub('^ [ ]+', r'', line)
			line_dict = {'M': line[:-1]}
			return line_dict
		else:
			line = re.sub('^ [ ]+', r'', line)
			line_dict = {'N': line[:-1]}
			return line_dict
	
	# if line consists of one or more spaces and anything in parentheses: label line as N
	elif re.match(r'[ ]+\(.+\)', line):
		line = re.sub('^ [ ]+', r'', line)
		line_dict = {'N': line[:-1]}
		return line_dict
	
	# if line starts with 5 spaces and any alphanumeric character: label line as N 
	elif re.match(r'^     [a-zA-Z0-9-]+', line):
		line = re.sub('^ [ ]+', r'', line)
		line_dict = {'N': line[:-1]}
		return line_dict
	
	# else label line as M
	else:
		line = re.sub('^ [ ]+', r'', line)
		line_dict = {'M': line[:-1]}
		return line_dict
		

def main():
	# for every line in the .txt file, apply the label_line function
	with open('mi.txt', 'r', encoding='utf8') as infile:
		for line in infile:
			print(label_line(line))

if __name__ == '__main__':
	main()

