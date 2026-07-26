def calculate_total(coffee, tea, sandwich):
    total = (coffee * 8.50) + (tea * 6.00) + (sandwich * 12.00)
    return total


def print_receipt(customer, coffee, tea, sandwich, total):

    print("\n======= RECEIPT =======")
    print("Customer :", customer)
    print("Coffee quantity :", coffee)
    print("Tea quantity :", tea)
    print("Sandwich quantity :", sandwich)
    print("-----------------------")
    print("Total = RM {:.2f}".format(total))