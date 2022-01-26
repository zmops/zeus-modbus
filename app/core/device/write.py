# -*- coding: utf-8 -*-
# 设备写入
# 作者: 三石
# 时间: 2022-01-21


import logging
from core.modbus import ModbusClient


logger = logging.getLogger(__name__)


class DeviceWrite(object):

    def __init__(self):
        """
        设备写入
        """
        self.logger = logger

    def single_register(self, ipaddress, address, value, slave, port=502) -> bool:
        """
        单个寄存器
        :param ipaddress: 设备IP地址
        :param port: 设备端口 默认502
        :param address: 寄存器地址
        :param slave: 从地址
        :param value: 写入值
        :return:
        """
        self.logger.info("创建modbus tcp连接, ipaddress: {}, port: {}".format(ipaddress, port))
        self.logger.info("设备写入, address: {}, value: {}".format(address, value))
        modbus = ModbusClient(ipaddress=ipaddress, port=port)
        response = modbus.write_register(address=address, value=value, unit=slave)
        modbus.close_client()

        return response
