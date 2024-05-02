from Lab2 import bmi

def test_bmi_under_weight():
    bmi_value = bmi.calculate_bmi(1.73, 5.7)
    assert (bmi_value == -1)

def test_bmi_normal_weight():
    bmi_value = bmi.calculate_bmi(1.73, 57)
    assert (bmi_value == 0)

def test_bmi_over_weight():
    bmi_value = bmi.calculate_bmi(1.73, 570)
    assert (bmi_value == 1)