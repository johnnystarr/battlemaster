import pytest
from battlemaster.rules.tables.rules_table import RulesTable


@pytest.fixture()
def table():
    return RulesTable()


def test_insert(table):
    table.insert(1, "a")
    table.insert(2, "b")
    table.insert(3, ["c"])


def test_get_one_dimensional(table):
    table.insert(1, 1)
    assert(table.get(1) == 1)


def test_get_two_dimensional(table):
    table.insert(1, [1, 2])
    # offset can be omitted because it is 0
    assert(table.get(1) == 1)
    # offset can be explicitly set to 0
    assert(table.get(1, offset=0) == 1)
    # offset for anything > 0 must be set
    assert(table.get(1, offset=1) == 2)

