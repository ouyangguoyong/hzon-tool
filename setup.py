import codecs
import os

from setuptools import find_packages, setup
from feapder.utils import tools
# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = '勇哥python工具包'
LONG_DESCRIPTION = '将一些公共的，第三方的以及自己工作日常，爬虫工作中常用的爬虫开发工具和方法做了一个大集合'

# Setting up
setup(
    name="hzon_tools",
    version=VERSION,
    author="勇哥的ID",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'getch; platform_system=="Unix"',
        'getch; platform_system=="MacOS"',
    ],
    keywords=['python', 'hzon_tools','hzon', 'spider', 'windows', 'mac', 'linux'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
