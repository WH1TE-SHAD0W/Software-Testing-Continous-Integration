'''
INVOICE_CMD
Takes following parameters from the command line:
    - Item Name
    - Quantity
Returns invoice details
'''
import sys

from invoice import get_item_number, load_stock, generate_invoice

# CONSTANTS
STOCK_FILE = "stock.txt"

def convert_arguments(stock_data, item_name, quantity_string):
    '''
    Take the argument list and return the item number and quantity.
    Checks to see if item name exists and
    '''
    #
    # Check item name exists
    try:
        selected_item = get_item_number(stock_data, item_name)
    except ValueError as err:
        raise ValueError(f"Item {item_name} not found", err) from err

    # check quantity is a number
    try:
        quantity = int(quantity_string)
    except ValueError as err:
        raise ValueError("Quantity is not an integer", err) from err

    return selected_item, quantity


if __name__ == "__main__":

    stock_info  = load_stock(STOCK_FILE)
    sel_item, sel_quantity = convert_arguments(stock_info, sys.argv[1], sys.argv[2])

    print(''.join(generate_invoice(stock_info, sel_item, sel_quantity)))
