# Computer Lab Access System

## Description
This project is a simple Python application that determines whether a student is allowed to enter a computer laboratory.

The system checks three conditions before granting access:
- Student is registered for today's lab session.
- Computer laboratory is currently open.
- A computer is available.

If all conditions are met, access is granted. Otherwise, access is denied with the appropriate reason.

---

## Project Structure

```
week_11/
│
├── main.py
├── student.py
├── access.py
├── display.py
└── README.md
```

---

## Modules

### student.py
Collects user input:
- Student Name
- Student ID
- Registration status
- Lab status
- Computer availability

### access.py
Contains two functions:
- `check_access()` – Determines whether access is granted or denied.
- `get_reason()` – Returns the reason for the decision.

### display.py
Displays the final access result including:
- Student Name
- Student ID
- Access Status
- Reason

### main.py
Coordinates all modules and runs the application.

---

## How to Run

1. Open a terminal.
2. Navigate to the project folder.
3. Run:

```bash
python main.py
```

---

## Sample Output

```
===== Computer Lab Access =====

Student Name : Fatiha
Student ID : 202505
Registered for today's lab? (Y/N): Y
Is the lab open? (Y/N): Y
Computer Available? (Y/N): Y

========== ACCESS RESULT ==========
Student Name : Fatiha
Student ID   : 202505
Status       : Access Granted
Reason       : Welcome to the lab
```

---

