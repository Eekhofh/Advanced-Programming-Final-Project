import sys
import label
sys.path.append('../')


def test_label():
    assert label.label_line("     INT. KIEV APARTMENT - NIGHT ")
    == {"S": "INT. KIEV APARTMENT - NIGHT"}
    assert label.label_line("                        MISSION: IMPOSSIBLE ")
    == {"M": "MISSION: IMPOSSIBLE"}
    assert label.label_line("     We're in a large closet.  JACK KIEFER, \
                            an athletic American ")
    == {"N": "We're in a large closet.  JACK KIEFER, an athletic American"}
    assert label.label_line("                          ANATOLY ")
    == {"C": "ANATOLY"}
    assert label.label_line("                Kasimov, Kasimov, good that\
                             you called us.")
    == "D \tKasimov, Kasimov, good that you called us."
