from receipt import calculate_total, print_receipt


def main():

    print("=== Cafe Billing System ===")

    customer = input("Enter customer name: ")

    coffee = int(input("Enter coffee quantity: "))
    tea = int(input("Enter tea quantity: "))
    sandwich = int(input("Enter sandwich quantity: "))

    total = calculate_total(coffee, tea, sandwich)

    print_receipt(customer, coffee, tea, sandwich, total)


if __name__ == "__main__":
    main()