import pytest

from nonex import first, firstx


@pytest.mark.parametrize(
    ("value", "retval"),
    [
        [[1, 2, 3], 1],
        [[], None],
    ],
)
def test_first(value: list[str], retval: str | None) -> None:
    assert first(value) == retval


def test_first_filtered() -> None:
    assert first([1, 2, 3, 4], lambda x: x > 3) == 4
    assert first([1, 2, 3, 4], lambda x: x > 4) is None


def test_firstx() -> None:
    with pytest.raises(TypeError):
        firstx([])

    assert firstx([1, 2]) == 1
