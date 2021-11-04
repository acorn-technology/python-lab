
import math

from lab_1_1 import output_pi
from lab_2_1 import single_tail

def test_output_pi_2_decimals():
    assert output_pi(2) == 3.14, "Wrong pi"

def test_output_p1_9_decimals():
    assert output_pi(9) == 3.141592653, "Wrong pi"

def test_output_p1_0_decimals():
    assert output_pi("a") == "Input must be number", "Input must be number"

def test_output_p1_neative_number():
    assert output_pi(0) == "Input must be larger than 0", "Input must be larger than 0"

#############################################################

def test_lab21_single_tail(capsys):
    captured = capsys.readouterr()
    single_tail("testfile1.txt")
    assert captured.out == "11", "Should be last ten lines"
    assert captured.out == "12", "Should be last ten lines"

    #\n12\n13\n14\n15\n16\n17\n18\n19\n20\n"

