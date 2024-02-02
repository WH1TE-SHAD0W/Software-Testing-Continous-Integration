"""
INVOICE MODULE
This module contains a set of functions to capture and calculate invoice data.
Stock data is loaded form the stock.txt file, which contains: item name, price
and quantity in stock.
A main program tests this on the command line.
"""

# constants
VAT_RATE = 0.22
DISCOUNT = 0.1
DISCOUNT_THRESHOLD = 20


def load_stock(stock_file):
    '''
    Load data from stock file into data list.
    Each line of the file holds name and price
    This information is loaded into a list which holds a list of id, name and price for each item.
    data = [ [id, name, price], ... ]
    '''
    data = []
    with open(stock_file, encoding="utf-8") as file:
        for line in file:
            line = line.split(',')
            data.append([line[0].strip(), float(line[1].strip())])
    return data


def item_list(stock_data):
    '''
    This prints out the list of items, prefixed with each item id
    The item id can be used to select the required item
    '''
    formatted_item_list = []
    for idx, item in enumerate(stock_data):
        formatted_item_list.append(f"{idx + 1} : {item[0]}\n")
    return formatted_item_list


def get_item_name(stock_data, selected_item):
    '''
    Returns the item name from the stock data structure for the selected line.
    '''
    return stock_data[selected_item][0]


def get_item_number(stock_data, item_name):
    '''
    Returns item number given item name.
    Raises valueError exception if not found
    '''
    return [x[0] for x in stock_data].index(item_name)


def get_price(stock_data, selected_item):
    '''
    Returns the price for the given item from the stock data structure.
    '''
    price = stock_data[selected_item][1]
    return price


def calculate_vat(amount):
    '''
    Calculates the VAT to be paid on an amount.
    '''
    return amount * VAT_RATE


def calculate_discount(amount):
    '''
    Calculates the amount of discount to apply.
    Amount over discount threshold has the discount amount applied
    '''
    if amount > DISCOUNT_THRESHOLD:
        return amount * DISCOUNT
    return 0


def create_invoice_data(stock_data, selected_item, quantity):
    '''
    Produce all the calculated values using the above functions.
    Returns the multiple calculated values in a list, rounded to 2dp
    '''
    price = get_price(stock_data, selected_item)
    total_before_discount = price * quantity
    dis = calculate_discount(total_before_discount)
    total_gross = total_before_discount - dis
    vat = calculate_vat(total_gross)
    total_net = total_gross + vat
    return [round(total_before_discount, 2),
            round(dis, 2),
            round(vat, 2),
            round(total_net, 2)]


def get_user_input(stock_data):
    '''
    Reads user input and checks values
    '''
    print(''.join(item_list(stock_data)))
    in_range = False
    while not in_range:
        user_selected_item = input("Enter Item:")
        if user_selected_item.isdigit() is False:
            print("Selection must be a number")
        elif int(user_selected_item) < 0 or int(user_selected_item) >= len(stock_data):
            print("Selected value out of range")
        else:
            in_range = True

    in_range = False
    while not in_range:
        selected_quantity = input("Enter Amount:")
        if selected_quantity.isdigit():
            in_range = True
        else:
            print("Quantity must be a number")

    return int(user_selected_item) - 1, int(selected_quantity)


# pylint: disable=R0913
def format_invoice(item_name, item_price, quantity,
                   total_before_discount, discount, vat, total_net):
    '''
    Print out the invoice on the console given stock, selected item and quantity
    '''
    invoice = []
    invoice.append("             INVOICE\n")
    invoice.append("=================================\n")
    invoice.append(f"Item:\t\t|  {item_name}\n")
    invoice.append(f"Item Price:\t|  {item_price}\n")
    invoice.append(f"Quantity:\t|  {quantity}\n")
    invoice.append(f"Total:\t\t|  {total_before_discount}\n")
    invoice.append(f"Discount:\t|  {discount}\n")
    invoice.append(f"VAT:\t\t|  {vat}\n")
    invoice.append(f"Net Total:\t|  {total_net}\n")
    return invoice


def generate_invoice(stock_data, selected_item, quantity):
    '''
    Calculate invoice values an format an output (list of strings)
    '''
    calculated_invoice_values = create_invoice_data(stock_data, selected_item, quantity)
    item_name = get_item_name(stock_data, selected_item)
    item_price = get_price(stock_data, selected_item)
    return format_invoice(item_name, item_price, quantity, *calculated_invoice_values)


# Main program asks user to select item and quantity and prints the invoice
# Only runs if this file is the first to be loaded ("__main__").
# This means the code will not be run when the file is imported into the test scripts.

if __name__ == "__main__":
    stock = load_stock("stock.txt")
    sel_item, sel_quantity = get_user_input(load_stock("stock.txt"))
    print()
    print(''.join(generate_invoice(stock, sel_item, sel_quantity)))
    # print(load_stock("stock.txt"))
    # print(item_list(load_stock("stock.txt")))
    # print(''.join(item_list(load_stock("stock.txt"))))
    # print(get_item_number(load_stock("stock.txt"), "folder"))
    print(get_user_input(stock))