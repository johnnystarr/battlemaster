"""
RulesTable Class
"""


class RulesTable:
    """
    Provides basic storage and retrieval for rules tables
    """

    def __init__(self):
        self.table = {}

    def insert(self, index, value):
        """
        insert()
        """
        self.table[index] = value

    def get(self, x, y=0):
        """
        get()
        """
        if self.table[x]:
            if isinstance(self.table[x], list):
                return self.table[x][y]
            return self.table[x]

        raise IndexError(f"{x} is not a valid index in this array.")

    def get_sub_table(self, x):
        """
        get_sub_table()
        """
        if self.table[x]:
            if isinstance(self.table[x], list):
                return self.table[x]

        raise IndexError(f"{x} is not a valid index in this array.")
