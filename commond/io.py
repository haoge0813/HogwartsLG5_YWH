import yaml
import os


def get_yaml_data(path=None, filename=None, key=None) -> list:
    """
    获取数据
    :param path: 文件夹路径，没有则为当前文件所在的目录
    :param filename:文件名，没有则为data.yml
    :param key: 取yml文件的数据为key名字的数据，没有则默认返回全部
    :return:
    """
    p = os.path.join(os.path.dirname(path),"data.yml") if path else os.path.join(os.path.dirname(__file__), filename if filename else "data.yml")

    with open(p, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        if key:
            if key in data:
                return data[key]
            else:
                raise Exception("key not exists")
        return data
