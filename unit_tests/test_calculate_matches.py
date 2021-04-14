import sys
sys.path.append('../')
import calculate_matches


def test_calculate_matches():
    test_path1 = "test_input_files/test_calculate_matches_input1.json"
    content = calculate_matches.calculate_matches(test_path1)
    assert content == 100

    test_path2 = "test_input_files/test_calculate_matches_input2.json"
    content = calculate_matches.calculate_matches(test_path2)
    assert content == 50.0
