from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_init(self):
        self.assertIsInstance(self.plantation, Plantation)
        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers,  [])

    def test_size_with_negative_value_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        message = "Size must be positive number!"
        self.assertEqual(str(ve.exception), message)

    def test_hire_workers(self):
        res = self.plantation.hire_worker("Gosho")
        message = "Gosho successfully hired."
        self.assertEqual(res, message)
        self.assertEqual(self.plantation.workers, ["Gosho"])

    def test_hire_worker_with_existing_name(self):
        self.plantation.hire_worker("Gosho")
        self.plantation.hire_worker("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Gosho")
        message = "Worker already hired!"
        self.assertEqual(str(ve.exception), message)
        self.assertEqual(self.plantation.workers, ["Gosho", "Ivan"])

    def test_len_method_with_not_added_plants(self):
        res = self.plantation.__len__()
        self.assertEqual(res, 0)

    def test_planting_first(self):
        self.plantation.hire_worker("Gosho")
        self.plantation.hire_worker("Ivan")
        self.assertEqual(self.plantation.workers, ["Gosho", "Ivan"])
        res = self.plantation.planting("Gosho", "plant")
        message = "Gosho planted it's first plant."
        self.assertEqual(res, message)
        self.assertEqual(self.plantation.plants, {"Gosho": ["plant"]})

    def test_planting_with_full_plantation(self):
        self.plantation.size = 2
        self.plantation.hire_worker("Gosho")
        self.plantation.hire_worker("Ivan")
        self.assertEqual(self.plantation.workers, ["Gosho", "Ivan"])
        self.plantation.planting("Gosho", "plant")
        self.plantation.planting("Gosho", "plant2")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "plant3")
        message = "The plantation is full!"
        self.assertEqual(str(ve.exception), message)
        self.assertEqual(self.plantation.plants, {"Gosho": ["plant", "plant2"]})

    def test_planting_with_existing_plants(self):
        self.plantation.hire_worker("Gosho")
        self.plantation.hire_worker("Ivan")
        self.assertEqual(self.plantation.workers, ["Gosho", "Ivan"])

        self.plantation.planting("Gosho", "plant")
        self.plantation.planting("Gosho", "plant2")
        res = self.plantation.planting("Gosho", "plant3")
        message = "Gosho planted plant3."
        self.assertEqual(res, message)
        self.assertEqual(self.plantation.plants, {"Gosho": ["plant", "plant2", "plant3"]})

    def test_planting_with_not_existing_worker_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "plan1")
        message = "Worker with name Gosho is not hired!"
        self.assertEqual(str(ve.exception), message)

    def test_len_method_with_added_plants(self):
        self.plantation.hire_worker("Gosho")
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Gosho", "plant")
        self.plantation.planting("Gosho", "plant2")
        self.plantation.planting("Ivan", "plant3")

        res = self.plantation.__len__()
        self.assertEqual(res, 3)
        self.assertEqual(self.plantation.plants, {
            "Gosho": ["plant", "plant2"],
            "Ivan": ["plant3"]})

    def test_str_method(self):
        self.plantation.hire_worker("Gosho")
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Gosho", "plant")
        self.plantation.planting("Gosho", "plant2")
        self.plantation.planting("Ivan", "plant3")

        res = self.plantation.__str__()
        actual = (f"Plantation size: {self.plantation.size}\n"
                  f"Gosho, Ivan\n"
                  f"Gosho planted: plant, plant2\n"
                  f"Ivan planted: plant3")

        self.assertEqual(res, actual)

    def test_repr(self):
        self.plantation.hire_worker("Gosho")
        self.plantation.hire_worker("Ivan")
        res = self.plantation.__repr__()
        actual = (f"Size: {self.plantation.size}\n"
                  f"Workers: Gosho, Ivan")
        self.assertEqual(res, actual)


if __name__ == '__main__':
    main()

