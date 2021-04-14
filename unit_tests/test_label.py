import sys
sys.path.append('../')
import label


def test_label():
    input = "     INT. KIEV APARTMENT - NIGHT "
    expected_output = {"S": "INT. KIEV APARTMENT - NIGHT"}

    input = "                        MISSION: IMPOSSIBLE "
    expected_output = {"M": "MISSION: IMPOSSIBLE"}
    assert label.label_line(input) == expected_output
    # It was not possible to complete pycodestyle requirements on the next
    # two lines, due to it leading to errors in the pytest.
    input = "     We're in a large closet.  JACK KIEFER, an athletic American "
    expected_output = {"N": "We're in a large closet.  JACK KIEFER, an athletic American"}
    assert label.label_line(input) == expected_output
    input = "                          ANATOLY "
    expected_output = {"C": "ANATOLY"}
    assert label.label_line(input) == expected_output
    input = "                Kasimov, Kasimov, good that you called us."
    expected_output = "D \tKasimov, Kasimov, good that you called us."
    assert label.label_line(input) == expected_output
