import pytest
from battlemaster.rules.tables.movement_costs import movement_costs_table

@pytest.fixture()
def movement_costs():
    return movement_costs_table()


def test_movement_cost_values(movement_costs):
    assert movement_costs.get(0) == 0
