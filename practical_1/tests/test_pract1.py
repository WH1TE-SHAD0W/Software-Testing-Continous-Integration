from practical_1.pytest_pract1 import question1


def test_question1_good():
    assert question1(9) == 11, "Answer incorrect"


def test_question1_letter():
    assert question1("?") != 0, "Tried to use a non numeric"


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
