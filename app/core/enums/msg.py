# -*- coding: utf-8 -*-
# 消息枚举
# 作者: 三石
# 时间: 2022-01-21


import enum


class MsgEnum(enum.Enum):
    """消息枚举"""

    success = "请求成功"
    start_send = "开启发送任务"
    error_model_not_match = "设备型号不匹配"
    error_device_not_found = "设备不存在"
    error_update = "设备更新失败"
