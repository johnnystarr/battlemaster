import pytest
from battlemaster.rules.tables.hex_type import HexType


def test_values():
    assert (HexType.CLEAR.value == 0)
    assert (HexType.JUNGLE_LIGHT.value == 1)
    assert (HexType.JUNGLE_HEAVY.value == 2)
    assert (HexType.PAVEMENT.value == 3)
    assert (HexType.ROUGH.value == 4)
    assert (HexType.RUBBLE.value == 5)
    assert (HexType.SAND.value == 6)
    assert (HexType.WATER.value == 7)
    assert (HexType.WOODS_LIGHT.value == 8)
    assert (HexType.WOODS_HEAVY.value == 9)
