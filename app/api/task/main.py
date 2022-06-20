#!/usr/bin/env python3
"""
@Project    ：zeus-modbus 
@File       ：task.py 
@Author     ：三石
@Time       ：2022/6/20 10:20
@Annotation : 任务-主要
"""


import logging
from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from device import DeviceSettings
from core.enums import MsgEnum, CodeEnum
from .schemas import SchemaDevice


logger = logging.getLogger(__name__)

device_settings = DeviceSettings()

router = APIRouter()


@router.post("/run/", summary="任务执行")
def run(body: SchemaDevice) -> JSONResponse:
    """

    :param body:
    :return:
    """
    logger.info("任务执行")

    device_code = body.device_code

    return JSONResponse(
        content={
            "data": device_code,
            "msg": MsgEnum.success.value,
            "success": True,
            "code": CodeEnum.success.value,
        },
        status_code=HTTP_200_OK
    )
