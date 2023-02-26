class State:
    found: bool
    more: bool

    def __init__(self):
        self.more = False
        self.found = False

    def set(self, found: bool, more: bool = False) -> "State":
        self.found = found
        self.more = more

        return self

    @staticmethod
    def create(more: bool = False, found: bool = False) -> "State":
        return State().set(more=more, found=found)

    def __str__(self) -> str:
        return f"State(more={self.more}, found={self.found})"


class Scan:
    """Scan is the abstract base class for all recognizers.  If scan() is sent to a Scanner,
    it selects the winning recognizer from it's table and pushes characters from Input to
    this Scan by calling nextChar().  The resulting Scan.State reflects in a boolean value
    found, if this character could complete a symbol and in a boolean value more, if more
    characters can be added to the symbol.  Scanner uses Scan.state to mark the Input and
    terminate pushing characters.
    """

    state_object: State

    def __init__(self):
        self.state_object = State()

    def reset(self):
        self.state_object.set(more=False, found=False)


class Set(Scan):
    """Set objects recognize a single character that does or does not belong to a set."""

    set: str
    inside: bool

    def __init__(self, _set: str, inside: bool = False):
        super().__init__()

        self.set = _set
        self.inside = inside

    def reset(self):
        super().reset()

    def next_char(self, char: str) -> State:
        location = self.set.find(char)

        if self.inside:
            found = location >= 0
        else:
            found = location < 0

        more = False

        self.state_object.set(found=found, more=more)

        return self.state_object


class Char(Set):
    """Char is a Scan that recognizes a single character.
    If the char is empty it should match any character."""

    def __init__(self, _set: str = "", inside: bool = True):
        super().__init__(_set=_set, inside=inside)


class SetMN(Set):
    """
    SetMN is a Scan that recognizes between m and n characters which do or do
    not belong to a set.
    """

    m: int
    n: int
    jog: int

    def __init__(self, _set: str, inside: bool, m: int, n: int):
        super().__init__(_set, inside)

        self.jog = 0
        self.m = m
        self.n = n

    def reset(self):
        super().reset()

        self.jog = 0

    def next_char(self, char: str) -> State:
        self.jog += 1

        position = self.set.find(char)
        char_found = position >= 0

        if char_found:
            self.state_object.more = self.jog < self.n
            self.state_object.found = self.jog >= self.m
        else:
            self.state_object.more = False
            self.state_object.found = False

        return self.state_object

class Int(SetMN):
    """Int is a Scan that recognizes an integer."""

    def __init__(self, max_digits: int):
        super().__init__(_set="0123456789", inside=True, m=1, n=max_digits)


class Word(Scan):
    """Word is a Scan that recognizes a word."""

    word: str
    index: int

    def __init__(self, word: str):
        super().__init__()

        self.word = word
        self.index = 0

    def reset(self):
        super().reset()

        self.index = 0

    def next_char(self, char: str) -> State:
        current_char = self.word[self.index]
        self.index += 1

        if current_char == char:
            self.state_object.more = self.index < len(self.word)
            self.state_object.found = self.index == len(self.word)
        else:
            self.state_object.more = False
            self.state_object.found = False

        return self.state_object
