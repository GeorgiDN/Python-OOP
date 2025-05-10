import unittest
from project.volcano import Volcano


class TestVolcano(unittest.TestCase):
    def setUp(self):
        self.volcano = Volcano('vulkan', 100)
        Volcano._unique_names.clear()

    def test_init(self):
        self.assertIsInstance(self.volcano, Volcano)
        self.assertEqual(self.volcano.name, 'VULKAN')
        self.assertEqual(self.volcano.height_m, 100)
        self.assertEqual(self.volcano.last_eruption, None)

    def test_valid_volcan_creation(self):
        v = Volcano("Vulkan", 100, 1999)
        self.assertEqual(v.name, "VULKAN")
        self.assertEqual(v.height_m, 100)
        self.assertEqual(v.last_eruption, 1999)
        self.assertFalse(v.is_active)

    def test_name_too_short_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            Volcano("V", 100)
        self.assertEqual(str(ve.exception), "Volcano name must be at least two characters long!")

    def test_name_uniqueness(self):
        Volcano("go6o", 100)
        with self.assertRaises(ValueError) as ve:
            Volcano("go6o", 100)
        self.assertEqual(str(ve.exception), "Volcano name must be unique!")

    def test_height_validation_with_zero_height_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            Volcano("go6o", 0)
        self.assertEqual(str(ve.exception), "Height must be a positive integer!")

    def test_height_validation_with_negative_height_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            Volcano("go6o", -1)
        self.assertEqual(str(ve.exception), "Height must be a positive integer!")

    def test_active_volcano_with_true(self):
        v = Volcano("activeVulkan", 100, 2001)
        self.assertTrue(v.is_active)

    def test_active_volcano_with_false(self):
        v = Volcano("notActiveVulkan", 100, 1999)
        self.assertFalse(v.is_active)

    def test_active_volcano_with_false_last_eruption_is_none(self):
        v = Volcano("notActiveVulkan", 100)
        self.assertFalse(v.is_active)

    def test_unique_volcano_count(self):
        Volcano("firstVulkan", 100)
        Volcano("secondVulcan", 101)
        self.assertEqual(Volcano.unique_volcano_count(), 2)


if __name__ == '__main__':
    unittest.main()
