import unittest
from NameFunction_11_1 import get_formatted_name


class NameFunctionTest(unittest.TestCase):
    """ 测试 NameFunction_11_1 类 方法 """

    def test_get_formatted_name(self):
        """ 正确处理像 陈明 """
        formatted_name = get_formatted_name('陈', '明')
        self.assertEqual(formatted_name, '陈 明')


if __name__ == '__main__':
    unittest.main()
