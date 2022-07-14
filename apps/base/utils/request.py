#!/usr/bin/env python3
"""
@Project    ：argus-app-console 
@File       ：requests.py 
@Author     ：三石
@Time       ：2022/5/20 15:40
@Annotation : 请求工具类
"""

import httpx
import logging
from typing import Optional
from httpx import DigestAuth


logger = logging.getLogger(__name__)


class UtilsRequest(object):

    def __init__(self):
        """
        接口工具类
        """
        # 超时时间
        self.timeout = 5

    def get(self, url, headers=None, params=None, digest_auth_username=None, digest_auth_password=None) -> Optional[dict] is False:
        """
        get请求
        :param url:
        :param headers:
        :param params:
        :param digest_auth_username:
        :param digest_auth_password:
        :return:
        """
        try:
            if digest_auth_username is not None and digest_auth_password is not None:
                response = httpx.get(url=url, headers=headers, params=params, timeout=self.timeout, verify=False, auth=DigestAuth(digest_auth_username, digest_auth_password))
            else:
                response = httpx.get(url=url, headers=headers, params=params, timeout=self.timeout, verify=False)

            logger.debug("调用返回: {}".format(response.text))
            return response
        except httpx.RequestError as error:
            logger.error("接口请求错误: {}".format(error))
            return False

    def post(self, url, headers=None, params=None, data=None) -> Optional[dict] is False:
        """
        post请求
        :param url:
        :param headers:
        :param params:
        :param data:
        :return:
        """
        try:
            response = httpx.post(url=url, headers=headers, params=params, json=data, timeout=self.timeout, verify=False)

            logger.debug("调用返回: {}".format(response.text))
            return response
        except httpx.RequestError as error:
            logger.error("接口请求错误: {}".format(error))
            return False
