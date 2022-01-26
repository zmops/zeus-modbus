# -*- coding: utf-8 -*-
# 返回异常拦截
# 作者: 三石
# 时间: 2021-12-15


import logging
from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


logger = logging.getLogger(__name__)


async def response_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """
    返回异常拦截
    :param _:
    :param exc:
    :return:
    """
    logger.error("http请求错误, 地址: {}, 错误信息: {}".format(_.url, exc.detail))
    return JSONResponse(
        {
            "errors": [exc.detail],
            "success": False,
            "code": exc.status_code,
        },
        status_code=exc.status_code
    )
