#!/usr/bin/env python3
"""
@Project    ：argus-app-console 
@File       ：response.py 
@Author     ：三石
@Time       ：2022/6/1 11:45
@Annotation : 返回response工具类
"""


from base.enums import EnumCode, EnumMsg


class UtilsResponse(object):

    def __init__(self):
        """
        返回response工具类
        """
        self.data = []

        self.code = EnumCode.Success.value
        self.msg = EnumMsg.Success.value

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name is not None:
            self.__dict__[name] = value

    @property
    def response(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        body["data"] = body.pop("data")
        body["msg"] = body.pop("msg")
        body["code"] = body.pop("code")
        return body
