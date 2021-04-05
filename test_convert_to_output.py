import convert_to_output
import json

test_dict = {"Line 1": {"C": "JACK", "D": "Great. Come on.", "timestamp": "00:01:23,210 --> 00:01:24,170"},
			"Line 2": {"C": "CLAIRE", "D": "Did we get it?", "timestamp": "00:02:57,429 --> 00:02:58,889"}}

expected_csv = "line,metadata,scene boundary,scene description,actor,dialogue,time\nLine 1,,,,JACK,Great. Come on.,\"00:01:23,210 --> 00:01:24,170\"\nLine 2,,,,CLAIRE,Did we get it?,\"00:02:57,429 --> 00:02:58,889\"\n"
expected_json = {"Line 1": {"C": "JACK","D": "Great. Come on.","timestamp": "00:01:23,210 --> 00:01:24,170"},"Line 2": {"C": "CLAIRE","D": "Did we get it?","timestamp": "00:02:57,429 --> 00:02:58,889"}}

def test_convert_to_csv():
	with open(convert_to_output.convert_to_csv(test_dict), 'r') as test_csv:
		content = test_csv.read()
		assert content == expected_csv

def test_convert_to_json():
	with open(convert_to_output.convert_to_json(test_dict), 'r') as test_json:
		content = test_json.read()

		expected_output = json.dumps(expected_json, indent=2)
		assert content == expected_output