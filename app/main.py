# -*- coding: utf-8 -*-
# 主函数
# 作者: 三石
# 时间: 2021-12-15


import logging.config
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from config import ConfigSettings
from log import LogConfig
from api.router import api_router
from core.errors import response_error_handler, validation_error_handler
from events import create_start_app_handler, create_stop_app_handler


def create_application() -> FastAPI:

    # 导入日志配置
    logging.config.dictConfig(LogConfig)

    # 导入配置
    config_settings = ConfigSettings()
    config_application = config_settings.application

    # 引入应用
    application = FastAPI(
        title=config_application.get("title"),
        description=config_application.get("description"),
        version=config_application.get("version")
    )

    # 应用开启
    application.add_event_handler(
        "startup",
        create_start_app_handler(application),
    )
    # 应用关闭
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )

    # 自定义异常
    application.add_exception_handler(HTTPException, response_error_handler)
    application.add_exception_handler(RequestValidationError, validation_error_handler)

    # 引入api路由
    application.include_router(api_router, prefix=config_settings.api_prefix)

    return application


app = create_application()
