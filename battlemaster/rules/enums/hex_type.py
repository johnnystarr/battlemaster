"""
HexTypes
"""
from enum import Enum


class HexType(Enum):
    """
    HexTypes for game board
    """
    CLEAR = 0
    JUNGLE_LIGHT = 1
    JUNGLE_HEAVY = 2
    PAVEMENT = 3
    ROUGH = 4
    RUBBLE = 5
    SAND = 6
    WOODS_LIGHT = 7
    WOODS_HEAVY = 8
    WATER_DEPTH_1 = 9
    WATER_DEPTH_2 = 10
    WATER_DEPTH_3 = 11
    LIGHT_BUILDING = 12
    MEDIUM_BUILDING = 13
    HEAVY_BUILDING = 14
    HARDENED_BUILDING = 15
