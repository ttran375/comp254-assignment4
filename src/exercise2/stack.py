class Stack:
    def __init__(self):
        self._elements = []

    def size(self):
        return len(self._elements)

    def is_empty(self):
        return len(self._elements) == 0

    def push(self, e):
        self._elements.append(e)

    def top(self):
        if self.is_empty():
            raise IndexError("Top from an empty stack")
        return self._elements[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self._elements.pop()


def remove_all_elements(stack):
    """
    Recursively removes all elements from the given stack.
    """
    # Base case: if the stack is empty, return (stop recursion)
    if stack.is_empty():
        return

    # Recursive case: pop an element and call remove_all_elements again
    stack.pop()
    remove_all_elements(stack)


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
    remove_all_elements(stack)

    # Check if the stack is empty
    if stack.is_empty():
        print("All elements removed. Stack is now empty.")
    else:
        print("Stack is not empty. Elements remain.")


if __name__ == "__main__":
    main()
