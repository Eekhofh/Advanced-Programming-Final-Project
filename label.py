import re

def label_line(line):
	if re.match(r'[\n]+', line):
		print(line)
	elif re.match(r'^     .*INT[\.\- ]', line) or re.match(r'^     .*EXT[\.\- ]', line):
		print('S \t' + line)
	elif re.match(r'^                          [A-Z]+', line):
		print('C \t' + line)
	elif re.match(r'^                [a-zA-Z0-9-.,\']+', line):
		print('D \t' + line)
	elif re.match(r'^     [A-Z]+[^a-z]+\n', line):
		if len(line) > 60 or line[-2] in ".?!":
			print('M \t' + line)
		else:
			print('N \t' + line)
	elif re.match(r'[ ]+\(.+\)', line):
		print('N \t' + line)
	elif re.match(r'^     [a-zA-Z0-9-]+', line):
		print('N \t' + line)
	else:
		print('M \t' + line)

def label_file(script):
	with open(script, 'r', encoding='utf8') as infile:
		for line in infile:
			label_line(line)

labeled_script = label_file('mi.txt')
print(labeled_script)
