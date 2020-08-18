import unittest

from 测试脚本 import testbaidu1


def creatsuite():
    suite = unittest.TestSuite()
    # 将测试用例加入到测试套件中
    suite.addTest(testbaidu1.Baidu1("test_baidusearch"))
    suite.addTest(testbaidu1.Baidu1("test_hao"))
    return suite

if __name__ == "__main__":
    suite = creatsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)