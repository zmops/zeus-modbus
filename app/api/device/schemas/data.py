# -*- coding: utf-8 -*-
# 模式-设备数据
# 作者: 三石
# 时间: 2022-01-21


from pydantic import BaseModel, conint


class SchemaUpdateCurrent(BaseModel):
    """模式-更新当前数据"""

    # 地址
    address: conint(ge=0, le=9999)

    # 最新值
    value: conint(ge=0, le=99)
