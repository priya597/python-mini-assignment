from taxcalculator import calculate_tax


def test_income_under_5lpa():
    assert calculate_tax(499999) == 12499.95
    
def test_income_under_7lpa():
    assert calculate_tax(699999) == 12499.95
    
def test_income_under_10lpa():
    assert calculate_tax(999999) == 12499.95
    
def test_income_under_125lpa():
    assert calculate_tax(1549999) == 12499.95
    
def test_income_under_15lpa():
    assert calculate_tax(149999) == 12499.95
    
 def test_income_under_1875lpa():
    assert calculate_tax(1899999) == 12499.95
