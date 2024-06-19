class JsonNodeIterator:
    def __init__(self, root):
        self._root = root
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._root._children):
            raise StopIteration
        self._idx += 1
        return self._root._children[self._idx-1]