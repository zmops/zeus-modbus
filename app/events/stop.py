# -*- coding: utf-8 -*-
# 关闭事件
# 作者: 三石
# 时间: 2021-12-15


import logging
from typing import Callable
from fastapi import FastAPI


logger = logging.getLogger(__name__)


def create_stop_app_handler(application: FastAPI) -> Callable:
    """
    创建关闭事件
    :param application: 服务
    :return:
    """

    async def stop_app() -> None:
        logger.info("采集服务关闭中...")

    return stop_app
