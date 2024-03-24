class Zoo:
    def __init__(self, name: int, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        searched_worker = next((w for w in self.workers if w.name == worker_name), None)
        if searched_worker is not None:
            self.workers.remove(searched_worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = sum(worker.salary for worker in self.workers)
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if type(animal).__name__ == "Lion":
                lions.append(animal)
            elif type(animal).__name__ == "Tiger":
                tigers.append(animal)
            elif type(animal).__name__ == "Cheetah":
                cheetahs.append(animal)

        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join(map(str, lions)) + '\n'
        result += f"----- {len(tigers)} Tigers:\n"
        result += '\n'.join(map(str, tigers)) + '\n'
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(map(str, cheetahs))

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if type(worker).__name__ == "Keeper":
                keepers.append(worker)
            elif type(worker).__name__ == "Caretaker":
                caretakers.append(worker)
            elif type(worker).__name__ == "Vet":
                vets.append(worker)

        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join(map(str, keepers)) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += '\n'.join(map(str, caretakers)) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += '\n'.join(map(str, vets))

        return result
