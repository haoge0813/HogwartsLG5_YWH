import requests
import json
def test_task_one():
    data={
        "corpid": "ww727958f0008fb450",
        "corpsecret": "ZcyyOuds2_tHV6ojEpTQZaE2uBNGoIpNkEstO8B-TD8"
    }
    url=" https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    response=requests.get(url=url,params=data)

    access_token=response.json()["access_token"]


    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"

    data={
            "userid": "zhangsan",
            "name": "王五",
            "alias": "jackzhang",
            "mobile": "+86 13800000011",
            "department": [1]

        }
    requests.post(url=url,data=json.dumps(data))

    data={
        "access_token":access_token,
        "userid":"zhangsan"

    }
    url="https://qyapi.weixin.qq.com/cgi-bin/user/get"
    response=requests.get(url=url,params=data)
    print(response.json())


    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_token}"
    data={
        "userid": "zhangsan",
        "name": "赵六",
    }
    response=requests.post(url=url,json=data)

    print(response.json())


    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={access_token}&userid=zhangsan"

    response=requests.get(url=url)
    print(response.json())
