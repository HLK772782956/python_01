
from python_01_zuoye.login
import unittest
class Testlogin(unittest.TestCase):
    #1.测试登录的用例

    #case1: 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)


# 初始化方法
   # def setUp(self) -> None:
        # print('开始运行方法：',sys._getframe().f_code.co_name)

# 清除方法
    # def tearDown(self) -> None:
        # print('开始运行方法'sys._getframe().f_code.co_name)