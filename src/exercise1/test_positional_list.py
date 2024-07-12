import pytest
from positional_list import PositionalList


@pytest.fixture
def plist():
    pl = PositionalList()
    positions = []
    # Adding 50 elements to the PositionalList
    for i in range(1, 51):
        positions.append(pl.add_last(i * 10))
    return pl, positions


# Generate 100 test cases
params = []
for i in range(50):
    params.append((i, (i + 1) * 10, f"p{i + 1}"))
for i in range(50, 100):
    params.append((-1, (i + 1) * 10, None))


@pytest.mark.parametrize("index, element, position_str", params)
def test_index_of_and_find_position(plist, index, element, position_str):
    pl, positions = plist

    # Testing indexOf
    if position_str is not None:
        pos = positions[int(position_str[1:]) - 1]
        assert pl.index_of(pos) == index
    else:
        with pytest.raises(ValueError):
            pl.index_of(
                None
            )  # This will raise a ValueError as expected for position not found

    # Testing findPosition
    expected = None if position_str is None else positions[int(position_str[1:]) - 1]
    assert pl.find_position(element) == expected
