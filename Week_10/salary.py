def gross_salary(basic_salary, allowance, overtime_hours):
    overtime_pay = overtime_hours * 25
    return basic_salary + allowance + overtime_pay


def epf(gross):
    return gross * 0.11


def socso(gross):
    return gross * 0.005


def reward(position, years):
    if position.lower() == "manager" and years > 3:
        return 500
    return 0


def net_salary(gross, epf_amount, socso_amount, reward_amount):
    return gross - epf_amount - socso_amount + reward_amount