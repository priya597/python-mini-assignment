from taxcalculator import calculate_tax

def test_income_under_5lpa():
	assert calculate_tax(499999) == 12499.95;