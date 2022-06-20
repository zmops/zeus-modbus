#!/usr/bin/env python3
"""
@Project    ：zeus-modbus 
@File       ：router.py 
@Author     ：三石
@Time       ：2022/6/20 10:30
@Annotation : 任务路由
"""


from fastapi import APIRouter
from config import ConfigSettings
from api.task import main as api_task


config_settings = ConfigSettings()


# 接口路由入口
api_router = APIRouter()
api_router.include_router(api_task.router, tags=["任务"], prefix=config_settings.task_prefix)
