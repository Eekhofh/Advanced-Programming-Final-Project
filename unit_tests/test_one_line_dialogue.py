import sys
sys.path.append('../')
import one_line_dialogue

test_content = "This a sentence\n which should be on\n one line."

expected_output = 'This a sentence\n which should be on\n one line.'


def test_one_line_dialogue():
    file_path = "../unit_tests/test_input_files/test_dialogue_file.txt"
    content = one_line_dialogue.one_line_dialogue(file_path)
    assert content == expected_output
