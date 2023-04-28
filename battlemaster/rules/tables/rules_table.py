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

    def get(self, index, offset=0):
        """
        get()
        """
        if self.table[index]:
            if isinstance(self.table[index], list):
                return self.table[index][offset]
            return self.table[index]

        raise IndexError(f"{index} is not a valid index in this array.")
