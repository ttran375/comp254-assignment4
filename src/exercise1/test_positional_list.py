import pytest
from positional_list import (
    PositionalList,
)  # Assuming the PositionalList class is in a file named positional_list.py


@pytest.fixture
def setup_large_list():
    pl = PositionalList()
    positions = []
    elements = []
    for i in range(50):
        elem = i % 250  # This will create duplicates for elements 0-249
        pos = pl.add_last(elem)
        positions.append(pos)
        elements.append(elem)
    return pl, positions, elements


test_cases = [
    (i % 250, i) for i in range(50)
]  # Testing first occurrence of each element
test_cases += [(i, None) for i in range(50, 100)]  # Testing elements not in the list


@pytest.mark.parametrize("element, expected_position_index", test_cases)
def test_find_position(setup_large_list, element, expected_position_index):
    pl, positions, _ = setup_large_list
    position = pl.find_position(element)

    if expected_position_index is None:
        assert position is None
    else:
        assert position == positions[expected_position_index]
