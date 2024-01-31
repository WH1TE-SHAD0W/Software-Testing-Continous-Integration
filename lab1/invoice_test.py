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

def test_get_item():
    data = load_stock("stock.txt")
    assert get_item_number(data, 'pencil') == 0