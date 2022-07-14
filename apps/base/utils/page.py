#!/usr/bin/env python3
"""
@Project    ：argus-app-console 
@File       ：page.py 
@Author     ：三石
@Time       ：2022/7/6 17:23
@Annotation : 分页工具类
"""

from django.core.paginator import Paginator, EmptyPage


class UtilsPage(object):
    def __init__(self, page=1, size=10):
        """
        分页工具类
        """

        self.db_page = []

        try:
            self.page = int(page)
            self.size = int(size)
        except (ValueError, TypeError):
            self.page = 1
            self.size = 10

    def get_by_page(self, db_list):
        """
        数据对象转分页
        :param db_list: 数据对象
        :return:
        """
        db = Paginator(object_list=db_list, per_page=self.size)
        try:
            db_page = db.page(self.page)
        except (EmptyPage, ZeroDivisionError):
            db_page = []
        self.db_page = db_page
