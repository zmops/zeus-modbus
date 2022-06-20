#!/usr/bin/env python3
"""
@Project    ：zeus-modbus 
@File       ：client.py 
@Author     ：三石
@Time       ：2022/6/20 10:32
@Annotation : modbus客户端
"""


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

    def read_coils(self, address, count, unit) -> dict:
        """
        读线圈
        :param address: 开始地址
        :param count: 读取多少位
        :param unit: 从地址
        :return:
        """
        payload = {}
        try:
            response = self.client.read_coils(address=address, count=count, unit=unit)
            logger.debug("Modbus read_coils 返回: {}".format(response))
            for x, y in enumerate(response.bits):
                payload["bit{}".format(address + x)] = y
            logger.debug("payload: {}".format(payload))
            return {
                "success": True,
                "payload": payload
            }
        except (AttributeError, ModbusException) as e:
            logger.error("Modbus异常: {}".format(str(e)))
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            self.client.close()

    def read_discrete_inputs(self, address, count, unit) -> dict:
        """
        读写线圈
        :param address: 开始地址
        :param count: 读取多少位
        :param unit: 从地址
        @return:
        """
        payload = {}
        try:
            response = self.client.read_discrete_inputs(address=address, count=count, unit=unit)
            logger.debug("Modbus read_discrete_inputs 返回: {}".format(response))
            for x, y in enumerate(response.bits):
                payload["bit{}".format(address + x)] = y
            logger.debug("payload: {}".format(payload))
            return {
                "success": True,
                "payload": payload
            }
        except (AttributeError, ModbusException) as e:
            logger.error("Modbus异常: {}".format(str(e)))
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            self.client.close()

    def read_input_registers(self, address, count, unit) -> dict:
        """
        读写寄存器
        :param address: 开始地址
        :param count: 读取多少位
        :param unit: 从地址
        @return:
        """
        payload = {}
        try:
            response = self.client.read_input_registers(address=address, count=count, unit=unit)
            logger.debug("Modbus read_input_registers 返回: {}".format(response))
            for x, y in enumerate(response.registers):
                payload[address + x] = y
            logger.debug("payload: {}".format(payload))
            return {
                "success": True,
                "payload": payload
            }
        except (AttributeError, ModbusException) as e:
            logger.error("Modbus异常: {}".format(str(e)))
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            self.client.close()

    def read_holding_registers(self, address, count, unit) -> dict:
        """
        读保持寄存器
        :param address: 开始地址
        :param count: 读取多少位
        :param unit: 从地址
        @return:
        """
        payload = {}
        try:
            response = self.client.read_holding_registers(address=address, count=count, unit=unit)
            logger.debug("Modbus read_holding_registers 返回: {}".format(response))
            for x, y in enumerate(response.registers):
                payload[address + x] = y
            logger.debug("payload: {}".format(payload))
            return {
                "success": True,
                "payload": payload
            }
        except (AttributeError, ModbusException) as e:
            logger.error("Modbus异常: {}".format(str(e)))
            return {
                "success": False,
                "error": str(e)
            }
        finally:
            self.client.close()

    def write_coil(self, address, value, unit) -> bool:
        """
        写单个线圈
        :param address: 开始地址
        :param count: 写入值
        :param unit: 从地址
        @return:
        """
        try:
            logger.info("写单个线圈 address: {}, value: {}, unit: {}".format(address, value, unit))
            self.client.write_coil(address=address, value=value, unit=unit)
            return True
        except ModbusException as e:
            logger.error("发生异常: {}".format(str(e)))
            return False

    def write_coils(self, address, values, unit) -> bool:
        """
        写多个线圈
        :param address: 开始地址
        :param count: 写入值
        :param unit: 从地址
        @return:
        """
        try:
            logger.info("写多个线圈 address: {}, value: {}, unit: {}".format(address, values, unit))
            self.client.write_coils(address=address, values=values, unit=unit)
            return True
        except ModbusException as e:
            logger.error("发生异常: {}".format(str(e)))
            return False

    def write_register(self, address, value, unit) -> bool:
        """
        写单个寄存器
        :param address: 开始地址
        :param count: 写入值
        :param unit: 从地址
        @return:
        """
        try:
            logger.info("写单个寄存器 address: {}, value: {}, unit: {}".format(address, value, unit))
            self.client.write_register(address=address, value=value, unit=unit)
            return True
        except ModbusException as e:
            logger.error("发生异常: {}".format(str(e)))
            return False

    def write_registers(self, address, values, unit) -> bool:
        """
        写多个寄存器
        :param address: 开始地址
        :param count: 写入值
        :param unit: 从地址
        @return:
        """
        try:
            logger.info("写多个寄存器 address: {}, value: {}, unit: {}".format(address, values, unit))
            self.client.write_registers(address=address, values=values, unit=unit)
            return True
        except ModbusException as e:
            logger.error("发生异常: {}".format(str(e)))
            return False
