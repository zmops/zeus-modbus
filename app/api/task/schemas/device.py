#!/usr/bin/env python3
"""
@Project    ：zeus-modbus 
@File       ：device.py 
@Author     ：三石
@Time       ：2022/6/20 10:20
@Annotation : 模式-设备
"""


from pydantic import BaseModel, conint


class SchemaDevice(BaseModel):
    """模式-设备"""

    # 设备编号
    device_code: str
