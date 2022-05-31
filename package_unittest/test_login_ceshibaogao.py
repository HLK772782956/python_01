# 问题：用unittest的测试报告太简单，只能在控制台查看，想生成的报告更详细，能在浏览器打开

# 解决方法：使用HMTLTestRunner模块生成测试报告，原理：将运行的测试报告结果输出到HTML文件中

# 前置条件：直接现成的

"""
类：HTMLTestRunner(f,title.,description)


"""


from package_unittest.HTMLTestRunner import HTMLTestRunner # 新加



from package_unittest.iter03_add_user import login
from loguru import logger


import unittest
import sys
class TestLogin(unittest.TestCase):
# 初始化方法

# 1.测试登录的测试用例


# case1 : 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        except_value = 0            # 期望值
        actual_value = login('admin','123456').get('code') # 实际值
        self.assertEqual(except_value,actual_value)
# case2 : 输入错误的用户和密码进行登录
    def test_user_wrong(self):
        except_value = 1  # 期望值
        actual_value = login('bca','123456').get('code')
        self.assertEqual(except_value, actual_value)
# case 3 : 输入空的用户和密码进行登录
    def test_password_is_null(self):
        except_value = 1  # 期望值
        actual_value = login('admin','').get('code')
        self.assertEqual(except_value, actual_value)

if __name__ == '__main__':
    # 创建一个套件
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_user_wrong'))
    suite_a.addTest(TestLogin('test_password_is_null'))
    print(suite_a)

    # 创建一个测试报告文件，HTML模式的
    test_report = './test_report.html'   #新加

    with open(test_report,'wb') as f:    #新加

        runner = HTMLTestRunner(f,title='测试报告',description='测试报告描述')     #新加
        runner.run(suite_a)