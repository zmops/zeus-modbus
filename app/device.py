# -*- coding: utf-8 -*-
# 配置设置
# 作者: 三石
# 时间: 2021-12-10


from pydantic import BaseSettings


class DeviceSettings(BaseSettings):

    plc366: dict = {
        "id": "plc366",
        "model": "napro_300",
        "ipaddress": "172.16.3.66",
        "port": 502,
        "slave": 1,
    }

    hf318: dict = {
        "id": "hf318",
        "model": "jiandarenke_temperature_and_humidity",
        "ipaddress": "172.16.3.18",
        "port": 512,
        "slave": 1,
    }

    air367: dict = {
        "id": "air367",
        "model": "demurui_air_conditioning_gateway",
        "ipaddress": "172.16.3.67",
        "port": 502,
        "slave": 1,
        "sub": 8
    }

    devices: list = [
        plc366,
        hf318,
        air367,
    ]
