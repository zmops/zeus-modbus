# -*- coding: utf-8 -*-
# 设备数据
# 作者: 三石
# 时间: 2021-12-15


import logging
from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from device import DeviceSettings
from core.device import DeviceRead, DeviceWrite
from core.enums import MsgEnum, CodeEnum
from .schemas import SchemaUpdateCurrent


logger = logging.getLogger(__name__)

device_settings = DeviceSettings()

router = APIRouter()


@router.get("/data/query/{device_id}/", summary="查询指定设备数据")
def query(device_id: str) -> JSONResponse:
    """
    单个设备查询此模型配置的所有寄存器数据
    :param device_id: 设备ID
    :return:
    """
    logger.info("查询当前数据")

    device = device_settings.dict().get(device_id)
    logger.debug("当前设备信息: {}".format(device))

    # 判断失败是否存在
    if not device:
        return JSONResponse(
            content={
                "data": None,
                "msg": MsgEnum.error_device_not_found.value,
                "success": False,
                "code": CodeEnum.error.value,
            },
            status_code=HTTP_200_OK,
        )

    device_model = device.get("model")
    device_ipaddress = device.get("ipaddress")
    device_port = device.get("port")
    device_slave = device.get("slave")

    # 根据设备类型来调用相应方法
    device_read = DeviceRead()
    device_read_func = getattr(device_read, device_model, None)

    # 判断设备模型是否匹配
    if not device_read_func:
        return JSONResponse(
            content={
                "data": None,
                "msg": MsgEnum.error_model_not_match.value,
                "success": False,
                "code": CodeEnum.error.value,
            },
            status_code=HTTP_200_OK
        )
    else:
        payload = device_read_func(ipaddress=device_ipaddress, port=device_port, slave=device_slave)

        return JSONResponse(
            content={
                "data": payload,
                "msg": MsgEnum.success.value,
                "success": True,
                "code": CodeEnum.success.value,
            },
            status_code=HTTP_200_OK
        )


@router.post("/data/update/{device_id}/", summary="更新指定设备数据")
def update(device_id: str, body: SchemaUpdateCurrent) -> JSONResponse:
    """
    单个设备更新单个寄存器数据
    :param device_id: 设备ID
    :param body: 请求体
    :return:
    """
    logger.info("更新当前数据")

    # 解析查询设备信息
    device = device_settings.dict().get(device_id)
    logger.debug("当前设备信息: {}".format(device))

    # 判断失败是否存在
    if not device:
        return JSONResponse(
            content={
                "data": None,
                "msg": MsgEnum.error_device_not_found.value,
                "success": False,
                "code": CodeEnum.error.value,
            },
            status_code=HTTP_200_OK,
        )

    ipaddress = device.get("ipaddress")
    port = device.get("port")
    slave = device.get("slave")
    address = body.address
    value = body.value

    # 设备写入
    device_write = DeviceWrite()
    result = device_write.single_register(ipaddress=ipaddress, port=port, address=address, value=value, slave=slave)

    # 写入失败
    if not result:
        return JSONResponse(
            content={
                "data": None,
                "msg": MsgEnum.error_update.value,
                "success": False,
                "code": CodeEnum.error.value,
            },
            status_code=HTTP_200_OK,
        )
    # 写入成功
    else:
        return JSONResponse(
            content={
                "data": None,
                "msg": MsgEnum.success.value,
                "success": True,
                "code": CodeEnum.success.value,
            },
            status_code=HTTP_200_OK,
        )
