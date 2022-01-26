# -*- coding: utf-8 -*-
# 字段校验异常拦截
# 作者: 三石
# 时间: 2021-12-15


import logging
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


logger = logging.getLogger(__name__)


async def validation_error_handler(_: Request, exc: Union[RequestValidationError, ValidationError]) -> JSONResponse:
    """
    字段校验异常拦截
    :param _:
    :param exc:
    :return:
    """
    logger.error("http请求参数校验失败, 地址: {}, 参数: {}, 错误信息: {}".format(_.url, exc.body, exc.errors()))
    return JSONResponse(
        {
            "errors": exc.errors(),
            "success": False,
            "code": HTTP_422_UNPROCESSABLE_ENTITY,
        },
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )
