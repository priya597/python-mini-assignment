def get_income():
    while True:
        try:
            income = int(input("Please enter your yearly income: "))
        except ValueError:
            print("invalid input, please enter yearly income as a number")
            continue
        else:
            break
    return income

def calculate_tax(income):
    if income <= 250000:  #2L 50 thousand
        tax = 0
    elif income >= 250000 and income <= 500000 : 
        tax = (income - 250000) * 0.05
    elif income >= 500000 and income <= 750000: 
        tax = (income - 500000) * 0.10 + 12500 
    elif income >= 750000 and income <= 1000000: 
        tax = (income - 750000) * 0.15 + 37500 
    elif income >= 1000000 and income <= 1250000:
        tax = (income - 1000000) * 0.20 + 75000 
    elif income >= 1250000 and income <= 1500000:
        tax = (income - 1250000) * 0.25 + 125000 
    else:
        tax = (income - 1500000) * 0.30 + 187500
    return tax

if __name__ == "__main__":
    income = get_income()
    tax = calculate_tax(income)
    print("you owe", tax, "Rupees in tax!")
