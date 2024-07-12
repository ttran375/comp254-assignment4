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

    def transfer(self, t):
        while not self.is_empty():
            element = self.pop()
            t.push(element)

    def remove_all(self):
        """
        Recursively removes all elements from the given stack.
        """
        if not self.is_empty():
            self.pop()
            self.remove_all()


# Function can be used in this exercise
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
    stack1 = Stack()
    stack2 = Stack()

    # Push elements into stack1
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print(f"Stack 1 before transfer: {stack1._elements}")
    print(f"Stack 2 before transfer: {stack2._elements}")

    # Transfer elements from stack1 to stack2
    stack1.transfer(stack2)
    print(f"Stack 1 after transfer: {stack1._elements}")
    print(f"Stack 2 after transfer: {stack2._elements}")

    # Remove all elements from stack2
    stack2.remove_all()
    print(f"Stack 2 after removing all elements: {stack2._elements}")


if __name__ == "__main__":
    main()
