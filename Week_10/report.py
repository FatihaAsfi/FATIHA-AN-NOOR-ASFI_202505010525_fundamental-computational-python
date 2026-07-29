def print_report(
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
):

    print("\n========== Employee Information ==========")
    print("Employee Name :", employee_name)
    print("Employee ID   :", employee_id)
    print("Basic Salary  : RM", format(basic_salary, ".2f"))
    print("Allowance     : RM", format(allowance, ".2f"))
    print("Overtime Hrs  :", overtime_hours)

    print("\n============= Salary Report =============")
    print("Gross Salary  : RM", format(gross, ".2f"))
    print("EPF (11%)     : RM", format(epf_amount, ".2f"))
    print("SOCSO (0.5%)  : RM", format(socso_amount, ".2f"))
    print("Reward        : RM", format(reward_amount, ".2f"))
    print("-----------------------------------------")
    print("Net Salary    : RM", format(net, ".2f"))