import pytest
from test_request.api.address import Address

class TestAddress():

    def setup_class(self):
        self.address=Address()
        pass

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("params",[{"userid":"zhangsan","name":"张三","mobile": "+86 13800000011","department":[1]},
                                       {"userid":"lisi","name":"李四","mobile": "+86 13800000022","department":[1]},
                                       {"userid":"wangwu","name":"王五","mobile": "+86 13800000033","department":[1]}])
    def test_create_member(self,params:dict):

        data=self.address.create_member(params)

        assert data.get("errcode")==0
        pass

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("userid",
                             ["zhangsan",
                              "lisi",
                              "wangwu"])
    def test_get_member(self,userid):

        data=self.address.get_member(userid)
        assert data.get("errcode") == 0
        assert data.get("userid") == userid
        pass

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("userid",
                             ["zhangsan",
                              "lisi",
                              "wangwu"])
    def test_delete_member(self,userid):
        data=self.address.delete_member(userid)
        assert data.get("errcode") == 0
        assert data.get("errmsg") == "deleted"
        pass

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("params",
                             [{"userid": "zhangsan", "name": "张三1", "mobile": "+86 13800000011", "department": [1]},
                              {"userid": "lisi", "name": "李四2", "mobile": "+86 13800000022", "department": [1]},
                              {"userid": "wangwu", "name": "王五3", "mobile": "+86 13800000033", "department": [1]}])
    def test_update_member(self,params):
        print(params)
        data=self.address.update_member(params)
        assert data.get("errcode")==0
        assert data.get("errmsg") == "updated"
        pass