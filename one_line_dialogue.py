# program makes all Dialogues on one line
import re


def one_line_dialogue(text_file):

	infile_list = []
	with open(text_file, 'r', encoding='utf8') as infile:
		for line in infile:
			infile_list.append(line)

	i = 0
	while i < len(infile_list):
		dialogue = []
		dialogue_dict = {}
		if re.match(r'^{\'C\'', infile_list[i]):
			dialogue_dict['C'] = infile_list[i][7:-3]
			for line in infile_list[i+1:]:
				if re.match('^D \t', line) or re.match('\n', line):
					line = re.sub(' [ ]+', r'', line[3:-1])
					dialogue.append(line)
				elif re.match('^{\'N\'', line):
					dialogue.append(line)
				else:
					break
			dialogue = [line for line in dialogue if line != '\n']
			dialogue = [line for line in dialogue if line != '']
			dialogue = [line for line in dialogue if not re.match(r'^{\'N\'', line)]
			dialogue_dict['D'] = "  ".join(dialogue)
			print(dialogue_dict)
		elif not re.match('^D \t', infile_list[i]) and not re.match('^{\'N\': \(', infile_list[i]):
			print(infile_list[i])
		i += 1

one_line_dialogue('labeled_script.txt')
