import employee_info

print("pytest for employree info")

def test_get_employees_by_age_range():
    expected_output = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    result = employee_info.get_employees_by_age_range(10,29)

    assert (expected_output == result)

def test_calculate_average_salary():
    expected_output = 361000/6
    result = employee_info.calculate_average_salary()

    assert (expected_output == result)

def test_get_employees_by_dept():
    expected_output = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    result = employee_info.get_employees_by_dept("Sales")

    assert (expected_output == result)