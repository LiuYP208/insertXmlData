#!/usr/bin/python
# -*- coding: UTF-8 -*-
# mysql 数据插入


import os
import lib.MysqlDBLib as MysqlDBLib
import lib.fileLib as fileLib
import func.tagsfunc as tagsfunc
import  func.usersfunc as usersfunc



import xml.etree.ElementTree as ET

MYSQL_IP = '********'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = 'shkshk'
MYSQL_CHARSET = 'utf8'


def creat_dict(root):
    """xml生成为dict：，
    将tree中个节点添加到list中，将list转换为字典dict_init
    叠加生成多层字典dict_new"""
    dict_new = {}
    for key, valu in enumerate(root):
        dict_init = {}
        list_init = []
        for item in valu:
            list_init.append([item.tag, item.text])
            for lists in list_init:
                dict_init[lists[0]] = lists[1]
        dict_new[key] = dict_init
    return dict_new





def readDir(dirPath, dbname):
    print 'readDir!'
    print dirPath, dbname
    # 初始化数据库
    conn = MysqlDBLib.getConn(MYSQL_IP, MYSQL_PORT, MYSQL_USER, MYSQL_PWD, dbname, MYSQL_CHARSET)
    Tagsfile = os.path.join(dirPath, 'Tags.xml')
    #tagsfunc.TagsFunc(Tagsfile, dbname, conn)
    # 关闭数据库

    UsersFile= os.path.join(dirPath, 'Users.xml')
    usersfunc.UsersFunc(UsersFile,dbname,conn)
    conn.close()


if __name__ == '__main__':
    filelistpath = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'data');

    print filelistpath
    fileDirList = fileLib.listDirDirs(filelistpath)
    for diritem in fileDirList:
        dbname = diritem.replace('.stackexchange.com', '')
        # dbname = diritemsp[0]
        print dbname
        if dbname == 'sports':
            readDir(os.path.join(filelistpath, diritem), dbname)

    print fileDirList
