import HTMLTestRunner
import os
import sys
import time
import unittest


def creatsuit():
    discover = unittest.defaultTestLoader.discover("../测试脚本",pattern="testbaidu1.py",top_level_dir=None)
    print(discover)
    return discover
if __name__ == "__main__":
    # 当前文件所在得到文件夹的绝对路径
    curpath =sys.path[0]
    if not os.path.exists(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')

    now=time.strftime("%Y-%m-%d-%H %M %S",time.localtime(time.time()))
    print("------------")
    print(time.time())
    print("------------")
    print(time.localtime(time.time()))
    print("------------")
    print(now)

    filename=curpath+'/resultreport/'+now+'resultreport.html'
    with open(filename,'wb+') as fp:
        runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"用例报告" ,verbosity=2)
        suite = creatsuit()
        runner.run(suite)