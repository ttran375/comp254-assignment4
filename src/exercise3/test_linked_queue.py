import pytest
from exceptions import Empty
from linked_queue import (
    LinkedQueue,
)  # Make sure to replace 'your_module' with the actual module name


@pytest.mark.parametrize(
    "Q1_elements, Q2_elements, expected_elements",
    [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [], []),
        ([1], [2], [1, 2]),
    ],
)
def test_concatenate(Q1_elements, Q2_elements, expected_elements):
    Q1 = LinkedQueue()
    Q2 = LinkedQueue()

    for elem in Q1_elements:
        Q1.enqueue(elem)

    for elem in Q2_elements:
        Q2.enqueue(elem)

    Q1.concatenate(Q2)

    result = []
    while not Q1.is_empty():
        result.append(Q1.dequeue())

    assert result == expected_elements
    assert Q2.is_empty()  # Q2 should be empty after concatenation


def test_concatenate_with_non_linkedqueue():
    Q1 = LinkedQueue()
    with pytest.raises(TypeError):
        Q1.concatenate([])  # This should raise a TypeError


def test_concatenate_with_empty_Q1():
    Q1 = LinkedQueue()
    Q2 = LinkedQueue()
    Q2.enqueue(1)
    Q2.enqueue(2)

    Q1.concatenate(Q2)

    result = []
    while not Q1.is_empty():
        result.append(Q1.dequeue())

    assert result == [1, 2]
    assert Q2.is_empty()  # Q2 should be empty after concatenation


def test_concatenate_with_empty_Q2():
    Q1 = LinkedQueue()
    Q1.enqueue(1)
    Q1.enqueue(2)

    Q2 = LinkedQueue()

    Q1.concatenate(Q2)

    result = []
    while not Q1.is_empty():
        result.append(Q1.dequeue())

    assert result == [1, 2]
    assert Q2.is_empty()  # Q2 should be empty after concatenation


def test_concatenate_both_empty():
    Q1 = LinkedQueue()
    Q2 = LinkedQueue()

    Q1.concatenate(Q2)

    assert Q1.is_empty()
    assert Q2.is_empty()


if __name__ == "__main__":
    pytest.main()
