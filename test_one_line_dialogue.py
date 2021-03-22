import one_line_dialogue

test_content = "This a sentence\n which should be on\n one line."

expected_output = ['This a sentence\n', ' which should be on\n', ' one line.']

def test_one_line_dialogue():
	with open("test_dialogue_file.txt", 'w') as test_file:
		test_file.write(test_content)

	content = one_line_dialogue.one_line_dialogue("test_dialogue_file.txt")
	assert content == expected_output
