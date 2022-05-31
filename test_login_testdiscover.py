# 使用TestLodaer()可以批量添加测试用例，解决单条测试用例效率问题
"""
TestLodaer（）：
1，可以批量运行测试用例：方法：discover(test_dir,patten='test*.py)
test_dir:指定要搜索的路径
patten:指定匹配的模式，在test_dir目录下搜索所有的patten文件

"""
from package_unittest.iter03_add_user import login
from loguru import logger


import unittest
import sys
class TestLogin(unittest.TestCase):
# 初始化方法
    def setUp(self) -> None:
        print('开始运行方法：', sys._getframe().f_code.co_name)
# 清除方法
    def tearDown(self) -> None:
        print('开始运行方法：', sys._getframe().f_code.co_name)

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
# case3 : 输入空的用户和密码进行登录
    def test_password_is_null(self):
        except_value = 2  # 期望值
        actual_value = login('admin','').get('code')
        self.assertEqual(except_value, actual_value)

if __name__ == '__main__':
    # 创建一个套件
    suite_a = unittest.TestLoader().discover('.',pattern='test_login_testdiscover.py')
    print(suite_a)

    runner = unittest.TextTestRunner()
    runner.run(suite_a)