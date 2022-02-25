# -*- coding: utf-8 -*-
# 设备信息
# 作者: 三石
# 时间: 2021-12-15


import logging
from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from device import DeviceSettings
from core.enums import CodeEnum, MsgEnum
from core.device import DeviceRead


logger = logging.getLogger(__name__)

device_settings = DeviceSettings()

router = APIRouter()


@router.get("/info/query_device/", summary="查询设备信息")
def query_device() -> JSONResponse:
    """
    查询所有设备信息
    :return:
    """
    logger.info("查询设备信息")

    devices = device_settings.devices

    data = []
    for device in devices:

        logger.debug("当前数据信息: {}".format(device))

        data.append(device)

    return JSONResponse(
        content={
            "data": data,
            "msg": MsgEnum.success.value,
            "success": True,
            "code": CodeEnum.success.value,
        },
        status_code=HTTP_200_OK
    )


@router.get("/info/query_model/", summary="查询型号信息")
def query_model() -> JSONResponse:
    """
    查询所有已定义的型号信息
    :return:
    """
    logger.info("查询型号信息")

    device_read = DeviceRead()
    data = device_read.support_models

    return JSONResponse(
        content={
            "data": data,
            "msg": MsgEnum.success.value,
            "success": True,
            "code": CodeEnum.success.value,
        },
        status_code=HTTP_200_OK
    )
