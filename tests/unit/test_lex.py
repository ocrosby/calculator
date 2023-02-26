from calc import lex


def test_reader_empty():
    tape = lex.Reader()

    assert tape.is_empty()


def test_reader_not_empty():
    tape = lex.Reader("1")

    assert not tape.is_empty()
