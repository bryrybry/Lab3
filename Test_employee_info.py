import employee_info

print("pytest for employree info")

# def test_get_employees_by_age_range():
    # code

def test_calculate_average_salary():
    expected_output = 361000/6
    result = employee_info.calculate_average_salary()

    assert (expected_output == result)