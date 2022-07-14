#!/usr/bin/env python3
"""
@Project    ：zeus-modbus 
@File       ：log.py 
@Author     ：三石
@Time       ：2022/7/14 10:46
@Annotation : 日志模块
"""

import os

# 找到上级路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_LOG_DIR = os.path.join(BASE_DIR, "logs")

# 初始化文件夹
if not os.path.exists(BASE_LOG_DIR):
    os.makedirs(BASE_LOG_DIR)


LogConfig = {
    'version': 1,  # 保留的参数，默认是1
    'disable_existing_loggers': False,  # 是否禁用已经存在的logger实例
    # 日志输出格式的定义
    'formatters': {
        'standard': {  # 标准的日志格式化
            'format': '[%(levelname)s] [%(asctime)s] [%(module)s] -- %(message)s'
        },
        'error': {     # 错误日志输出格式
            'format': '[%(levelname)s] [%(asctime)s] [%(pathname)s] [%(module)s] -- %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] [%(asctime)s] -- %(message)s'
        },
        'collect': {
            'format': '%(message)s'
        }
    },
    # 处理器：需要处理什么级别的日志及如何处理
    'handlers': {
        # 将日志打印到终端
        'console': {
            'level': 'DEBUG',                  # 日志级别
            'class': 'logging.StreamHandler',  # 使用什么类去处理日志流
            'formatter': 'simple'              # 指定上面定义过的一种日志输出格式
        },
        # 默认日志处理器
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "default.log"),  # 日志文件路径
            'when': 'D',
            'interval': 1,
            'backupCount': 7,  # 日志文件备份的数量
            'formatter': 'standard',  # 日志输出格式
            'encoding': 'utf-8',
        },
        # Error日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "error.log"),  # 日志文件路径
            'when': 'D',
            'interval': 1,
            'backupCount': 7,  # 日志文件备份的数量
            'formatter': 'error',  # 日志格式
            'encoding': 'utf-8',
        },
    },

    'loggers': {
        # 默认的logger应用如下配置
        '': {
            'handlers': ['console', 'default', 'error'],
            'level': 'DEBUG',
            'propagate': True,  # 如果有父级的logger示例，表示不要向上传递日志流
        },
        'collect': {
            'handlers': ['default', 'error'],
            'level': 'INFO',
        }
    },
}
