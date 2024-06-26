class Equipment:
    equipment_id = 0

    def __init__(self, name: str):
        Equipment.equipment_id = Equipment.get_next_id()
        self.name = name
        self.id = Equipment.equipment_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.equipment_id + 1
