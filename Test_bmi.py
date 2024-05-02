from Lab2 import bmi

def test_bmi_under_weight():

    assert (bmi_value < 18.5)

def test_bmi_normal_weight():
    
    assert (18.5 <= bmi_value <= 25.0)

def test_bmi_over_weight():

    assert (bmi_value > 25.0)