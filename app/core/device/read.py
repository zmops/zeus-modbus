# -*- coding: utf-8 -*-
# 设备读取
# 作者: 三石
# 时间: 2021-07-01


import logging
from core.modbus import ModbusClient


logger = logging.getLogger(__name__)


class DeviceRead(object):

    def __init__(self):
        """
        设备读取
        """
        self.logger = logger

    def jiandarenke_temperature_and_humidity(self, ipaddress, slave, port=502) -> dict:
        """
        建大仁科温湿度
        :param ipaddress: 设备IP地址
        :param slave: 从地址
        :param port: 设备端口 默认502
        :return:
        """
        self.logger.info("读取 建大仁科温湿度, ipaddress: {}, port: {}".format(ipaddress, port))
        modbus = ModbusClient(ipaddress=ipaddress, port=port)
        payload = modbus.read_holding_registers(address=0, count=2, unit=slave)
        modbus.close_client()
        return payload

    def napro_300(self, ipaddress, slave, port=502) -> dict:
        """
        NAPro 300
        :param ipaddress: 设备IP地址
        :param slave: 从地址
        :param port: 设备端口 默认502
        :return:
        """
        self.logger.info("读取 NAPro 300, ipaddress: {}, port: {}".format(ipaddress, port))
        modbus = ModbusClient(ipaddress=ipaddress, port=port)
        payload_s_1 = modbus.read_discrete_inputs(address=10000, count=151, unit=slave)
        payload_s_2 = modbus.read_discrete_inputs(address=10510, count=21, unit=slave)
        payload_sw_1 = modbus.read_input_registers(address=5000, count=41, unit=slave)
        payload_sw_2 = modbus.read_input_registers(address=5510, count=21, unit=slave)
        modbus.close_client()
        payload = {**payload_sw_1, **payload_sw_2, **payload_s_1, **payload_s_2}
        return payload

    def demurui_air_conditioning_gateway(self, ipaddress, slave, port=502) -> dict:
        """
        德姆瑞空调网关
        :param ipaddress: 设备IP地址
        :param slave: 从地址
        :param port: 设备端口 默认502
        :return:
        """
        self.logger.info("读取 德姆瑞空调网关, ipaddress: {}, port: {}".format(ipaddress, port))
        modbus = ModbusClient(ipaddress=ipaddress, port=port)
        payload_sys = modbus.read_holding_registers(address=2000, count=5, unit=slave)
        payload_controllers = modbus.read_holding_registers(address=0, count=48, unit=slave)
        modbus.close_client()
        payload = {**payload_sys, **payload_controllers}
        return payload

    @property
    def support_models(self) -> list:
        """
        支持的类型
        :return:
        """

        models = list(
            filter(
                # 筛除 以__开头, 以__结尾, logger 和 当前本身
                lambda m: not m.startswith("__") and not m.endswith("__") and m not in ["logger", "support_models"],
                dir(self)
            )
        )

        return models
