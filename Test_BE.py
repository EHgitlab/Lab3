import Lab2.BE as be
#test_BE.py
def test_bmi_normal_weight():
    result = be.conditional_queue(20)
    assert (result == -1)

def test_bmi_over_weight():
    result = be.conditional_queue(30)
    assert (result == 0)
    
def test_bmi_under_weight():
    result = be.conditional_queue(17)
    assert (result == 1)