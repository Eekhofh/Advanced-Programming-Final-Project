# program puts all Dialogues on the same line 
import re


def one_line_dialogue(text_file):
	
	# Opens the file given as an argument as a list of lines
	infile_list = []
	with open(text_file, 'r', encoding='utf8') as infile:
		for line in infile:
			infile_list.append(line)
			
	# Defines aligned_dialogue_file, which is an empty string
	aligned_dialogue_file = ""
	
	# Loops over all lines of the opened file list
	i = 0
	while i < len(infile_list):
		
		# Define the dialogue list and the dialogue_dict dictionary
		dialogue = []
		dialogue_dict = {}
		
		# If line begins with "{'C'":
		if re.match(r'^{\'C\'', infile_list[i]):
			
			# Add the line to dialogue dict with key C
			dialogue_dict['C'] = infile_list[i][7:-3]
			
			# Loop over the next few lines 
			# If they begin with D, add the lines to the dialogue list
			for line in infile_list[i+1:]:
				if re.match('^D \t', line) or re.match('\n', line):
					line = re.sub(' [ ]+', r'', line[3:-1])
					dialogue.append(line)
				elif re.match('^{\'N\'', line):
					dialogue.append(line)
				else:
					break
			
			# Edit the dialogue list to ensure that its content appears as one line 
			# Add the line to the dialogue dictionary with key D
			# Add the dialogue dictionary to the string aligned_dialogue_file
			dialogue = [line for line in dialogue if line != '\n']
			dialogue = [line for line in dialogue if line != '']
			dialogue = [line for line in dialogue if not re.match('^{\'N\'', line)]
			dialogue_dict['D'] = "  ".join(dialogue)
			aligned_dialogue_file += str(dialogue_dict) + '\n'
		
		# Else just add the line to the string aligned_dialogue_file
		elif not re.match('^D \t', infile_list[i]) and not re.match('^{\'N\': \(', infile_list[i]):
			aligned_dialogue_file += infile_list[i]
		i += 1
	
	# Return the string aligned_dialogue_file
	return aligned_dialogue_file

print(one_line_dialogue('labeled_script.txt'))

