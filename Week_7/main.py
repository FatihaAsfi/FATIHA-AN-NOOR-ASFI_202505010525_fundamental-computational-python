from food_order import calculate_total

def main():
    price = float(input("Price(RM):"))
    quantity = int(input("Quality:"))

    total = calculate_total(price, quantity)

    print(f"Total PAyment = RM{total:.2f}")

    if __name__ == "_main_":
        main()