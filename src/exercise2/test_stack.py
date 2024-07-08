import pytest
from stack import Stack, removeAllElements


@pytest.fixture
def stack():
    return Stack()


@pytest.mark.parametrize(
    "elements",
    [
        ([]),  # Test with an empty stack
        ([1]),  # Test with a stack containing one element
        ([1, 2, 3, 4]),  # Test with a stack containing multiple elements
    ],
)
def test_removeAllElements(stack, elements):
    for element in elements:
        stack.push(element)

    removeAllElements(stack)

    assert stack.isEmpty()


if __name__ == "__main__":
    pytest.main()
