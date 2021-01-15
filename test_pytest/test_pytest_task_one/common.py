import yaml
import os

def get_data(path=None,filename=None,key=None):
    """
    获取数据
    :param path: 文件夹路径，没有则为当前文件所在的目录
    :param filename:文件名，没有则为data.yml
    :param key: 取yml文件的数据为key名字的数据，没有则默认返回全部
    :return:
    """
    p= path if path else os.path.join(os.path.dirname(__file__),filename if filename else "data.yml")
    with open(p,encoding='utf-8') as f:
        data = yaml.safe_load(f)
        if key:
            if key in data:
                return data[key]
            else:
                raise Exception("key not exists")
        return data


class Calculator:

    def check_number_type(self,data):
        """
        校验数据类型是否int类型
        :param data:
        :return:
        """
        assert (isinstance(data, int) or isinstance(data, float)),"参数类型不是数值类型"

    def add(self,a,b):
        """
        加法运算
        :param a:
        :param b:
        :return:
        """
        self.check_number_type(a)
        self.check_number_type(b)
        return a+b

    def sub(self,a,b):
        """
        减法运算
        :param a:
        :param b:
        :return:
        """
        self.check_number_type(a)
        self.check_number_type(b)
        return a-b

    def multiplication(self,a,b):
        '''
        乘法运算
        :param a:
        :param b:
        :return:
        '''
        self.check_number_type(a)
        self.check_number_type(b)
        return a*b

    def division(self,a,b):
        """
        除法运算
        :param a:
        :param b:
        :return:
        """
        self.check_number_type(a)
        self.check_number_type(b)
        return a/b