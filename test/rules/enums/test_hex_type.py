import pytest
from battlemaster.rules.enums.hex_type import HexType


def test_values():
    assert (HexType.CLEAR.value == 0)
    assert (HexType.JUNGLE_LIGHT.value == 1)
    assert (HexType.JUNGLE_HEAVY.value == 2)
    assert (HexType.PAVEMENT.value == 3)
    assert (HexType.ROUGH.value == 4)
    assert (HexType.RUBBLE.value == 5)
    assert (HexType.SAND.value == 6)
    assert (HexType.WOODS_LIGHT.value == 7)
    assert (HexType.WOODS_HEAVY.value == 8)
    assert (HexType.WATER_DEPTH_1.value == 9)
    assert (HexType.WATER_DEPTH_2.value == 10)
    assert (HexType.WATER_DEPTH_3.value == 11)
    assert (HexType.LIGHT_BUILDING.value == 12)
    assert (HexType.MEDIUM_BUILDING.value == 13)
    assert (HexType.HEAVY_BUILDING.value == 14)
    assert (HexType.HARDENED_BUILDING.value == 15)
