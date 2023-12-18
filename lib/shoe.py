#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.repaired = False
        self.condition = None

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print(f"size must be an integer")
        else:
            self._size = value

    def repair(self):
        self.repaired = True

        print(f"The {self.brand} shoe has been repaired.")
        self.condtion = "New"

    def cobble(self):
        if self.repaired:
            print(f"The shoe needs repair before cobbling.")
        else:
            print(f"Your shoe is as good as new!")
            self.condition = "New"
