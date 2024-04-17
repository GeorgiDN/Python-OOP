from unittest import TestCase, main
from project.list_ import IntegerList


class IntegerListTest(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3)

    def test_initializing(self):
        self.integer_list = IntegerList(1, 2, "a", 3)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3])

    def test_initializing_with_no_arguments(self):
        self.integer_list = IntegerList()
        self.assertEqual([], self.integer_list.get_data())

    def test_initializing_with_strings_only(self):
        self.integer_list = IntegerList("b", "a")
        self.assertEqual(self.integer_list.get_data(), [])

    def test_add_method_with_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.add("a")
        expected_result = "Element is not Integer"
        self.assertEqual(expected_result, str(ex.exception))

    def test_add_method_with_float_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.add(1.2)
        expected_result = "Element is not Integer"
        self.assertEqual(expected_result, str(ex.exception))

    def test_add_method_with_integer_and_return_get_data(self):
        self.integer_list.add(4)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4])

    def test_remove_index_with_index_out_of_range_raise_exception(self):
        with self.assertRaises(IndexError) as idx_error:
            self.integer_list.remove_index(8)
        self.assertEqual("Index is out of range", str(idx_error.exception))

    def test_remove_index_with_valid_index(self):
        self.integer_list.remove_index(0)
        self.assertEqual([2, 3], self.integer_list.get_data())

    def test_get_method_with_index_out_of_range_raise_exception(self):
        with self.assertRaises(IndexError) as idx_error:
            self.integer_list.get(8)
        self.assertEqual("Index is out of range", str(idx_error.exception))

    def test_get_method_with_valid_index(self):
        self.integer_list.get(0)
        self.assertEqual(1, self.integer_list.get_data()[0])

    def test_insert_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as idx_error:
            self.integer_list.insert(8, 4)
        self.assertEqual("Index is out of range", str(idx_error.exception))

    def test_insert_with_not_type_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(0, "a")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_with_valid_type_and_index(self):
        self.integer_list.insert(0, 4)
        self.assertEqual([4, 1, 2, 3], self.integer_list.get_data())

    def test_get_biggest(self):
        result = self.integer_list.get_biggest()
        self.assertEqual(result, 3)

    def test_get_index(self):
        result = self.integer_list.get_index(1)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    main()
