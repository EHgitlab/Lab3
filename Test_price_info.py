import price_info as price

test_price_list={'guava' : 2.20, 'orange':1.50, 'watermelon': 9.24, 'pineapple': 2.71, 'pear' : 1.90, 'papaya': 9.95, 'pomegranate': 8.95, 'passionfruit': 11.5}

def test_total_cost_shopping():
    test_quantity_list={'guava' : 7, 'orange':9, 'watermelon':12, 'pineapple':5, 'pear' :3, 'papaya':6, 'pomegranate':1, 'passionfruit':12}
    result = price.total_cost_shopping(test_price_list, test_quantity_list)
    test_result = 365.67999999999995
    assert (result == test_result)

def test_cost_of_fruits():
    test_fruit = 'passionfruit'
    test_quantity = 7
    result = price.cost_of_fruits(test_fruit, test_quantity, test_price_list)
    expected_result = 80.5
    assert(result == expected_result)