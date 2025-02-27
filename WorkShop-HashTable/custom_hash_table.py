from copy import deepcopy


class HashTable:
    def __init__(self):
        self.__keys: list = [None, None, None, None]
        self.__values: list = [None, None, None, None]
        self.__length: int = 4

    @property
    def _count(self):
        return len([el for el in self.__keys if el is not None])

    def __len__(self):
        return self.__length

    def __getitem__(self, item):
        try:
            index = self.__keys.index(item)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key does not exist")

    def __setitem__(self, key, value):
        try:
            existing_value_index = self.__keys.index(key)
            self.__values[existing_value_index] = value
        except ValueError:
            if self._count == self.__length:
                # Resize
                self.__resize()

            index = self.__find_index(self.hash(key))
            self.__keys[index] = key
            self.__values[index] = value

    def hash(self, key: str) -> int:
        return sum([ord(el) for el in key]) % self.__length

    def __find_index(self, index):
        if index == self.__length:
            index = 0
        if self.__keys[index] is None:
            return index
        return self.__find_index(index + 1)

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__length
        self.__values = self.__values + [None] * self.__length
        self.__length *= 2

    def get(self, key, default_value=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default_value

    def sort_result(self):
        copy_keys = [el for el in self.__keys if el is not None]
        copy_values = [el for el in self.__values if el is not None]
        result = list(zip(copy_keys, copy_values))
        sorted_result = sorted(result, key=lambda x: x[0])

        table = HashTable()
        table._HashTable__keys = [t[0] for t in sorted_result]
        table._HashTable__values = [t[1] for t in sorted_result]
        table._HashTable__length = self.__length
        diff = self.__length - self._count
        table._HashTable__keys = table._HashTable__keys + [None] * diff
        table._HashTable__values = table._HashTable__values + [None] * diff

        return table

    def add(self, key, value):
        self.__setitem__(key, value)

    def __str__(self):
        result = [f"{self.__keys[index]}: {self.__values[index]}" for index in range(self.__length) if
                  self.__keys[index] is not None]
        return "{ " + ', '.join(result) + "}"


table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table["country"] = "BG"
table.add("number", "1")
table["city"] = "Sofia"

print(table)
print(table.sort_result())
print(table.get("name"))
print(table["age"])
print(len(table))
print(table._count)
print(table["number"])
