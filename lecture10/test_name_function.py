import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确的处理像Chen Han这样的姓名吗？"""
        formatted_name = get_formatted_name('Chen', 'Han')
        self.assertEqual(formatted_name, 'Chen Han')

    def test_first_last_middle_name(self):
        """能够正确的处理像Chen Zhi An这样的姓名吗？"""
        formatted_name = get_formatted_name('Chen', 'Zhi', 'An')
        self.assertEqual(formatted_name, 'Chen Zhi An')


unittest.main()