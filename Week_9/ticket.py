def create_ticket():
    print("=== IT Helpdesk Ticket ===")

    student_name = input("Student Name: ")
    student_id = input("Student ID: ")
    issue = input("Issue: ")
    location = input("Location: ")
    priority = input("Priority (High/Medium/Low): ")

    status = "Pending"

    # Return all values
    return {
        "student_name": student_name,
        "student_id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "status": status
    }