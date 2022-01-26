# -*- coding: utf-8 -*-
# 测试用例-api
# 作者: 三石
# 时间: 2021-12-10


import unittest
from main import app
from device import DeviceSettings
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED, HTTP_422_UNPROCESSABLE_ENTITY
from core.enums import CodeEnum, MsgEnum
from core.device import DeviceRead


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def tearDown(self) -> None:
        self.client = None

    def test_device_info_query_device(self):
        """查询设备信息"""
        response = self.client.get("/api/device/info/query_device/")
        status_code = response.status_code
        response_json = response.json()

        self.assertEqual(status_code, HTTP_200_OK)

        success = response_json.get("success")
        code = response_json.get("code")
        msg = response_json.get("msg")
        data = response_json.get("data")
        device_settings = DeviceSettings()

        self.assertEqual(success, True)
        self.assertEqual(code, CodeEnum.success.value)
        self.assertEqual(msg, MsgEnum.success.value)
        self.assertEqual(data, device_settings.devices)

    def test_device_info_query_model(self):
        """查询型号信息"""
        response = self.client.get("/api/device/info/query_model/")
        status_code = response.status_code
        response_json = response.json()

        self.assertEqual(status_code, HTTP_200_OK)

        success = response_json.get("success")
        code = response_json.get("code")
        msg = response_json.get("msg")
        data = response_json.get("data")
        device_read = DeviceRead()

        self.assertEqual(success, True)
        self.assertEqual(code, CodeEnum.success.value)
        self.assertEqual(msg, MsgEnum.success.value)
        self.assertEqual(data, device_read.support_models)

    def test_device_data_query_current_normal(self):
        """查询设备当前数据-正常"""
        response = self.client.get("/api/device/data/query_current/hf318/")
        status_code = response.status_code
        response_json = response.json()

        self.assertEqual(status_code, HTTP_200_OK)

        success = response_json.get("success")
        code = response_json.get("code")
        msg = response_json.get("msg")
        data = response_json.get("data")

        self.assertEqual(success, True)
        self.assertEqual(code, CodeEnum.success.value)
        self.assertEqual(msg, MsgEnum.success.value)
        self.assertIn("key0", data.keys())
        self.assertIn("key1", data.keys())

    def test_device_data_query_current_deviceNotFound(self):
        """查询设备当前数据-设备不存在"""
        response = self.client.get("/api/device/data/query_current/xx/")
        status_code = response.status_code
        response_json = response.json()

        self.assertEqual(status_code, HTTP_200_OK)

        success = response_json.get("success")
        code = response_json.get("code")
        msg = response_json.get("msg")

        self.assertEqual(success, False)
        self.assertEqual(code, CodeEnum.error.value)
        self.assertEqual(msg, MsgEnum.error_device_not_found.value)

    def test_device_data_update_current_normal(self):
        """修改设备当前数据-正常"""
        response = self.client.post("/api/device/data/update_current/hf318/", json={
            "address": 4001,
            "value": 1
        })
        status_code = response.status_code
        response_json = response.json()

        self.assertEqual(status_code, HTTP_200_OK)

        success = response_json.get("success")
        code = response_json.get("code")
        msg = response_json.get("msg")

        self.assertEqual(success, True)
        self.assertEqual(code, CodeEnum.success.value)
        self.assertEqual(msg, MsgEnum.success.value)

    def test_device_data_update_current_deviceNotFound(self):
        """修改设备当前数据-设备不存在"""
        response = self.client.post("/api/device/data/update_current/xx/", json={
            "address": 4001,
            "value": 1
        })
        status_code = response.status_code
        response_json = response.json()

        self.assertEqual(status_code, HTTP_200_OK)

        success = response_json.get("success")
        code = response_json.get("code")
        msg = response_json.get("msg")

        self.assertEqual(success, False)
        self.assertEqual(code, CodeEnum.error.value)
        self.assertEqual(msg, MsgEnum.error_device_not_found.value)

    def test_device_data_update_current_getNotSupport(self):
        """修改设备当前数据-get不支持"""
        response = self.client.get("/api/device/data/update_current/xx/")
        status_code = response.status_code
        response_json = response.json()

        self.assertEqual(status_code, HTTP_405_METHOD_NOT_ALLOWED)

        success = response_json.get("success")
        code = response_json.get("code")
        errors = response_json.get("errors")

        self.assertEqual(success, False)
        self.assertEqual(code, HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(errors, ["Method Not Allowed"])

    def test_device_data_update_current_bodyIncomplete(self):
        """修改设备当前数据-参数不完整"""
        response = self.client.post("/api/device/data/update_current/hf318/")
        status_code = response.status_code
        response_json = response.json()

        self.assertEqual(status_code, HTTP_422_UNPROCESSABLE_ENTITY)

        success = response_json.get("success")
        code = response_json.get("code")
        errors = response_json.get("errors")

        self.assertEqual(success, False)
        self.assertEqual(code, HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(errors, [{"loc": ["body"], "msg": "field required", "type": "value_error.missing"}])
