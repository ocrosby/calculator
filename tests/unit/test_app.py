import pytest

import math
import tkinter

from calc import app


class TestApplication:
    def test_add(self, application):
        # Arrange
        a = 2
        b = 3
        expected_result = 5

        # Act
        result = application.add(a, b)

        # Assert
        assert result == expected_result

    def test_subtract(self, application):
        # Arrange
        a = 2
        b = 3
        expected_result = -1

        # Act
        result = application.subtract(a, b)

        # Assert
        assert result == expected_result

    def test_multiply(self, application):
        # Arrange
        a = 2
        b = 3
        expected_result = 6

        # Act
        result = application.multiply(a, b)

        # Assert
        assert result == expected_result

    def test_divide(self, application):
        # Arrange
        a = 2
        b = 3
        expected_result = 0.6666666666666666

        # Act
        result = application.divide(a, b)

        # Assert
        assert result == expected_result

    def test_mod(self, application):
        # Arrange
        a = 2
        b = 3
        expected_result = 2

        # Act
        result = application.mod(a, b)

        # Assert
        assert result == expected_result

    def test_lcm(self, application):
        # Arrange
        a = 2
        b = 3
        expected_result = 6

        # Act
        result = application.lcm(a, b)

        # Assert
        assert result == expected_result

    def test_gcd(self, application):
        # Arrange
        a = 2
        b = 3
        expected_result = 1

        # Act
        result = application.gcd(a, b)

        # Assert
        assert result == expected_result


def test_configure_root(mocker):
    # Arrange
    mocked_root = mocker.Mock()

    mocked_title = mocker.patch.object(mocked_root, "title")
    mocked_config = mocker.patch.object(mocked_root, "config")
    mocked_geometry = mocker.patch.object(mocked_root, "geometry")

    # Act
    app.configure_root(mocked_root)

    # Assert
    mocked_title.assert_called_once_with('Scientific Calculator')
    mocked_config.assert_called_once_with(bg='gray')
    mocked_geometry.assert_called_once_with('870x550+50+50')

def test_create_button(mocker):
    # Arrange
    mocked_root = mocker.Mock()
    mocked_app = mocker.Mock()
    caption = "test"

    mocked_button = mocker.patch("calc.app.Button")

    # Act
    app.create_button(mocked_app, mocked_root, caption)

    # Assert
    mocked_button.assert_called_once()

class TestButtonClicked:
    def test_log_base_10(self, application, mocker):
        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value="2.3")
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked("log₁₀")

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, 0.36172783601759284)

    def test_sin_0(self, application, mocker):
        x_value = "0"
        expected_result = 0
        function_name = "sinθ"

        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value=x_value)
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked(function_name)

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, expected_result)

    def test_cos_0(self, application, mocker):
        x_value = "0"
        expected_result = 1
        function_name = "cosθ"

        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value=x_value)
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked(function_name)

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, expected_result)

    def test_radians_180_degrees(self, application, mocker):
        x_value = "180"
        expected_result = math.pi
        function_name = "rad"

        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value=x_value)
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked(function_name)

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, expected_result)

    def test_degrees_pi_radians(self, application, mocker):
        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value=str(math.pi))
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked('deg')

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, 180)

    def test_ce(self, application, mocker):
        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value='')
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked('CE')

        # Assert
        mocked_get.assert_called_once()
        assert mocked_delete.call_count == 2
        mocked_insert.assert_called_once_with(0, '')

    def test_c(self, application, mocker):
        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value='')
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked('C')

        # Assert
        mocked_get.assert_called_once()
        assert mocked_delete.call_count == 1
        mocked_insert.assert_called_once_with(0, '')

    def test_sqrt(self, application, mocker):
        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value='4')
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked('√')

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)
        mocked_insert.assert_called_once_with(0, 2)

    def test_tangent_of_pi(self, application, mocker):
        # Arrange
        mocked_get = mocker.patch.object(application.entry_box, "get", return_value=str(math.pi))
        mocked_delete = mocker.patch.object(application.entry_box, "delete")
        mocked_insert = mocker.patch.object(application.entry_box, "insert")

        # Act
        application.button_clicked('tanθ')

        # Assert
        mocked_get.assert_called_once()
        mocked_delete.assert_called_once_with(0, tkinter.END)

        result = mocked_insert.call_args[0][1]
        assert pytest.approx(result, 0.1) == 0.05

class TestEvaluate:
    def test_add_1_1(self, application):
        assert application.evaluate("1+1") == 2


    def test_add_1_2(self, application):
        assert application.evaluate("1+2") == 3


    def test_subtract_1_1(self, application):
        assert application.evaluate("1-1") == 0


    def test_subtract_1_2(self, application):
        assert application.evaluate("1-2") == -1


    def test_multiply_1_1(self, application):
        assert application.evaluate("1*1") == 1


    def test_multiply_1_2(self, application):
        assert application.evaluate("1*2") == 2


    def test_divide_1_1(self, application):
        assert application.evaluate("1/1") == 1


    def test_divide_1_2(self, application):
        assert application.evaluate("1/2") == 0.5


    def test_divide_2_1(self, application):
        assert application.evaluate("2/1") == 2


    def test_divide_by_zero(self, application):
        assert application.evaluate("1/0") == "Divide by zero error"


    def test_cos_0(self, application):
        assert application.evaluate("cos(0)") == 1


    def test_cos_90(self, application):
        assert application.evaluate("cos(90)") == -0.4480736161291701

    def test_ln_1(self, application):
        assert application.evaluate("ln(1)") == 0

    def test_cos_pi_times_1(self, application):
        assert application.evaluate("cos(pi) * 1") == -1

    def test_tan_pi(self, application):
        assert pytest.approx(application.evaluate("tan(pi)"), 0.000001) == 0

    def test_sqrt_4(self, application):
        assert application.evaluate("sqrt(4)") == 2

    def test_sin_0(self, application):
        assert application.evaluate("sin(0)") == 0


    def test_atan2_2_1(self, application):
        assert application.evaluate("atan2(2, 1)") == 1.1071487177940904


    def test_pow_3_5(self, application):
        assert application.evaluate("pow(3, 5)") == 243


    def test_abs_negative_2(self, application):
        assert application.evaluate("abs(-2)") == 2


    def test_abs_2(self, application):
        assert application.evaluate("abs(2)") == 2


    def test_expression_case1(self, application):
        assert application.evaluate("-(1 + 2) * 3") == -9
