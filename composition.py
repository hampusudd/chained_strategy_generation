class Composition:
    def __init__(self, characters):
        self._n = None
        self._characters = characters

    def get_characters(self):
        return self._characters

    def __len__(self):
        return len(self._characters)

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n < len(self._characters):
            result = self._characters[self._n]
            self._n += 1
            return result
        else:
            raise StopIteration

    def __repr__(self):
        return str(list((map(lambda x: x.name[0], self._characters))))
