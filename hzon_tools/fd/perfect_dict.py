# -*- coding: utf-8 -*-
"""
Created on 2021/4/8 11:32 上午
---------
@summary:
---------
@author: Boris
@email: boris_liu@foxmail.com
"""


def ensure_value(value):
    # 判断value是否为列表或元组类型
    if isinstance(value, (list, tuple)):
        # 创建一个空列表_value
        _value = []
        # 遍历value中的每个元素v
        for v in value:
            # 递归调用ensure_value函数处理v，并将处理后的结果添加到_value列表中
            _value.append(ensure_value(v))

        # 判断value是否为元组类型
        if isinstance(value, tuple):
            # 将_value列表转换为元组，并赋值给value
            value = tuple(_value)
        else:
            # 将_value列表赋值给value
            value = _value

    # 判断value是否为字典类型
    if isinstance(value, dict):
        # 调用PerfectDict函数处理value，并返回处理后的结果
        return PerfectDict(value)
    else:
        # 返回原值value
        return value


class PerfectDict(dict):
    """
    >>> data = PerfectDict({"id":1, "url":"xxx"})
    >>> data
    {'id': 1, 'url': 'xxx'}
    >>> data = PerfectDict(id=1, url="xxx")
    >>> data
    {'id': 1, 'url': 'xxx'}
    >>> data.id
    1
    >>> data.get("id")
    1
    >>> data["id"]
    1
    >>> id, url = data
    >>> id
    1
    >>> url
    'xxx'
    >>> data[0]
    1
    >>> data[1]
    'xxx'
    >>> data = PerfectDict({"a": 1, "b": {"b1": 2}, "c": [{"c1": [{"d": 1}]}]})
    >>> data.b.b1
    2
    >>> data[1].b1
    2
    >>> data.get("b").b1
    2
    >>> data.c[0].c1
    [{'d': 1}]
    >>> data.c[0].c1[0]
    {'d': 1}
    """

    def __init__(self, _dict: dict = None, _values: list = None, **kwargs):
        # 如果_dict不为None，则将_dict赋值给self.__dict__，否则如果kwargs不为空，则将kwargs赋值给self.__dict__，最后默认为空字典
        self.__dict__ = _dict or kwargs or {}
        # 移除self.__dict__中的"__values__"键及其对应的值
        self.__dict__.pop("__values__", None)
        # 调用父类的构造函数，传入self.__dict__和kwargs
        super().__init__(self.__dict__, **kwargs)
        # 如果_values不为None，则将_values赋值给self.__values__，否则将self.__dict__中的值转换为列表后赋值给self.__values__
        self.__values__ = _values or list(self.__dict__.values())

    def __getitem__(self, key):
        # 如果key是整数类型
        if isinstance(key, int):
            # 获取对应索引位置的value
            value = self.__values__[key]
        else:
            # 获取字典中对应key的value
            value = self.__dict__[key]

        # 返回经过ensure_value函数处理后的value
        return ensure_value(value)

    def __iter__(self, *args, **kwargs):
        # 遍历self.__values__列表中的每个元素
        for value in self.__values__:
            # 对每个元素调用ensure_value函数，并将结果作为生成器的值返回
            yield ensure_value(value)

    def __getattribute__(self, item):
        # 获取对象的属性值
        value = object.__getattribute__(self, item)

        # 如果属性名为"__dict__"或"__values__"
        if item == "__dict__" or item == "__values__":
            # 直接返回属性值
            return value

        # 否则对属性值进行ensure_value处理，并返回处理后的结果
        return ensure_value(value)

    def get(self, key, default=None):
        # 检查键是否在对象的属性字典中
        if key in self.__dict__:
            # 获取键对应的属性值
            value = self.__dict__[key]
            # 对属性值进行ensure_value处理，并返回处理后的结果
            return ensure_value(value)

        # 如果键不在对象的属性字典中，则返回默认值
        return default
