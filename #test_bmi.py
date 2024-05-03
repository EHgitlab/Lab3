import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.conditional_queue(20)
    assert (result == -1)

def test_bmi_over_weight():
    result = bmi.conditional_queue(30)
    assert (result == 0)
    
def test_bmi_under_weight():
    result = bmi.conditional_queue(17)
    assert (result == 1)