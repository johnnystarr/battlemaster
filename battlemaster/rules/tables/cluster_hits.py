"""
Cluster Hits Table
"""

from battlemaster.rules.tables.rules_table import RulesTable


def cluster_hits_table():
    """
    Global function to get the cluster hits table
    """
    table = RulesTable()
    a = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 12]
    b = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 18]
    c = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 13, 14, 15, 16, 16, 17, 17, 17, 18, 18, 24]
    d = [2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 20, 21, 21, 22, 23, 23, 24, 32]
    e = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40]
    table.insert(2, a)
    table.insert(3, a)
    table.insert(4, b)
    table.insert(5, c)
    table.insert(6, c)
    table.insert(7, c)
    table.insert(8, c)
    table.insert(9, d)
    table.insert(10, d)
    table.insert(11, e)
    table.insert(12, e)

    return table
