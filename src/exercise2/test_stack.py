import pytest
from stack import Stack, remove_all_elements


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
def test_remove_all_elements(stack, elements):
    for element in elements:
        stack.push(element)

    remove_all_elements(stack)

    assert stack.is_empty()


if __name__ == "__main__":
    pytest.main()
