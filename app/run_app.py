#!/usr/bin/env python3
# coding: utf-8


import sys
import subprocess


if __name__ == '__main__':
    subprocess.call('uvicorn main:app --host 0.0.0.0 --port 8029', shell=True,
                    stdin=sys.stdin, stdout=sys.stdout)
