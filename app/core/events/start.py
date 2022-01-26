# -*- coding: utf-8 -*-
# 开始事件
# 作者: 三石
# 时间: 2021-12-15


import logging
from typing import Callable
from fastapi import FastAPI
from config import ConfigSettings
from core.task import task_send_data
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler


logger = logging.getLogger(__name__)

config_settings = ConfigSettings()


def create_start_app_handler(application: FastAPI) -> Callable:
    """
    创建开始事件
    :param application: 服务
    :return:
    """

    async def start_app() -> None:
        logger.info("采集服务开启中...")

        # 引入任务-发送
        zabbix = config_settings.zabbix
        zabbix_ip = zabbix.get("ip", "127.0.0.1")
        zabbix_port = zabbix.get("port", 10051)
        zabbix_interval = zabbix.get("interval", 60)

        # 线程池
        executors = {
            "default": ThreadPoolExecutor(20)
        }

        # 后台定时任务
        scheduler = BackgroundScheduler(timezone="Asia/Shanghai", executors=executors)
        scheduler.add_job(task_send_data, id="job_task_send", trigger="interval", seconds=zabbix_interval, replace_existing=True)
        scheduler.start()

        logger.info("定时采集服务已开启, zabbix服务地址: {} 端口: {}, 采集间隔: {}秒".format(zabbix_ip, zabbix_port, zabbix_interval))
        logger.info("================================================================================================")

    return start_app

