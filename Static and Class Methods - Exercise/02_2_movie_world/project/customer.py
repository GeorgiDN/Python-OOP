class Customer:
    CAPACITY = 10

    def __init__(self, name: str, age: int, _id: int):
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds: list = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} "
                f"has {len(self.rented_dvds)} rented DVD's ({', '.join(d.name for d in self.rented_dvds)})")
