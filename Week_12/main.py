def check_computers():
    computers = []  # first value

    # iterate and check for 5 computers
    for i in range(5):

        # A - Available, U - Used, M - Maintenance
        status = input( f"Computer {i + 1} status (A/U/M): " ).upper()

        computers.append(status)

    return computers


def count_available(computers):
    available = 0 

    for i in computers:
        if i == "A":
            available += 1

    return available


def display_status(computers, available):
    print("\n========== LAB STATUS ==========")

    for number in range(len(computers)):
        print(f"Computer {number + 1} status (A/U/M): {computers[number]}")

    print("-------------------------------")
    print(f"Available Computers: {available}")
    print("===============================")


# Main program starts from here
while True:

    computers = check_computers()

    available = count_available(computers)

    display_status(computers, available)

    choice = input("\nPerform another monitoring cycle? (Y/N): ").upper()

    if choice != "Y":
        break