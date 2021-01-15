
import pytest
import common

class TestTaskOne():
    def setup_class(self):
        """
        类执行前运行
        :return:
        """
        self.calculator=common.Calculator()
        pass
    def teardown_class(self):
        """
        类结束后执行
        :return:
        """
        print("\n==============自动化测试结束==============")

    def setup_method(self):
        """
        用例执行前执行
        :return:
        """
        print("\n==========开始计算==========")
        pass

    def teardown_method(self):
        """
        用例执行完执行
        :return:
        """
        print("\n==========结束计算==========")
        pass

    @pytest.mark.parametrize("a,b,range_left,range_right",common.get_data(key="add"),ids=common.get_data(key="ids"))
    def test_add(self,a,b,range_left,range_right):
        r=self.calculator.add(a,b)
        if isinstance(r,float):
            r=round(r,2)

        assert (r>= range_left and  r<= range_right), "计算结果小于区间" if r < range_left else "计算结果大于区间" if r > range_left else r

    @pytest.mark.parametrize("a,b,range_left,range_right", common.get_data(key="sub"), ids=common.get_data(key="ids"))
    def test_sub(self,a,b,range_left,range_right):
        r = self.calculator.sub(a, b)
        if isinstance(r, float):
            r = round(r, 2)

        assert (r >= range_left and r <= range_right), "计算结果小于区间" if r < range_left else "计算结果大于区间" if r > range_left else r
        pass

    @pytest.mark.parametrize("a,b,range_left,range_right", common.get_data(key="multiplication"), ids=common.get_data(key="ids"))
    def test_multiplication(self,a,b,range_left,range_right):
        r = self.calculator.multiplication(a, b)
        if isinstance(r, float):
            r = round(r, 2)

        assert (r >= range_left and r <= range_right), "计算结果小于区间" if r < range_left else "计算结果大于区间" if r > range_left else r
        pass

    @pytest.mark.parametrize("a,b,range_left,range_right", common.get_data(key="division"), ids=common.get_data(key="ids"))
    def test_division(self,a,b,range_left,range_right):
        r = self.calculator.division(a, b)
        if isinstance(r, float):
            r = round(r, 2)

        assert (r >= range_left and r <= range_right), "计算结果小于区间" if r < range_left else "计算结果大于区间" if r > range_left else r
        pass



