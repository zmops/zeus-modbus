#!/usr/bin/env python3
"""
@Project    ：argus-app-console 
@File       ：basics.py 
@Author     ：三石
@Time       ：2022/7/11 14:33
@Annotation : 异常中间件
"""

import logging
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from base.utils import UtilsResponse
from base.enums import EnumCode, EnumMsg
from datetime import datetime

logger = logging.getLogger(__name__)


class ExceptionMiddleware(MiddlewareMixin):
    """
    异常中间件
    """

    def process_request(self, request):

        logger.info("请求地址：{url}".format(url=request.build_absolute_uri()))

        return None

    def process_response(self, request, response):
        resp = UtilsResponse()

        # 状态码404
        if response.status_code == 404:
            logger.error("请求地址不存在: {url}".format(url=request.path))

            resp.code = EnumCode.UrlNotFound.value
            resp.msg = EnumMsg.UrlNotFound.value

            return JsonResponse(resp.response)

        # 判断api开头的请求
        if request.path.startswith("/admin/"):
            return response
        else:
            # 状态码
            logger.info("返回状态码: {code}".format(code=response.status_code))

            # 正常返回
            if response.status_code in [200, 302]:
                return response

            # 400异常
            elif response.status_code == 400:
                logger.error("400异常信息: {resp}".format(resp=response))

                resp.code = EnumCode.InvalidParam.value
                resp.msg = EnumMsg.InvalidError.value
                return JsonResponse(resp.response)

            # 未知异常
            else:
                logger.error("未知异常信息: {resp}".format(resp=response))

                resp.code = EnumCode.UnknownError.value
                resp.msg = EnumMsg.UnknownError.value.format(response.status_code)
                now_time = datetime.now()
                now_time_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
                resp.add_field(name="error", value="[{time}]发生异常, 详情查看日志".format(time=now_time_str))

                return JsonResponse(resp.response)
