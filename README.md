# hzon-tools

[![Downloads](https://static.pepy.tech/badge/dumb-menu)](https://pepy.tech/project/dumb-menu)

日常工作的时候我们总是会写一些重复的工具函数

包含**后端**，**数据处理**，**爬虫**等等使用python处理的场景

我会将一些工作中常用的文档以及demo也总结金来，方便沟通的查阅

zhon-tools是一个轻量级的python工具包，适用的平台包括**Windows**, **MacOS**, and **Linux**.


## Installation

```
pip install hzon_tools
```

https://pypi.org/project/hzon-tools/

https://github.com/ouyangguoyong/hzon-tool (I want stars ⭐ uwu)


## Usage

example:

```python
from hzon_tools import get_computer_name

computer_name = get_computer_name()

```


## Update log


`0.0.1` 创建项目

## how to upload a new version (for me)

en: https://packaging.python.org/tutorials/packaging-projects/ 

zh: https://python-packaging-zh.readthedocs.io/zh_CN/latest/minimal.html#id2

> make sure have twine installed first

1. change `setup.py`
2. testing `python3 setup.py develop`
3. `python3 setup.py sdist`
4. `twine upload dist/*`

