#!/usr/bin/env python3
"""
@Project    ：argus-app-console 
@File       ：favicon.py 
@Author     ：三石
@Time       ：2022/5/20 15:39
@Annotation : icon视图
"""


import os
from django.http import HttpResponse
from django.conf import settings


def favicon_view(request):
    """
    显示favicon
    :param request:
    :return:
    """
    base_path = settings.BASE_DIR
    logo_file = os.path.join(base_path, "static/images/favicon.ico")
    file_favicon = open(logo_file, "rb")
    return HttpResponse(file_favicon.read(), content_type='image/jpg')
