from calc import lolo

class TestState:
    def test_false_false(self):
        # Arrange
        state = lolo.State.create(False, False)

        # Act
        state_string = str(state)

        # Assert
        assert state_string == "State(more=False, found=False)"

    def test_true_true(self):
        # Arrange
        state = lolo.State.create(True, True)

        # Act
        state_string = str(state)

        # Assert
        assert state_string == "State(more=True, found=True)"

    def test_false_true(self):
        # Arrange
        state = lolo.State.create(False, True)

        # Act
        state_string = str(state)

        # Assert
        assert state_string == "State(more=False, found=True)"

    def test_true_false(self):
        # Arrange
        state = lolo.State.create(True, False)

        # Act
        state_string = str(state)

        # Assert
        assert state_string == "State(more=True, found=False)"

class TestWord:
    def test_case1(self):
        # Arrange
        test_word = lolo.Word("abc")

        # Act
        state = test_word.next_char("a")

        # Assert
        assert state.more == True
        assert state.found == False

    def test_case2(self):
        # Arrange
        test_word = lolo.Word("abc")

        # Act
        state = test_word.next_char("a")
        state = test_word.next_char("b")

        # Assert
        assert state.more == True
        assert state.found == False

    def test_case3(self):
        # Arrange
        test_word = lolo.Word("abc")

        # Act
        state = test_word.next_char("a")
        state = test_word.next_char("b")
        state = test_word.next_char("c")

        # Assert
        assert state.more == False
        assert state.found == True

class TestSet:
    def test_next_char_contained(self):
        # Arrange
        test_set = lolo.Set("abc", True)

        # Act
        state = test_set.next_char("a")

        # Assert
        assert test_set.state_object.more == False
        assert test_set.state_object.found == True

        assert state.more == False
        assert state.found == True

    def test_next_char_not_contained(self):
        # Arrange
        test_set = lolo.Set("abc", True)

        # Act
        state = test_set.next_char("d")

        # Assert
        assert test_set.state_object.more == False
        assert test_set.state_object.found == False

        assert state.more == False
        assert state.found == False


class TestChar:
    def test_next_char_any(self):
        # Arrange
        test_char = lolo.Char("", False)

        # Act
        state = test_char.next_char("a")

        # Assert
        assert test_char.state_object.more == False
        assert test_char.state_object.found == True

        assert state.more == False
        assert state.found == True

    def test_next_char_specific_match(self):
        # Arrange
        test_char = lolo.Char("a", True)

        # Act
        state = test_char.next_char("a")

        # Assert
        assert test_char.state_object.more == False
        assert test_char.state_object.found == True

        assert state.more == False
        assert state.found == True

    def test_next_char_specific_no_match(self):
        # Arrange
        test_char = lolo.Char("a")

        # Act
        state = test_char.next_char("b")

        # Assert
        assert test_char.state_object.more == False
        assert test_char.state_object.found == False

        assert state.more == False
        assert state.found == False
