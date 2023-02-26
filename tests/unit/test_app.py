from calc.app import evaluate


def test_add_1_1():
    assert evaluate("1+1") == 2


def test_add_1_2():
    assert evaluate("1+2") == 3


def test_subtract_1_1():
    assert evaluate("1-1") == 0


def test_subtract_1_2():
    assert evaluate("1-2") == -1


def test_multiply_1_1():
    assert evaluate("1*1") == 1


def test_multiply_1_2():
    assert evaluate("1*2") == 2


def test_divide_1_1():
    assert evaluate("1/1") == 1


def test_divide_1_2():
    assert evaluate("1/2") == 0.5


def test_divide_2_1():
    assert evaluate("2/1") == 2


def test_divide_by_zero():
    assert evaluate("1/0") == "Divide by zero error"


def test_cos_0():
    assert evaluate("cos(0)") == 1


def test_cos_90():
    assert evaluate("cos(90)") == -0.4480736161291701


def test_cos_pi_times_1():
    assert evaluate("cos(pi) * 1") == -1


def test_sin_0():
    assert evaluate("sin(0)") == 0


def test_atan2_2_1():
    assert evaluate("atan2(2, 1)") == 1.1071487177940904


def test_pow_3_5():
    assert evaluate("pow(3, 5)") == 243


def test_abs_negative_2():
    assert evaluate("abs(-2)") == 2


def test_abs_2():
    assert evaluate("abs(2)") == 2


def test_expression_case1():
    assert evaluate("-(1 + 2) * 3") == -9
