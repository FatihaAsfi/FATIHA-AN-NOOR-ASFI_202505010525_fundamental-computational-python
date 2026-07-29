from employee import get_employee
from salary import gross_salary, epf, socso, reward, net_salary
from report import print_report


def main():

    (
        employee_name,
        employee_id,
        basic_salary,
        allowance,
        epf_choice,
        socso_choice,
        overtime_hours,
        position,
        years
    ) = get_employee()

    gross = gross_salary(basic_salary, allowance, overtime_hours)

    if epf_choice == "Y":
        epf_amount = epf(gross)
    else:
        epf_amount = 0

    if socso_choice == "Y":
        socso_amount = socso(gross)
    else:
        socso_amount = 0

    reward_amount = reward(position, years)

    net = net_salary(gross, epf_amount, socso_amount, reward_amount)

    print_report(
        employee_name,
        employee_id,
        basic_salary,
        allowance,
        overtime_hours,
        gross,
        epf_amount,
        socso_amount,
        reward_amount,
        net
    )


if __name__ == "__main__":
    main()