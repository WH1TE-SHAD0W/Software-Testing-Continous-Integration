def calc_discount(amount):
    if amount > 100:
        return round(amount * 0.1, 2)
    return 0

if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    discount = calc_discount(amount)
    total = amount - discount
    print("Amount => ", amount)
    print("Discount => ", discount)
    print("Total => ", total)