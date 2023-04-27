import pytest
from battlemaster.rules.tables.turn_phase import TurnPhase


def test_values():
    assert (TurnPhase.INITIATIVE.value == 0)
    assert (TurnPhase.MOVEMENT.value == 1)
    assert (TurnPhase.WEAPON_ATTACK.value == 2)
    assert (TurnPhase.PHYSICAL_ATTACK.value == 3)
    assert (TurnPhase.HEAT.value == 4)
    assert (TurnPhase.END.value == 5)
