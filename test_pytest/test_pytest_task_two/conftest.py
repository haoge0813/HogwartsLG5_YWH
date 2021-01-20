import yaml
import os
import pytest

def get_yaml_data(path=None,filename=None,key=None):
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
"""
scope:
    function:方法
    class:类使用一次
    module:文件使用一次
    session:多个文件调用一次
"""
@pytest.fixture(scope="module")
def setup_teardown():
    print("\n============开始计算============")
    yield
    print("\n============结束计算============")


