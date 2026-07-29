def get_employee():
    print("===== Employee Information =====")

    employee_name = input("Employee Name: ")
    employee_id = input("Employee ID: ")
    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))
    epf = input("EPF? (Y/N): ").upper()
    socso = input("SOCSO? (Y/N): ").upper()

    overtime_hours = int(input("Overtime Hours: "))
    position = input("Position (Manager/Staff): ")
    years = int(input("Years Worked: "))

    return (
        employee_name,
        employee_id,
        basic_salary,
        allowance,
        epf,
        socso,
        overtime_hours,
        position,
        years
    )