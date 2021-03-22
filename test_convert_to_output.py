import convert_to_output

test_dict = {"Line 1": {"actor": "JACK", "line": "Great. Come on.", "time": "00:01:23,210 --> 00:01:24,170"},
			"Line 2": {"actor": "CLAIRE", "line": "Did we get it?", "time": "00:02:57,429 --> 00:02:58,889"}}

expected_csv = "line,actor,dialogue,time\n1,JACK,Great. Come on.,\"00:01:23,210 --> 00:01:24,170\"\n2,CLAIRE,Did we get it?,\"00:02:57,429 --> 00:02:58,889\"\n"
expected_json = '{"Line 1": {"actor": "JACK", "line": "Great. Come on.", "time": "00:01:23,210 --> 00:01:24,170"}, "Line 2": {"actor": "CLAIRE", "line": "Did we get it?", "time": "00:02:57,429 --> 00:02:58,889"}}'

def test_convert_to_csv():
	with open(convert_to_output.convert_to_csv(test_dict), 'r') as test_csv:
		content = test_csv.read()
		assert content == expected_csv

def test_convert_to_json():
	with open(convert_to_output.convert_to_json(test_dict), 'r') as test_json:
		content = test_json.read()
		assert content == expected_json