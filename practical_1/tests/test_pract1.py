from practical_1.pytest_pract1 import question1, question2, question3, question4


def test_question1_good():
    assert question1(9) == 11, "Answer incorrect"


def test_question1_letter():
    assert question1("?") == -1, "Tried to use a non numeric"


def test_question1_float():
    assert question1(5.5) == 7.5, "tried floating point number"



def test_question2_99():
    assert question2(99) == 0, "tried 99 should be 0"


def test_question2_100():
    assert question2(100) == 0


def test_question2_101():
    assert question2(101) == '5.05', " tried 101 wee error"


def test_question2_999():
    assert question2(999) == '49.95'


def test_question2_1000():
    assert question2(1000) == '50';


def test_question2_1001():
    assert question2(1001) == '65.065'


def test_question3_win():
    assert question3(2, 0, 0) == 6


def test_question3_win_draw():
    assert question3(1, 3, 0) == 6


def test_question3_win_lost():
    assert question3(4, 0, 3) == 12


def test_question3_win_draw_lost():
    assert question3(2, 3, 1) == 9


def test_question3_draw():
    assert question3(0, 4, 0) == 4


def test_question3_draw_lost():
    assert question3(0, 6, 3) == 6


def test_question3_lost():
    assert question3(0, 0, 6) == 0


def test_question3_no_game():
    assert question3(0, 0, 0) == 0

def test_question3_wrong_input():
    assert question3("string", "string", "string") == "wrong input"
def test_question4_lt_0():
    assert question4(-500) == 0
def test_question4_lt_100():
    assert question4(10) == 0.3


def test_question4_e_100():
    assert question4(100) == 3


def test_question4_gt_100_lt_1000():
    assert question4(500) == 25


def test_question4_e_1000():
    assert question4(1000) == 70


def test_question4_gt_1000():
    assert question4(10000) == 700


def test_question4_wrong_input():
    assert question4("string") == "The input is wrong, please write a number!"
