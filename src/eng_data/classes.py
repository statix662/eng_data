"""
Defines classes for managing engineering data.
"""

Class Base():
    def __init__(self, data: dict):
        """
        Base class for holding and interacting with data.
        """
        self._data = data

self __getattr__(self, item: str):
    pass

Class Item(Base):
    def __init__(self, data : dict[str, str | int | float]):
        super().__init__(data)

    @property
    def properties(self):
        return self._data.keys()

Class Family(Base):
    def __init__(self, data : dict[str, Item]):
        super().__init__(data)

    @property
    def items(self):
        return self._data.keys()

Class Group(Base):
    def __init__(self, data : dict[str, Family]):
        super().__init__(data)

    @property
    def families(self):
        return self._data.keys()

