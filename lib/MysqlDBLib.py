#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


def getConn(host, port, user, pwd, db, charset):
    print host, port, user, pwd, db, charset
    conn = MySQLdb.connect(host=host, user=user, passwd=pwd, db=db, port=port, charset=charset)
    return conn


def execSQL(conn, sqlstr):
    cur = conn.cursor()
    cur.execute(sqlstr)
    conn.commit()
    lines = cur.fetchall()
    return lines;
