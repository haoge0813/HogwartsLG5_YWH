import requests


class Base():


    def __init__(self):
        data = {
            "corpid": "ww727958f0008fb450",
            "corpsecret": "ZcyyOuds2_tHV6ojEpTQZaE2uBNGoIpNkEstO8B-TD8"
        }
        url = " https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        response = requests.get(url=url, params=data)

        self.access_token = response.json()["access_token"]

        self.s=requests.Session()

        self.s.params={"access_token":self.access_token}



    def send(self,*args, **kwargs):
        respones = self.s.request(*args,**kwargs)

        return respones.json()

