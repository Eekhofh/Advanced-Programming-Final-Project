import re

def label_line(line):
	line_dict = {}
	if re.match(r'[\n]+', line):
		return line
	elif re.match(r'^     .*INT[\.\- ]', line) or re.match(r'^     .*EXT[\.\- ]', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'S': line[:-1]}
		return line_dict
	elif re.match(r'^                          [A-Z]+', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'C': line[:-1]}
		return line_dict
	elif re.match(r'^                [a-zA-Z0-9-.,\']+', line):
		line = re.sub(' [ ]+', r'', line)
		return 'D \t' + line
	elif re.match(r'^     [A-Z]+[^a-z]+\n', line):
		if len(line) > 60 or line[-2] in ".?!":
			line = re.sub(' [ ]+', r'', line)
			line_dict = {'M': line[:-1]}
			return line_dict
		else:
			line = re.sub(' [ ]+', r'', line)
			line_dict = {'N': line[:-1]}
			return line_dict
	elif re.match(r'[ ]+\(.+\)', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'N': line[:-1]}
		return line_dict
	elif re.match(r'^     [a-zA-Z0-9-]+', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'N': line[:-1]}
		return line_dict
	else:
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'M': line[:-1]}
		return line_dict
		

def main():
	with open('mi.txt', 'r', encoding='utf8') as infile:
		for line in infile:
			print(label_line(line))

if __name__ == '__main__':
	main()

