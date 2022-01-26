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

    def demurui_air_conditioning_gateway(self, ipaddress, slave, port=502) -> list:
        """
        德姆瑞空调网关(切割子设备)
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

        # 读取子设备未发生异常
        if not payload_controllers.get("error"):

            # 切割8个子设备 重新排序键值
            payload_sub_1 = dict([("key{}".format(int(key[3:]) % 6), payload_controllers[key]) for key in ["key0", "key1", "key2", "key3", "key4", "key5"]])
            payload_sub_2 = dict([("key{}".format(int(key[3:]) % 6), payload_controllers[key]) for key in ["key6", "key7", "key8", "key9", "key10", "key11"]])
            payload_sub_3 = dict([("key{}".format(int(key[3:]) % 6), payload_controllers[key]) for key in ["key12", "key13", "key14", "key15", "key16", "key17"]])
            payload_sub_4 = dict([("key{}".format(int(key[3:]) % 6), payload_controllers[key]) for key in ["key18", "key19", "key20", "key21", "key22", "key23"]])
            payload_sub_5 = dict([("key{}".format(int(key[3:]) % 6), payload_controllers[key]) for key in ["key24", "key25", "key26", "key27", "key28", "key29"]])
            payload_sub_6 = dict([("key{}".format(int(key[3:]) % 6), payload_controllers[key]) for key in ["key30", "key31", "key32", "key33", "key34", "key35"]])
            payload_sub_7 = dict([("key{}".format(int(key[3:]) % 6), payload_controllers[key]) for key in ["key36", "key37", "key38", "key39", "key40", "key41"]])
            payload_sub_8 = dict([("key{}".format(int(key[3:]) % 6), payload_controllers[key]) for key in ["key42", "key43", "key44", "key45", "key46", "key47"]])

        # 读取子设备发生异常
        else:
            payload_sub_1 = payload_controllers
            payload_sub_2 = payload_controllers
            payload_sub_3 = payload_controllers
            payload_sub_4 = payload_controllers
            payload_sub_5 = payload_controllers
            payload_sub_6 = payload_controllers
            payload_sub_7 = payload_controllers
            payload_sub_8 = payload_controllers

        # 组装设备数据 主设备+子设备
        payload = [
            payload_sys,
            payload_sub_1,
            payload_sub_2,
            payload_sub_3,
            payload_sub_4,
            payload_sub_5,
            payload_sub_6,
            payload_sub_7,
            payload_sub_8
        ]
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
