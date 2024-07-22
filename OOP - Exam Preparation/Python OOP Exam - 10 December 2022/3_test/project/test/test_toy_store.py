from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.toystore = ToyStore()

    def test_init(self):
        shelf_check = {
            "A": None, "B": None, "C": None, "D": None,
            "E": None, "F": None, "G": None
        }
        self.assertEqual(self.toystore.toy_shelf, shelf_check)

    def test_add_toy_successfully(self):
        result = self.toystore.add_toy("A", "car")
        shelf_check = {
            "A": "car", "B": None, "C": None, "D": None,
            "E": None, "F": None, "G": None
        }
        message = f"Toy:car placed successfully!"
        self.assertEqual(result, message)
        self.assertEqual(self.toystore.toy_shelf["A"], "car")
        self.assertEqual(self.toystore.toy_shelf, shelf_check)

    def test_add_toy_shelf_does_not_exist_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("Q", "car")
        message = "Shelf doesn't exist!"
        self.assertEqual(message, str(ex.exception))

    def test_add_toy_with_toy_already_on_shelf_raise_exception(self):
        self.toystore.add_toy("A", "car")
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("A", "car")
        message = "Toy is already in shelf!"
        self.assertEqual(message, str(ex.exception))

    def test_add_toy_with_shelf_already_taken_raise_exception(self):
        self.toystore.add_toy("A", "car")
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("A", "motor")
        message = "Shelf is already taken!"
        self.assertEqual(message, str(ex.exception))

    def test_remove_toy_successfully(self):
        self.toystore.add_toy("A", "car")
        result = self.toystore.remove_toy("A", "car")
        message = f"Remove toy:car successfully!"
        self.assertEqual(result, message)
        shelf_check = {
            "A": None, "B": None, "C": None, "D": None,
            "E": None, "F": None, "G": None
        }
        self.assertEqual(self.toystore.toy_shelf["A"], None)
        self.assertEqual(self.toystore.toy_shelf, shelf_check)

    def test_remove_toy_with_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("Q", "car")
        message = "Shelf doesn't exist!"
        self.assertEqual(message, str(ex.exception))

    def test_remove_toy_toy_does_not_exist_on_the_shelf(self):
        self.toystore.add_toy("A", "car")
        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("A", "motor")
        message = "Toy in that shelf doesn't exists!"
        self.assertEqual(message, str(ex.exception))

    def test_add_toy_does_not_affect_other_shelves(self):
        self.toystore.add_toy("A", "car")
        shelf_check = {
            "A": "car", "B": None, "C": None, "D": None,
            "E": None, "F": None, "G": None
        }
        self.assertEqual(self.toystore.toy_shelf, shelf_check)

    def test_remove_toy_from_empty_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("A", "car")
        message = "Toy in that shelf doesn't exists!"
        self.assertEqual(message, str(ex.exception))

    def test_state_after_invalid_add_toy(self):
        try:
            self.toystore.add_toy("Q", "car")
        except Exception:
            pass
        shelf_check = {
            "A": None, "B": None, "C": None, "D": None,
            "E": None, "F": None, "G": None
        }
        self.assertEqual(self.toystore.toy_shelf, shelf_check)

    def test_state_after_invalid_remove_toy(self):
        self.toystore.add_toy("A", "car")
        try:
            self.toystore.remove_toy("A", "motor")
        except Exception:
            pass
        shelf_check = {
            "A": "car", "B": None, "C": None, "D": None,
            "E": None, "F": None, "G": None
        }
        self.assertEqual(self.toystore.toy_shelf, shelf_check)


if __name__ == '__main__':
    main()




# # 90/100
# from project.toy_store import ToyStore
# from unittest import TestCase, main
#
#
# class TestToyStore(TestCase):
#     def setUp(self):
#         self.toystore = ToyStore()
#         self.toystore.toy_shelf = {
#             "A": None, "B": None, "C": None, "D": None,
#             "E": None, "F": None, "G": None
#         }
#
#     def test_init(self):
#         shelf_check = {
#             "A": None, "B": None, "C": None, "D": None,
#             "E": None, "F": None, "G": None
#         }
#         self.assertEqual(self.toystore.toy_shelf, shelf_check)
#
#     def test_add_toy_successfully(self):
#         result = self.toystore.add_toy("A", "car")
#         shelf_check = {
#             "A": "car", "B": None, "C": None, "D": None,
#             "E": None, "F": None, "G": None
#         }
#         message = f"Toy:car placed successfully!"
#         self.assertEqual(result, message)
#         self.assertEqual(self.toystore.toy_shelf["A"], "car")
#         self.assertEqual(self.toystore.toy_shelf, shelf_check)
#
#     def test_add_toy_shelf_does_not_exist_raise_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.toystore.add_toy("Q", "car")
#         message = "Shelf doesn't exist!"
#         self.assertEqual(message, str(ex.exception))
#
#     def test_add_toy_with_toy_already_on_shelf_raise_exception(self):
#         self.toystore.add_toy("A", "car")
#         with self.assertRaises(Exception) as ex:
#             self.toystore.add_toy("A", "car")
#         message = "Toy is already in shelf!"
#         self.assertEqual(message, str(ex.exception))
#
#         shelf_check = {
#             "A": "car", "B": None, "C": None, "D": None,
#             "E": None, "F": None, "G": None
#         }
#         self.assertEqual(self.toystore.toy_shelf, shelf_check)
#
#     def test_add_toy_with_shelf_already_taken_raise_exception(self):
#         self.toystore.add_toy("A", "car")
#         with self.assertRaises(Exception) as ex:
#             self.toystore.add_toy("A", "motor")
#         message = "Shelf is already taken!"
#         self.assertEqual(message, str(ex.exception))
#
#         shelf_check = {
#             "A": "car", "B": None, "C": None, "D": None,
#             "E": None, "F": None, "G": None
#         }
#         self.assertEqual(self.toystore.toy_shelf, shelf_check)
#
#     def test_remove_toy_successfully(self):
#         self.toystore.add_toy("A", "car")
#         result = self.toystore.remove_toy("A", "car")
#         message = f"Remove toy:car successfully!"
#         self.assertEqual(result, message)
#         shelf_check = {
#             "A": None, "B": None, "C": None, "D": None,
#             "E": None, "F": None, "G": None
#         }
#         self.assertEqual(self.toystore.toy_shelf["A"], None)
#         self.assertEqual(self.toystore.toy_shelf, shelf_check)
#
#     def test_remove_toy_with_shelf_does_not_exist(self):
#         with self.assertRaises(Exception) as ex:
#             self.toystore.remove_toy("Q", "car")
#         message = "Shelf doesn't exist!"
#         self.assertEqual(message, str(ex.exception))
#
#     def test_remove_toy_toy_does_not_exist_on_the_shelf(self):
#         self.toystore.add_toy("A", "car")
#         with self.assertRaises(Exception) as ex:
#             self.toystore.remove_toy("A", "motor")
#         message = "Toy in that shelf doesn't exists!"
#         self.assertEqual(message, str(ex.exception))
#
#         shelf_check = {
#             "A": "car", "B": None, "C": None, "D": None,
#             "E": None, "F": None, "G": None
#         }
#         self.assertEqual(self.toystore.toy_shelf, shelf_check)
#
#
# if __name__ == '__main__':
#     main()

