# -*- coding: utf-8 -*-
# 配置设置
# 作者: 三石
# 时间: 2021-12-10


import os
from pydantic import BaseSettings


class ConfigSettings(BaseSettings):
    # 基础路径
    base_path: str = os.path.abspath(os.path.dirname(__file__))
    # 日志路径
    log_path: str = os.path.join(base_path, "logs")
    # 文件路径
    files_path: str = os.path.join(base_path, "files")
    # csv路径
    files_csv_path: str = os.path.join(files_path, "csv")

    # 接口前缀
    api_prefix: str = "/api"
    task_prefix: str = "/task"

    # zabbix配置
    zabbix: dict = {
        "ip": "127.0.0.1",
        "port": 10051,
        "interval": 60
    }

    application: dict = {
        "title": "modbus采集平台",
        "description": "基于python的FastApi+pymodbus+APScheduler开发的采集平台定时发送采集数据给zabbix服务端.",
        "version": "V1.1"
    }
