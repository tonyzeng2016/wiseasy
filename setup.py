#!/usr/bin/env python
from setuptools import setup

version = "0.0.1"


setup(
    name="wiseasy",
    version=version,
    url='https://github.com/tonyzeng2016/wiseasy',
    project_urls={
        "Documentation": "https://wiseasy.readthedocs.io/",
    },
    description='the utility in wiseasy',
    long_description=u'''
    2018工作日判断;
    四舍五入,四舍六入五成双,进一,取整
    ''',
    install_requires=[
        "pandas","numpy"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: utility',
    ],
    keywords="workday,round",
)
