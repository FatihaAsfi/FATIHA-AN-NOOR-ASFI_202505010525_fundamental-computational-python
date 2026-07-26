def display_ticket(ticket):
    print("\n========== IT HELPDESK TICKET ==========")
    print(f"Student Name : {ticket['student_name']}")
    print(f"Student ID   : {ticket['student_id']}")
    print(f"Issue        : {ticket['issue']}")
    print(f"Location     : {ticket['location']}")
    print(f"Priority     : {ticket['priority']}")
    print(f"Status       : {ticket['status']}")
    print("========================================")