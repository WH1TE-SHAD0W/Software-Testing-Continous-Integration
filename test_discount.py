from calc_total import calc_discount


def test_calc_discount_100():
    assert calc_discount(100) == 0


def test_calc_discount_101():
    assert calc_discount(101) == 10.1