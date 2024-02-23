def question1(x):
    # function to increment a number x by 2
    return x * 2


def question2(amount):
    # function to calculate interest
    # if amount is greater than 100 then interest rate is 5%
    # if amount is greater than 1000 then interest rate is 6%
    # otherwise interest rate is 0

    if amount < 100:
        return 0

    elif amount > 100:
        return "{:.2f}".format(amount * 0.05)

    elif amount > 1000:
        return "{:.3f}".format(amount * 0.065)

    return 0

def question3(win, draw, lost):
    # calculate the number of points a team has
    # 3 points for win
    # 1 point for draw
    # 0 point for lost

    points = win * 3 + draw * 1 + lost
    return points


def question4(deposit):
    # function to calculate interest
    # calculate the interest for a deposit value
    # if amount is up to 100 then interest rate is 3%
    # if amount is over 100 and up to 1000 is 5%
    # balances of 1000 and greater have a 7% interest rate

    if deposit < 100:
        return deposit * 0.03
    elif 100 < deposit < 1000:
        return deposit * 0.05
    elif deposit > 1000:
        return deposit * 0.07

    return 0
