from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Gosho",
                               {"python": ["p1", "p2"]})

    def test_enroll_method_with_existing_course_add_course_and_return_message(self):
        res = self.student.enroll("python", ["p3", "p4"], "x")
        self.assertEqual("Course already added. Notes have been updated.", res)
        self.assertEqual(self.student.courses, {"python": ["p1", "p2", "p3", "p4"]})

    def test_enroll_method_with_not_existing_course_and_add_course_with_empty_add_course_notes(self):
        res = self.student.enroll("java", ["j1"], "")
        self.assertEqual("Course and course notes have been added.", res)
        self.assertEqual(self.student.courses,
                         {"python": ["p1", "p2"],
                          "java": ["j1"]})

    def test_enroll_method_with_not_existing_course_and_add_course_with_add_course_notes_equal_to_Y(self):
        res = self.student.enroll("java", ["j1"], "Y")
        self.assertEqual("Course and course notes have been added.", res)
        self.assertEqual(self.student.courses,
                         {"python": ["p1", "p2"],
                          "java": ["j1"]})

    def test_enroll_method_with_not_existing_course_and_add_course_with_empty_notes(self):
        res = self.student.enroll("java", ["j1"], "x")
        self.assertEqual("Course has been added.", res)
        self.assertEqual(self.student.courses,
                         {"python": ["p1", "p2"],
                          "java": []})

    def test_add_notes_with_not_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("java", ["j1"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_with_existing_course_return_message(self):
        res = self.student.add_notes("python", "p3")
        self.assertEqual("Notes have been updated", res)
        self.assertEqual(self.student.courses, {"python": ["p1", "p2", "p3"]})

    def test_leave_course_with_not_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_with_existing_course_return_message_and_remove_course(self):
        res = self.student.leave_course("python")
        self.assertEqual("Course has been removed", res)
        self.assertEqual(self.student.courses, {})


if __name__ == '__main__':
    main()
