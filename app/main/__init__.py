#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/3/25
# @File Name: __init__.py.py


from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors

__all__ = [
    'main',
    'views',
    'errors'
]
