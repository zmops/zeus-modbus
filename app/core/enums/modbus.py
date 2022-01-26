# -*- coding: utf-8 -*-
# modbus code枚举
# 作者: 三石
# 时间: 2022-01-21


import enum


class ModbusCodeEnum(int, enum.Enum):
    """modbus命令"""

    input_registers = 6
