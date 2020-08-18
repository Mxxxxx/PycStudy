import unittest

from 测试脚本 import testbaidu1


def creatsuitr():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testbaidu1.Baidu1))
    return suite


if __name__ == "__main__":
    suite = creatsuitr()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
