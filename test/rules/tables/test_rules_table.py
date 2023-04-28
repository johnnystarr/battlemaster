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
    # y can be omitted because it is 0
    assert(table.get(1) == 1)
    # y can be explicitly set to 0
    assert(table.get(1, y=0) == 1)
    # y for anything > 0 must be set
    assert(table.get(1, y=1) == 2)


def test_get_sub_table(table):
    table.insert(1, [1, 2, 3])
    assert(table.get_sub_table(1) == [1, 2, 3])


def test_bad_indices(table):
    table.insert(0, 1)
    with pytest.raises(IndexError):
        table.get(1)
    with pytest.raises(IndexError):
        table.get_sub_table(1)
