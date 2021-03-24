import sys
import json
import ast

def load_file(filescript):
	# Loads a file and returns a list of the all the lines

	with open(filescript, encoding='latin-1') as f:
		data = f.readlines()

	return data

def clean_srt(srt_file):
	#places srt file content in dictionary
	clean_lines = []
	# remove spaces around the items
	for item in srt_file:
		if item.strip():
			clean_lines.append(item.strip())

	srt_dict = {}
	empty_list = []

	for item in clean_lines:
		if item.isnumeric():
			# if there is data in list save it to dictionary
			if empty_list:
				srt_dict[line_dict] = empty_list

			# saves the line number
			line_dict =  item
			srt_dict[line_dict] = ""
			empty_list = []

		else:
			empty_list.append(item)

	return srt_dict

def clean_script(text_script):
	# reads script, removes empty lines and convert to dictionary
	script_dict = {}
	counter = 0

	for element in text_script:
		# removes wrong quotes
		if not element.isspace():
			# convert to dictionary
			x = ast.literal_eval(element)
			script_dict[counter] = x
			counter += 1

	return script_dict

def main():

	filescript = sys.argv[1]
	text_script = load_file(filescript)
	text_script = clean_script(text_script)

	file_srt = sys.argv[2]
	srt_file = load_file(file_srt)
	cleaned_srt = clean_srt(srt_file)

	# iternate over the script
	for line_numer, text in text_script.items():
		if type(text) is dict:
			# check if current dictionary is dialogue
			if "D" in text.keys():
				# get value from dialogue 
				dialogue = text["D"]
				# iternate over dictionary and search for dialogue
				if dialogue != "":
					for srt_key, srt_value in cleaned_srt.items():
						if len(srt_value) > 1:

							timestamp = srt_value[0]
							current_dialogue = srt_value[1]

							if dialogue in current_dialogue:
								text["timestamp"] = timestamp

								del cleaned_srt[srt_key]
								break
								
	with open('output.json', 'w') as json_file:
		json.dump(text_script, json_file, indent = 2)

if __name__ == '__main__':
	main()












