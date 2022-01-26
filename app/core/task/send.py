# -*- coding: utf-8 -*-
# 任务-发送数据
# 作者: 三石
# 时间: 2021-07-01


import logging
from device import DeviceSettings
from config import ConfigSettings
from core.device import DeviceRead
from core.enums import MsgEnum
from utils import UtilsZabbix


logger = logging.getLogger(__name__)

device_settings = DeviceSettings()
config_settings = ConfigSettings()


def task_send_data():
    """
    任务-发送数据
    :return:
    """
    zabbix = config_settings.zabbix
    zabbix_ip = zabbix.get("ip", "127.0.0.1")
    zabbix_port = zabbix.get("port", 10051)

    zabbix_client = UtilsZabbix(zabbix_ip, zabbix_port)

    devices = device_settings.devices
    logger.debug("所有设备信息: {}".format(devices))

    # 遍历设备数据
    for device in devices:

        device_id = device.get("id")
        device_model = device.get("model")
        device_ipaddress = device.get("ipaddress")
        device_port = device.get("port")
        device_slave = device.get("slave")
        device_sub = device.get("sub")

        # 根据设备类型来调用相应方法
        device_read = DeviceRead()
        device_read_func = getattr(device_read, device_model, None)

        # 判断设备模型是否匹配
        if not device_read_func:

            # 不包含子设备
            if not device_sub:
                payload = MsgEnum.error_model_not_match.value
                zabbix_client.create_payload(host=device_id, payload=payload)

            # 包含子设备
            else:
                for sub in range(device_sub):
                    payload = MsgEnum.error_model_not_match.value
                    zabbix_client.create_payload(host="{}.{}".format(device_id, sub), payload=payload)
        else:

            # 不包含子设备
            if not device_sub:
                payload = device_read_func(ipaddress=device_ipaddress, port=device_port, slave=device_slave)
                zabbix_client.create_payload(host=device_id, payload=payload)

            # 包含子设备
            else:
                payloads = device_read_func(ipaddress=device_ipaddress, port=device_port, slave=device_slave)
                for x, payload in enumerate(payloads):
                    zabbix_client.create_payload(host="{}.{}".format(device_id, x), payload=payload)

    logger.debug("zabbix_sender 发送数据: {}".format(zabbix_client.data))

    # 循环遍历
    for payload in zabbix_client.data:
        packet = zabbix_client.get_packet(data=[payload])
        zabbix_client.send_packet(packet=packet)
