class Stack:
    def __init__(self):
        self._elements = []

    def size(self):
        return len(self._elements)

    def isEmpty(self):
        return len(self._elements) == 0

    def push(self, e):
        self._elements.append(e)

    def top(self):
        if self.isEmpty():
            raise IndexError("Top from an empty stack")
        return self._elements[-1]

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from an empty stack")
        return self._elements.pop()
