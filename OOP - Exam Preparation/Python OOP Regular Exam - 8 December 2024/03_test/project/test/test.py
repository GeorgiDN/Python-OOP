from project.senior_student import SeniorStudent

from unittest import TestCase, main


class TestSeniorStudent(TestCase):
    def setUp(self):
        self.student = SeniorStudent("1234", "Go6o", 5.0)

    def test_init(self):
        self.assertIsInstance(self.student, SeniorStudent)
        self.assertEqual(self.student.student_id, "1234")
        self.assertEqual(self.student.name, "Go6o")
        self.assertEqual(self.student.student_gpa, 5.0)
        self.assertEqual(self.student.colleges, set())

    def test_invalid_student_id_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_id = ""
        message = "Student ID must be at least 4 digits long!"
        self.assertEqual(str(ve.exception), message)

    def test_invalid_student_id_with_string_with_spaces(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_id = "  "
        message = "Student ID must be at least 4 digits long!"
        self.assertEqual(str(ve.exception), message)

    def test_invalid_student_id_with_digits_less_than_4(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_id = "123"
        message = "Student ID must be at least 4 digits long!"
        self.assertEqual(str(ve.exception), message)

    def test_invalid_student_name_with_name_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.student.name = ""
        message = "Student name cannot be null or empty!"
        self.assertEqual(str(ve.exception), message)

    def test_invalid_student_name_with_name_with_spaces_only(self):
        with self.assertRaises(ValueError) as ve:
            self.student.name = "      "
        message = "Student name cannot be null or empty!"
        self.assertEqual(str(ve.exception), message)

    def test_invalid_student_gpa_with_negative_gpa(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_gpa = -1
        message = "Student GPA must be more than 1.0!"
        self.assertEqual(str(ve.exception), message)

    def test_invalid_student_gpa_with_zero_gpa(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_gpa = 0
        message = "Student GPA must be more than 1.0!"
        self.assertEqual(str(ve.exception), message)

    def test_invalid_student_gpa_with_one_gpa(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_gpa = 1
        message = "Student GPA must be more than 1.0!"
        self.assertEqual(str(ve.exception), message)

    def test_apply_to_college_failed(self):
        res = self.student.apply_to_college(10.0, "SoftUni")
        message = "Application failed!"
        self.assertEqual(res, message)

    def test_apply_to_college_successful_with_gpa_equal_to_gpa_required(self):
        res = self.student.apply_to_college(5.0, "SoftUni")
        message = f"Go6o successfully applied to SoftUni."
        self.assertEqual(res, message)
        self.assertEqual(self.student.colleges, {"SOFTUNI"})

    def test_apply_to_college_successful_with_gpa_greater_than_gpa_required(self):
        res = self.student.apply_to_college(2.0, "SoftUni")
        message = f"Go6o successfully applied to SoftUni."
        self.assertEqual(res, message)
        self.assertEqual(self.student.colleges, {"SOFTUNI"})

    def test_update_gpa_unsuccessful_with_gpa_zero(self):
        res = self.student.update_gpa(0.0)
        message = "The GPA has not been changed!"
        self.assertEqual(res, message)

    def test_update_gpa_unsuccessful_with_gpa_one(self):
        res = self.student.update_gpa(1.0)
        message = "The GPA has not been changed!"
        self.assertEqual(res, message)

    def test_update_gpa_successful(self):
        res = self.student.update_gpa(6.0)
        message = "Student GPA was successfully updated."
        self.assertEqual(res, message)
        self.assertEqual(self.student.student_gpa, 6.0)

    def test_equal_method_false_with_greater_student_gpa_than_other(self):
        self.student2 = SeniorStudent("5678", "Ivan", 6.0)
        res = self.student.__eq__(self.student2)
        self.assertFalse(res)

    def test_equal_method_false_with_less_student_gpa_than_other(self):
        self.student2 = SeniorStudent("5678", "Ivan", 4.0)
        res = self.student.__eq__(self.student2)
        self.assertFalse(res)

    def test_equal_method_true(self):
        self.student2 = SeniorStudent("5678", "Ivan", 5.0)
        res = self.student.__eq__(self.student2)
        self.assertTrue(res)
