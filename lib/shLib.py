#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess as sp


# 调用标准sh
def execSHStr(shStr):
    print shStr
    sp.call(shStr, shell = True)
    return 0
