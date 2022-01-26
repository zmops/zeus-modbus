# -*- coding: utf-8 -*-
# modbus客户端
# 作者: 三石
# 时间: 2021-10-21


import logging
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ModbusException


logger = logging.getLogger(__name__)


class ModbusClient(object):

    def __init__(self, ipaddress, port=502):
        """
        modbus客户端
        :param ipaddress: ip地址
        :param port: 端口 默认502
        """
        self.ipaddress = ipaddress
        self.port = port

        self.client = self.create_tcp_client()

    def create_tcp_client(self) -> ModbusTcpClient:
        """
        创建tcp连接客户端
        :return:
        """
        logger.info("创建modbus tcp连接, host: {},port: {}".format(self.ipaddress, self.port))
        client = ModbusTcpClient(
            host=self.ipaddress,
            port=self.port
        )
        client.connect()
        return client

    def close_client(self):
        """
        关闭连接
        :return:
        """
        self.client.close()

    def read_discrete_inputs(self, address, count, unit):
        """
        读写线圈
        :param address: 开始地址
        :param count: 读取多少位
        :param unit: 从地址 默认1
        :return:
        """
        payload = {}
        try:
            response = self.client.read_discrete_inputs(address=address, count=count, unit=unit)
            for x, y in enumerate(response.bits):
                payload["key{}".format(address + x)] = y
        except (AttributeError, ModbusException) as e:
            payload["error"] = str(e)

        logger.info("payload: {}".format(payload))
        return payload

    def read_input_registers(self, address, count, unit):
        """
        读写寄存器
        :param address: 开始地址
        :param count: 读取多少位
        :param unit: 从地址 默认1
        :return:
        """
        payload = {}
        try:
            response = self.client.read_input_registers(address=address, count=count, unit=unit)
            payload = {}
            for x, y in enumerate(response.registers):
                payload["key{}".format(address + x)] = y
        except (AttributeError, ModbusException) as e:
            payload["error"] = str(e)

        logger.info("payload: {}".format(payload))
        return payload

    def read_holding_registers(self, address, count, unit):
        """
        读保持寄存器
        :param address: 开始地址
        :param count: 读取多少位
        :param unit: 从地址 默认1
        :return:
        """
        payload = {}
        try:
            response = self.client.read_holding_registers(address=address, count=count, unit=unit)
            payload = {}
            for x, y in enumerate(response.registers):
                payload["key{}".format(address + x)] = y
        except (AttributeError, ModbusException) as e:
            payload["error"] = str(e)

        logger.info("payload: {}".format(payload))
        return payload

    def write_register(self, address, value, unit):
        """
        写寄存器
        :param address: 开始地址
        :param value: 读取多少位
        :param unit: 从地址 默认1
        :return:
        """

        try:
            logger.info("写入寄存器 address: {}, value: {}, unit: {}".format(address, value, unit))
            self.client.write_register(address=address, value=value, unit=unit)
            return True
        except ModbusException as e:
            logger.error("发生异常: {}".format(e))
            return False

