import price_info

print("Test - Price info")

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()

    assert (result == 46.75)

def test_cost_of_fruit():
    expected_output = 28
    result = price_info.cost_of_fruits('orange', 20)

    assert (result == expected_output)