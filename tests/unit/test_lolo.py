from calc import lolo


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
