from typing import Optional

class Volcano:
    _unique_names = set()

    def __init__(self, name: str, height_m: int, last_eruption: Optional[int] = None):
        self.name = name
        self.height_m = height_m
        self.last_eruption = last_eruption

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = value.strip().upper()
        if len(value) < 2:
            raise ValueError("Volcano name must be at least two characters long!")
        if value in Volcano._unique_names:
            raise ValueError("Volcano name must be unique!")
        self._name = value
        Volcano._unique_names.add(value)

    @property
    def height_m(self):
        return self._height_m

    @height_m.setter
    def height_m(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive integer!")
        self._height_m = value

    @property
    def is_active(self) -> bool:
        return self.last_eruption is not None and self.last_eruption >= 2000

    @classmethod
    def unique_volcano_count(cls) -> int:
        return len(cls._unique_names)
