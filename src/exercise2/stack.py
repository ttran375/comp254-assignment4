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


def removeAllElements(stack):
    """
    Recursively removes all elements from the given stack.
    """
    # Base case: if the stack is empty, return (stop recursion)
    if stack.isEmpty():
        return

    # Recursive case: pop an element and call removeAllElements again
    stack.pop()
    removeAllElements(stack)


def main():
    # Create a stack and push some elements
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print(
        "Stack before removing elements:",
        [stack._elements[i] for i in range(stack.size())],
    )

    # Remove all elements
    removeAllElements(stack)

    # Check if the stack is empty
    if stack.isEmpty():
        print("All elements removed. Stack is now empty.")
    else:
        print("Stack is not empty. Elements remain.")


if __name__ == "__main__":
    main()
