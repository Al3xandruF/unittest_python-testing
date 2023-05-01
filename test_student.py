import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Alex', 'Florea')

        self.assertEqual(student.full_name, 'Alex Florea')

    def test_email(self):
        student = Student('Alex', 'Florea')

        self.assertEqual(student.email, 'alex.florea@email.com')

    def test_alert_santa(self):
        student = Student('Alex', 'Florea')
        student.alert_santa()

        self.assertTrue(student.naughty_list)


if __name__ == '__main__':
    unittest.main()
