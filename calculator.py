standard_deduction = {
    "single": 13850,
    "married": 27700,
    "married_separately": 13850,
    "head_of_household": 20800
}

over_65 ={
    "single": 15700,
    "married": 29200,
    "married_separately": 15350,
    "head_of_household": 22650
}

brackets = [
    {"min": 0, "max": 11000, "rate": 0.1},
    {"min": 11001, "max": 44725, "rate": 0.12},
    {"min": 44726, "max": 99375, "rate": 0.22},
    {"min": 99376, "max": 182100, "rate": 0.24},
    {"min": 182101, "max": 231250, "rate": 0.32},
    {"min": 231251, "max": 578125, "rate": 0.35},
    {"min": 578126, "max": float('inf'), "rate": 0.37}
]


# Taxable Income = Gross Income - Standard Deduction - Over 65 Deduction
def calc_federal_tax(income, filling_status):
    taxable = income - standard_deduction[filling_status] - over_65[filling_status]
    taxable = max(0, taxable)

    tax = 0.0
    for i in range(len(brackets)):
        lower_bound = brackets[i]["min"]
        upper_bound = brackets[i]["max"]
        rate = brackets[i]["rate"]
        if taxable > lower_bound:
            income_in_bracket = taxable - lower_bound
            tax += income * rate
        else:
            break
    return tax




def calc_state_tax(income, filling_status):
    pass


print(calc_federal_tax(120000, "single"))
