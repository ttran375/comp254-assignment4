import pytest
from positional_list import PositionalList

@pytest.fixture
def positional_list():
    pl = PositionalList()
    pl.add_last(10)
    pl.add_last(10)
    pl.add_last(20)
    pl.add_last(30)
    pl.add_last(40)
    pl.add_last(50)
    return pl

@pytest.mark.parametrize("element, expected_index", [
    (10, 0),    # First element
    (20, 2),    # Second element
    (30, 3),    # Middle element
    (50, 5),    # Last element
    (60, None), # Element not in list
])
def test_find_position(positional_list, element, expected_index):
    position = positional_list.find_position(element)
    if expected_index is None:
        assert position is None
    else:
        # Get the element at the expected index to compare positions
        cursor = positional_list.first()
        for _ in range(expected_index):
            cursor = positional_list.after(cursor)
        assert position == cursor

if __name__ == "__main__":
    pytest.main()
