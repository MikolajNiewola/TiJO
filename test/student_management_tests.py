import unittest
from src.student_management import StudentManagement


class StudentManagementTestCase(unittest.TestCase):
    def test_add_student_should_add_student(self):
        # given
        student_management = StudentManagement()
        id = "student2"
        name = "Piotr"
        age = 20

        # when
        result = student_management.add_student(id, name, age)

        # then
        self.assertEqual(result, True)

    def test_update_student_should_update_student(self):
        # given
        student_management = StudentManagement()
        id = "student1"
        name = "Adaam"
        age = 21

        # when
        result = student_management.update_student(id, name, age)

        # then
        self.assertEqual(result, True)

    def test_remove_student_should_remove_student(self):
        # given
        student_management = StudentManagement()
        id = "student1"

        # when
        result = student_management.remove_student(id)

        #then
        self.assertEqual(result, True)

    def test_add_grade_should_add_grade(self):
        # given
        student_management = StudentManagement()
        id = "student1"
        subject = "Fizyka"
        grade = 4.5

        # when
        result = student_management.add_grade(id, subject, grade)
        student_management.add_grade(id, "Fizyka", 4.0)

        # then
        self.assertEqual(result, True)

    def test_avg_grades_should_show_avg_of_all_grades_from_subject(self):
        # given
        student_management = StudentManagement()
        subject = "Fizyka"

        # when
        result = student_management.avg_grades(subject)

        # then
        self.assertEqual(result, 3.5)

if __name__ == '__main__':
    unittest.main()
