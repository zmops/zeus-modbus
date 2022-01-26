# modbus采集服务
## 框架介绍
**FastApi+pymodbus多进程采集服务**
* Python3.8+

## 功能介绍
**模块**
* api: 定义业务接口
    > 定位对外暴露的接口 默认接口文档: http://127.0.0.1:8029/docs/

* core: 核心功能
    > 定义核心组件

    ###### 组件
    1. device: 设备读取和采集方法
    2. enums: 枚举类
    3. errors: 异常
    4. events: 事件（定时任务开启）
    5. modbus: modbus核心方法
    6. task: 任务 定时采集发送

* files: 文件
    > 管理普通文件

* logs: 日志
    > 保存日志

* utils
    > 工具库

**文件**
* config.py
    > 配置项目参数
  
    ###### zabbix参数
    1. ip: zabbix服务端IP
    2. port: zabbix采集接受端口
    3. interval: 定时采集频率 单位秒
  
* device.py
    > 采集的设备信息

    ###### 设备参数
    1. id: 设备ID zabbix中资源名称 host字段
    2. model: 设备型号 采集服务中已内置的型号方法名称 不匹配则不支持采集
    3. ipaddress: 采集设备上报的modbus服务对应IP
    4. port: 采集设备上报的modbus服务对应端口
    5. slave: 采集设备从地址
    6. sub: 切割子设备

* main.py
    > 主函数 可用来debug

* run_app.py
    > 运行文件 可修改服务端口