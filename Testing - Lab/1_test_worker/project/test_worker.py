from project.worker import Worker

from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Gosho", 1000, 100)

    def test_01_initialization(self):
        self.assertEqual("Gosho", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_02_work_with_zero_energy_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_03_work_with_negative_energy_raise_exception(self):
        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_04_work_with_energy_greater_than_zero_increase_salary_reduce_energy(self):
        expected_energy = 99
        expected_money = self.worker.salary

        self.worker.work()
        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_05_rest_method(self):
        expected_energy = 101
        self.worker.rest()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_06_get_info(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.',
                         self.worker.get_info())


if __name__ == "__main__":
    main()
