from project.gallery import Gallery
from unittest import TestCase, main


class TestGallery(TestCase):
    def setUp(self):
        self.gallery = Gallery("Gallery1", "Sofia", 100.0, True)

    def test_init(self):
        self.assertIsInstance(self.gallery, Gallery)
        self.assertEqual(self.gallery.gallery_name, "Gallery1")
        self.assertEqual(self.gallery.city, "Sofia")
        self.assertEqual(self.gallery.area_sq_m, 100.0)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual(self.gallery.exhibitions, {})

    def test_gallery_name_with_empty_space(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.gallery_name = ""
        message = "Gallery name can contain letters and digits only!"
        self.assertEqual(str(ve.exception), message)

    def test_gallery_name_with_empty_spaces(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.gallery_name = "  "
        message = "Gallery name can contain letters and digits only!"
        self.assertEqual(str(ve.exception), message)

    def test_gallery_name_with_special_characters(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.gallery_name = "Gallery123_"
        message = "Gallery name can contain letters and digits only!"
        self.assertEqual(str(ve.exception), message)

    def test_city_with_empty_space(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.city = ""
        message = "City name must start with a letter!"
        self.assertEqual(str(ve.exception), message)

    def test_city_start_with_no_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.city = "1Sofia"
        message = "City name must start with a letter!"
        self.assertEqual(str(ve.exception), message)

    def test_area_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.area_sq_m = -1
        message = "Gallery area must be a positive number!"
        self.assertEqual(str(ve.exception), message)

    def test_area_with_zero_value(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.area_sq_m = 0
        message = "Gallery area must be a positive number!"
        self.assertEqual(str(ve.exception), message)

    def test_add_exhibition_successful(self):
        result = self.gallery.add_exhibition("Exhibition1", 2000)
        message = 'Exhibition "Exhibition1" added for the year 2000.'
        self.assertEqual(result, message)
        self.assertEqual(self.gallery.exhibitions["Exhibition1"], 2000)

    def test_add_exhibition_with_existing_exhibition(self):
        self.gallery.add_exhibition("Exhibition1", 2000)
        result = self.gallery.add_exhibition("Exhibition1", 2000)
        message = 'Exhibition "Exhibition1" already exists.'
        self.assertEqual(result, message)
        self.assertEqual(self.gallery.exhibitions["Exhibition1"], 2000)

    def test_remove_exhibition_successful(self):
        self.gallery.add_exhibition("Exhibition1", 2000)
        self.assertEqual(self.gallery.exhibitions["Exhibition1"], 2000)
        result = self.gallery.remove_exhibition("Exhibition1")
        message = 'Exhibition "Exhibition1" removed.'
        self.assertEqual(result, message)
        self.assertEqual(self.gallery.exhibitions, {})

    def test_remove_exhibition_successful_with_multiply_exhibitions(self):
        self.gallery.add_exhibition("Exhibition1", 2000)
        self.gallery.add_exhibition("Exhibition2", 2001)
        self.assertEqual(self.gallery.exhibitions["Exhibition1"], 2000)
        self.assertEqual(self.gallery.exhibitions["Exhibition2"], 2001)
        result = self.gallery.remove_exhibition("Exhibition1")
        message = 'Exhibition "Exhibition1" removed.'
        self.assertEqual(result, message)
        self.assertEqual(self.gallery.exhibitions["Exhibition2"], 2001)

    def test_remove_exhibition_with_not_existing_exhibition(self):
        result = self.gallery.remove_exhibition("Exhibition1")
        message = 'Exhibition "Exhibition1" not found.'
        self.assertEqual(result, message)

    def test_list_exhibitions_with_open_to_public(self):
        self.gallery.add_exhibition("Exhibition1", 2000)
        self.gallery.add_exhibition("Exhibition2", 2001)
        result = self.gallery.list_exhibitions()
        message = 'Exhibition1: 2000\nExhibition2: 2001'
        self.assertEqual(result, message)

    def test_list_exhibitions_with_not_open_to_public(self):
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        message = f'Gallery {self.gallery.gallery_name} is currently closed for public! Check for updates later on.'
        self.assertEqual(result, message)
