import re

def label_line(line):
	line_dict = {}
	if re.match(r'[\n]+', line):
		print(line)
	elif re.match(r'^     .*INT[\.\- ]', line) or re.match(r'^     .*EXT[\.\- ]', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'S': line[:-1]}
		print(line_dict)
	elif re.match(r'^                          [A-Z]+', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'C': line[:-1]}
		print(line_dict)
	elif re.match(r'^                [a-zA-Z0-9-.,\']+', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'D': line[:-1]}
		print(line_dict)
	elif re.match(r'^     [A-Z]+[^a-z]+\n', line):
		if len(line) > 60 or line[-2] in ".?!":
			line = re.sub(' [ ]+', r'', line)
			line_dict = {'M': line[:-1]}
			print(line_dict)
		else:
			line = re.sub(' [ ]+', r'', line)
			line_dict = {'N': line[:-1]}
			print(line_dict)
	elif re.match(r'[ ]+\(.+\)', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'N': line[:-1]}
		print(line_dict)
	elif re.match(r'^     [a-zA-Z0-9-]+', line):
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'N': line[:-1]}
		print(line_dict)
	else:
		line = re.sub(' [ ]+', r'', line)
		line_dict = {'M': line[:-1]}
		print(line_dict)

def label_file(script):
	with open(script, 'r', encoding='utf8') as infile:
		for line in infile:
			label_line(line)

labeled_script = label_file('mi.txt')
print(labeled_script)
