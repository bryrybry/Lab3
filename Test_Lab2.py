from Lab2 import Lab2

print("Lab2_pytest!!!!!")

def test_find_min_max():
    input_list = [34, 21, 100, 3, 69, 137, 56]
    expected_min_output = 3
    expected_max_output = 137

    result = Lab2.find_min_max(input_list)

    assert (result[0] == expected_min_output and result[1] == expected_max_output)

def test_calc_average():
    input_list = [34, 21, 100, 3, 69, 137, 56]
    expected_output = 60

    result = Lab2.calc_average(input_list)

    assert (result == expected_output)

def test_calc_median():
    # odd number of elements
    input_list0 = [34, 21, 100, 3, 69, 137, 56]
    expected_output0 = 56
    # even number of elements
    input_list1 = [34, 21, 100, 3, 69, 137, 56, 3]
    expected_output1 = 45

    result0 = Lab2.calc_median(input_list0)
    result1 = Lab2.calc_median(input_list1)

    assert (result0 == expected_output0 and result1 == expected_output1)