import sys
sys.path.append(r"./")

import pytest
from conftest import get_yaml_data
from src.model.calculator import Calculator
import allure


@allure.feature("作业二")#父级标注
class TestTaskTwo():

    @allure.severity(allure.severity_level.NORMAL)#标记严重级别
    @allure.link("https://www.baidu.com/",name="连接")#标记用例的连接
    @allure.story("加法运算用例")#子级标注
    @pytest.mark.run(order=1)#执行顺序
    @pytest.mark.usefixtures("setup_teardown")#调用fixtures方法
    @pytest.mark.parametrize("a,b,range_left,range_right",get_yaml_data(key="add"),ids=get_yaml_data(key="ids"))#参数
    def test_add(self,a,b,range_left,range_right):
        #allure.attach("content","name",allure.attachment_type.HTML) #给报告添加内容
        # allure.attach.file("file",allure.attachment_type.PNG) 给报告添加图片
        r=Calculator.add(a,b)
        if isinstance(r,float):
            r=round(r,2)
        with allure.step("加法断言"):#allure步骤说明
            assert (r>= range_left and  r<= range_right), "计算结果小于区间" if r < range_left else "计算结果大于区间" if r > range_left else r

    @allure.story("减法运算用例")
    @pytest.mark.run(order=3)
    @pytest.mark.usefixtures("setup_teardown")
    @pytest.mark.parametrize("a,b,range_left,range_right", get_yaml_data(key="sub"), ids=get_yaml_data(key="ids"))
    def test_sub(self,a,b,range_left,range_right):
        r = Calculator.sub(a, b)
        if isinstance(r, float):
            r = round(r, 2)
        with allure.step("断言"):
            assert (r >= range_left and r <= range_right), "计算结果小于区间" if r < range_left else "计算结果大于区间" if r > range_left else r
        pass

    @allure.story("乘法运算用例")
    @pytest.mark.run(order=4)
    # @pytest.mark.usefixtures("setup_teardown")
    @pytest.mark.parametrize("a,b,range_left,range_right", get_yaml_data(key="multiplication"), ids=get_yaml_data(key="ids"))
    def test_multiplication(self,a,b,range_left,range_right,setup_teardown):
        r = Calculator.multiplication(a, b)
        if isinstance(r, float):
            r = round(r, 2)
        with allure.step("断言"):
            assert (r >= range_left and r <= range_right), "计算结果小于区间" if r < range_left else "计算结果大于区间" if r > range_left else r
        pass

    @allure.story("除法运算用例")
    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures("setup_teardown")
    @pytest.mark.flaky(reruns=5, reruns_delay=2)
    @pytest.mark.parametrize("a,b,range_left,range_right", get_yaml_data(key="division"), ids=get_yaml_data(key="ids"))
    def test_division(self,a,b,range_left,range_right):
        r = Calculator.division(a, b)
        if isinstance(r, float):
            r = round(r, 2)
        with allure.step("断言"):
            assert (r >= range_left and r <= range_right), "计算结果小于区间" if r < range_left else "计算结果大于区间" if r > range_left else r
        pass



