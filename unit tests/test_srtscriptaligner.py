'''
import sys
sys.path.append('../')
import srtscriptaligner


def test_load_file():
	return

def test_clean_srt():
	with open("test_input_files/test_srt.srt", "r") as test_srt:
		content = srtscriptaligner.clean_srt(test_srt)
		assert content == ""

def test_clean_script():
	return'''