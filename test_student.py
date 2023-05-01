import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Alex', 'Florea')

        self.assertEqual(student.full_name, 'Alex Florea')


if __name__ == '__main__':
    unittest.main()
