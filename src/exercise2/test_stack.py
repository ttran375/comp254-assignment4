import sys
import pytest

from stack import Stack, remove_all_elements

sys.setrecursionlimit(5000)


@pytest.fixture
def stack():
    return Stack()


@pytest.mark.parametrize(
    "elements",
    [
        ([]),
        ([1]),
        ([1, 2, 3, 4]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ([1, 1, 1, 1, 1]),
        ([1, 2, 2, 3, 4, 4, 5]),
        ([-1, -2, -3, -4]),
        ([0, 0, 0, 0]),
        ([1, 1, 1, 1]),
        (list(range(50))),
        ([float(i) for i in range(10)]),
        (["a", "b", "c", "d"]),
        ([True, False, True]),
        ([None, None, None]),
        ([1.1, 2.2, 3.3, 4.4, 5.5]),
        ([complex(1, 1), complex(2, 2), complex(3, 3)]),
        ([1, "a", 2, "b"]),
        ([[], [], []]),
        ([{}, {}, {}]),
        ([set(), set(), set()]),
        ([frozenset(), frozenset(), frozenset()]),
        ([1, None, "a", 4.4]),
        ([i for i in range(100)]),
        ([i for i in range(1000)]),
        ([float(i) for i in range(100)]),
        (["a" * i for i in range(100)]),
        ([i for i in range(-50, 50)]),
        ([complex(i, i) for i in range(10)]),
        ([True, False] * 50),
        ([None] * 100),
        ([1, 2] * 50),
        (list(range(10)) * 10),
        ([i for i in range(-100, 100)]),
        ([complex(i, -i) for i in range(10)]),
        ([float(i) / 10 for i in range(10)]),
        ([1.1, "a", True, None, complex(1, 1)]),
        ([i**2 for i in range(50)]),
        ([str(i) for i in range(50)]),
        ([i for i in range(0, 100, 2)]),
        ([i for i in range(1, 100, 2)]),
        ([(i, i + 1) for i in range(50)]),
        ([{i: i + 1} for i in range(50)]),
        ([frozenset([i, i + 1]) for i in range(50)]),
        ([set([i, i + 1]) for i in range(50)]),
        ([i * 10 for i in range(50)]),
        ([i / 10 for i in range(50)]),
        ([(i, i + 1) for i in range(50)]),
        ([i for i in range(100, 50, -1)]),
        ([str(i) for i in range(100)]),
    ],
)
def test_remove_all_elements(stack, elements):
    for element in elements:
        stack.push(element)

    remove_all_elements(stack)

    assert stack.is_empty()


if __name__ == "__main__":
    pytest.main()
