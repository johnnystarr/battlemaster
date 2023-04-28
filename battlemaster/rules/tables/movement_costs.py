"""
Used to calculate the cost for moving.
"""

from battlemaster.rules.tables.rules_table import RulesTable


def movement_costs_table():
    """
    Build the table
    """
    table = RulesTable()
    table.insert(0, 0)

    return table
