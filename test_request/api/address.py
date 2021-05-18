from test_request.api.base import Base


class Address(Base):

    def create_member(self,params):
        url="https://qyapi.weixin.qq.com/cgi-bin/user/create"
        return self.send("post",url,json=params)
        pass

    def update_member(self,params):
        url="https://qyapi.weixin.qq.com/cgi-bin/user/update"
        return self.send("post",url,json=params)
        pass

    def delete_member(self,userid):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get",url)
        pass

    def get_member(self,userid):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get",url)
        pass

