# import python
from invoice import *


def test_load_stock_check_size():
    """ Test the number of lines loaded is correct """
    data = load_stock('stock.txt')
    assert len(data) == 7


def test_load_stock_first_item():
    """ Checks details of the first loaded stock """
    data = load_stock('stock.txt')
    assert data[0] == ['pencil', 0.15]


def test_load_stock_last_item():
    """ Check last line if stock file loaded correctly """
    data = load_stock('stock.txt')
    assert data[6] == ['folder', 1.40]


def test_item_list_first():
    data = item_list(load_stock("stock.txt"))
    assert data[0] == '1 : pencil\n'


def test_item_list_last():
    data = item_list(load_stock("stock.txt"))
    assert data[6] == '7 : folder\n'


def test_get_item_name():
    data = load_stock("stock.txt")
    assert get_item_name(data, 0) == 'pencil'
    assert get_item_name(data, 6) == 'folder'


def test_get_item_number():
    data = load_stock("stock.txt")
    assert get_item_number(data, 'pencil') == 0


def test_get_price():
    data = load_stock("stock.txt")
    assert get_price(data, 0) == 0.15


def test_calculate_vat():
    assert calculate_vat(100) == 22


def test_calculate_discount_below():
    assert calculate_discount(20) == 0
    assert calculate_discount(5) == 0


def test_calculate_discount_over():
    data = 21
    assert calculate_discount(data) == 21 * 0.1


def test_create_invoice_data():
    data = load_stock("stock.txt")
    assert create_invoice_data(data, 0, 1) == [0.15, 0, 0.03, 0.18]


def test_get_user_input_below_out_of_range(monkeypatch):
    inputs = iter([1, 20])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    stock = load_stock("stock.txt")
    result = get_user_input(stock)
    assert result == (0, 20)

def test_say_hello(monkeypatch):
    inputs = iter(['Pavol', 'Kutaj'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = say_hello()
    assert result == "Hello Pavol Kutaj"

def say_hello():
    name = input("What is your first name?")
    name2 = input("What is your last name?")
    print("Hello " + name + " " + name2)
    return "Hello " + name + " " + name2


if __name__ == "__main__":
    say_hello()
