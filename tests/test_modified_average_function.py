from unittest import TestCase

from PythonPackage.chapter_four.modified_average_function import modified_average_function


class Test(TestCase):
    def test_modified_average_function(self):
        self.assertEqual(modified_average_function(1, 2, 3), 2.7)
