import math
import tkinter

from calc import app
from calc.app import evaluate, button_clicked


class TestButtonClicked:
    def test_log_base_10(self, mocker):
        # Arrange
        mocked_get = mocker.patch.object(app.entryBox, "get", return_value="2.3")
        mocked_delete = mocker.patch.object(app.entryBox, "delete")
        mocked_insert = mocker.patch.object(app.entryBox, "insert")

        # Act
        app.button_clicked("log₁₀")

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, 0.36172783601759284)

    def test_sin_0(self, mocker):
        x_value = "0"
        expected_result = 0
        function_name = "sinθ"

        # Arrange
        mocked_get = mocker.patch.object(app.entryBox, "get", return_value=x_value)
        mocked_delete = mocker.patch.object(app.entryBox, "delete")
        mocked_insert = mocker.patch.object(app.entryBox, "insert")

        # Act
        app.button_clicked(function_name)

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, expected_result)

    def test_cos_0(self, mocker):
        x_value = "0"
        expected_result = 1
        function_name = "cosθ"

        # Arrange
        mocked_get = mocker.patch.object(app.entryBox, "get", return_value=x_value)
        mocked_delete = mocker.patch.object(app.entryBox, "delete")
        mocked_insert = mocker.patch.object(app.entryBox, "insert")

        # Act
        app.button_clicked(function_name)

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, expected_result)

    def test_radians_180_degrees(self, mocker):
        x_value = "180"
        expected_result = math.pi
        function_name = "rad"

        # Arrange
        mocked_get = mocker.patch.object(app.entryBox, "get", return_value=x_value)
        mocked_delete = mocker.patch.object(app.entryBox, "delete")
        mocked_insert = mocker.patch.object(app.entryBox, "insert")

        # Act
        app.button_clicked(function_name)

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, expected_result)

    def test_degrees_pi_radians(self, mocker):
        x_value = str(math.pi)
        expected_result = 180
        function_name = "deg"

        # Arrange
        mocked_get = mocker.patch.object(app.entryBox, "get", return_value=x_value)
        mocked_delete = mocker.patch.object(app.entryBox, "delete")
        mocked_insert = mocker.patch.object(app.entryBox, "insert")

        # Act
        app.button_clicked(function_name)

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, expected_result)

    def test_CE(self, mocker):
        expected_result = ''
        function_name = "CE"

        # Arrange
        mocked_get = mocker.patch.object(app.entryBox, "get", return_value=None)
        mocked_delete = mocker.patch.object(app.entryBox, "delete")
        mocked_insert = mocker.patch.object(app.entryBox, "insert")

        # Act
        app.button_clicked(function_name)

        # Assert
        mocked_get.assert_called_once()
        assert mocked_delete.call_count == 2
        mocked_insert.assert_called_once_with(0, expected_result)

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
