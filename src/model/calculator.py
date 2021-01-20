

class Calculator:
    @staticmethod
    def check_number_type(data):
        """
        校验数据类型是否int类型
        :param data:
        :return:
        """
        assert (isinstance(data, int) or isinstance(data, float)),"参数类型不是数值类型"

    @staticmethod
    def add(a,b):
        """
        加法运算
        :param a:
        :param b:
        :return:
        """
        Calculator.check_number_type(a)
        Calculator.check_number_type(b)
        return a+b

    @staticmethod
    def sub(a,b):
        """
        减法运算
        :param a:
        :param b:
        :return:
        """
        Calculator.check_number_type(a)
        Calculator.check_number_type(b)
        return a-b

    @staticmethod
    def multiplication(a,b):
        '''
        乘法运算
        :param a:
        :param b:
        :return:
        '''
        Calculator.check_number_type(a)
        Calculator.check_number_type(b)
        return a*b

    @staticmethod
    def division(a,b):
        """
        除法运算
        :param a:
        :param b:
        :return:
        """
        Calculator.check_number_type(a)
        Calculator.check_number_type(b)
        return a/b