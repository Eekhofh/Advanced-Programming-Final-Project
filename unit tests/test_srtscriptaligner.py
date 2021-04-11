import sys
import srtscriptaligner
sys.path.append('../')


def test_load_file():
    expected_output = ['This a sentence\n', ' which should be on\n',
                       ' one line.']
    content = srtscriptaligner.load_file("test_input_files/\
                                         test_dialogue_file.txt")
    assert content == expected_output


def test_clean_srt():
    expected_output = {'1': ['00:00:52,346 --> 00:00:55,099',
                       'Come on, come on.', "She's been under too long."],
                       '2': ['00:01:23,210 --> 00:01:24,170', 'Come on.'],
                       '3': ''}
    with open("test_input_files/test_srt.srt", "r") as test_srt:
        content = srtscriptaligner.clean_srt(test_srt)
        assert content == expected_output


def test_clean_script():
    expected_output = {0: 1, 1: 2, 2: 3}
    content = srtscriptaligner.clean_script(
        {'1': ['00:00:52,346 --> 00:00:55,099', 'Come on, come on.',
         "She's been under too long."], '2': ['00:01:23,210 --> 00:01:24,170',
         'Come on.'], '3': ''})
    assert content == expected_output
