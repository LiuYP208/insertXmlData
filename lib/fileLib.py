#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os


# 遍历文件夹 返回数组格式的文件
def listDirFiles(dirPath):
    fs = os.listdir(dirPath)
    fileList = []
    for f1 in fs:
        tmp_path = os.path.join(dirPath, f1)
        if not os.path.isdir(tmp_path):
            # print('文件: %s' % tmp_path)
            fileList.append(f1)
    return fileList


def listDirDirs(dirPath):
    fs = os.listdir(dirPath)
    dirList = []
    for f1 in fs:
        tmp_path = os.path.join(dirPath, f1)
        if os.path.isdir(tmp_path):
            # print('文件夹: %s' % tmp_path)
            #排除上下选项
            if f1 == '.' or f1 == '..':
                continue
            dirList.append(f1)
    return dirList
