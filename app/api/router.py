# -*- coding: utf-8 -*-
# 接口路由
# 作者: 三石
# 时间: 2022-01-11


from fastapi import APIRouter
from config import ConfigSettings
from api.device import data as device_data
from api.device import info as device_info


config_settings = ConfigSettings()


# 接口路由入口
api_router = APIRouter()
api_router.include_router(device_info.router, tags=["设备信息"], prefix=config_settings.device_prefix)
api_router.include_router(device_data.router, tags=["设备数据"], prefix=config_settings.device_prefix)
