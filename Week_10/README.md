# Employee Salary Calculator

## Description
This is a Python program that calculates an employee's salary. The program is divided into multiple modules to make the code organized and easier to maintain.

## Features
- Enter employee information
- Calculate gross salary
- Calculate EPF deduction (11%)
- Calculate SOCSO deduction (0.5%)
- Calculate overtime pay (RM25 per hour)
- Give a RM500 reward to managers who have worked for more than 3 years
- Calculate net salary
- Display a salary report

## Project Structure
```
week_10/
│── main.py
│── employee.py
│── salary.py
│── report.py
│── README.md
```

## How to Run
1. Open the project folder.
2. Run `main.py`.
3. Enter the employee details.
4. The program will display the salary report.

## Formula Used
- Gross Salary = Basic Salary + Allowance + Overtime Pay
- Overtime Pay = Overtime Hours × RM25
- EPF = Gross Salary × 11%
- SOCSO = Gross Salary × 0.5%
- Reward = RM500 (Managers with more than 3 years of service)
- Net Salary = Gross Salary − EPF − SOCSO + Reward

