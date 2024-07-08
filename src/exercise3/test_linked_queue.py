import pytest
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
        (["a", "b", "c"], ["d", "e", "f"], ["a", "b", "c", "d", "e", "f"]),
        ([1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]),
        ([True, False], [False, True], [True, False, False, True]),
        ([None, None], [None], [None, None, None]),
        (["apple"], ["banana", "cherry"], ["apple", "banana", "cherry"]),
        ([], ["single"], ["single"]),
        (["only"], [], ["only"]),
        ([1, 2], [3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3, 4, 5], [6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([complex(1, 1), complex(2, 2)], [complex(3, 3)], [complex(1, 1), complex(2, 2), complex(3, 3)]),
        ([1, "a"], [2, "b"], [1, "a", 2, "b"]),
        ([(1, 2), (3, 4)], [(5, 6)], [(1, 2), (3, 4), (5, 6)]),
        ([{"key": "value"}], [{"another_key": "another_value"}], [{"key": "value"}, {"another_key": "another_value"}]),
        ([set([1, 2])], [set([3, 4])], [set([1, 2]), set([3, 4])]),
        ([frozenset([1, 2])], [frozenset([3, 4])], [frozenset([1, 2]), frozenset([3, 4])]),
        ([1, 2, 3], ["a", "b", "c"], [1, 2, 3, "a", "b", "c"]),
        ([float(i) for i in range(10)], [float(i + 10) for i in range(10)], [float(i) for i in range(20)]),
        ([str(i) for i in range(10)], [str(i + 10) for i in range(10)], [str(i) for i in range(20)]),
        ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
        ([None] * 10, [None] * 10, [None] * 20),
        ([1, 2, 3, None], [4, None, 5], [1, 2, 3, None, 4, None, 5]),
        ([], [1], [1]),
        ([1], [], [1]),
        ([1, 2, 3], [4, None, 6], [1, 2, 3, 4, None, 6]),
        ([complex(1, 1), complex(2, 2)], [], [complex(1, 1), complex(2, 2)]),
        ([1.1, 2.2, 3.3], [], [1.1, 2.2, 3.3]),
        ([True, False], [], [True, False]),
        ([None], [], [None]),
        ([set([1, 2])], [], [set([1, 2])]),
        ([frozenset([1, 2])], [], [frozenset([1, 2])]),
        ([{"key": "value"}], [], [{"key": "value"}]),
        ([(1, 2)], [], [(1, 2)]),
        ([1, "a", 2, "b"], [], [1, "a", 2, "b"]),
        ([complex(1, 1), complex(2, 2)], [complex(3, 3), complex(4, 4)], [complex(1, 1), complex(2, 2), complex(3, 3), complex(4, 4)]),
        ([1, "a", 2, "b"], [3, "c", 4, "d"], [1, "a", 2, "b", 3, "c", 4, "d"]),
        ([(1, 2), (3, 4)], [(5, 6), (7, 8)], [(1, 2), (3, 4), (5, 6), (7, 8)]),
        ([{"key": "value"}], [{"another_key": "another_value"}], [{"key": "value"}, {"another_key": "another_value"}]),
        ([set([1, 2])], [set([3, 4])], [set([1, 2]), set([3, 4])]),
        ([frozenset([1, 2])], [frozenset([3, 4])], [frozenset([1, 2]), frozenset([3, 4])]),
        ([None], [None], [None, None]),
        ([1.1], [2.2], [1.1, 2.2]),
        ([True], [False], [True, False]),
        ([set([1])], [set([2])], [set([1]), set([2])]),
        ([frozenset([1])], [frozenset([2])], [frozenset([1]), frozenset([2])]),
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
