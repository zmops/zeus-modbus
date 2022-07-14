#!/usr/bin/env python3
"""
@Project    ：argus-app-console 
@File       ：enums.py 
@Author     ：三石
@Time       ：2022/5/30 10:29
@Annotation : 枚举
"""


from enum import Enum, unique


@unique
class EnumCode(Enum):
    """
    枚举code
    """

    Success = 10000
    Error = 50000

    InvalidError = 61000
    InvalidParam = 61001
    NotFound = 61002
    AlreadyExists = 61003
    PermissionDenied = 61004

    MethodNotSupport = 63000

    UnknownError = 64000
    AuthFailed = 64001
    AuthStatusError = 64003
    UrlNotFound = 64004

    UserNotConfiguredToken = 64005
    ZabbixAPIError = 64006

    KnownError = 65000
    KnownErrorNotExist = 65001


@unique
class EnumMsg(Enum):
    """
    枚举msg
    """

    Success = "请求成功"
    Error = "请求失败"

    InvalidError = "请求参数错误"
    InvalidParam = "请求参数无效"
    NotFound = "数据不存在"
    AlreadyExists = "数据已存在"
    PermissionDenied = "数据权限不足"

    MethodNotSupport = "{}请求方法不支持"

    UnknownError = "服务未知异常,详情查看日志"
    AuthFailed = "认证失败,请重新登录"
    AuthStatusError = "认证状态异常"
    UrlNotFound = "请求url不存在"

    UserNotConfiguredToken = "用户未配置Token"
    ZabbixAPIError = "Zabbix接口服务异常: {}"

    KnownError = "服务异常: {}"
    KnownErrorNotExist = "服务异常: 数据不存在"

    SuccessEnable = "数据启用成功"
    SuccessDisable = "数据禁用成功"
