# -*- coding: utf-8 -*-
# 开始事件
# 作者: 三石
# 时间: 2021-12-15


import logging
from typing import Callable
from fastapi import FastAPI


logger = logging.getLogger(__name__)


def create_start_app_handler(application: FastAPI) -> Callable:
    """
    创建开始事件
    :param application: 服务
    :return:
    """

    async def start_app() -> None:
        logger.info("采集服务开启中...")

    return start_app
