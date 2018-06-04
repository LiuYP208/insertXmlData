# !/usr/bin/python
# -*- coding: UTF-8 -*-
# mysql 数据插入 Tags

import os
import xmltodict
import lib.MysqlDBLib as MysqlDBLib


def TagsFunc(filename, dbname, conn):
    sqlList = []
    tablename = 'Tags'
    print filename
    with open(filename) as fd:
        doc = xmltodict.parse(fd.read())
        rows = doc['tags']['row']
        for row in rows:
            # print row
            Id, TagName, Count, ExcerptPostId, WikiPostId = '', '', '', 'null', 'null'
            for i in row:
                # print i
                if i == '@Id':
                    Id = row['@Id']
                if i == '@TagName':
                    TagName = row['@TagName']
                if i == '@Count':
                    Count = row['@Count']
                if i == '@ExcerptPostId':
                    ExcerptPostId = row['@ExcerptPostId']
                if i == '@WikiPostId':
                    WikiPostId = row['@WikiPostId']
            sqlstr = 'INSERT INTO %s (Id,TagName,Count,ExcerptPostId,WikiPostId) VALUES (%s,"%s",%s,%s,%s)' % (
                tablename, Id, TagName, Count, ExcerptPostId, WikiPostId)
            sqlList.append(sqlstr)
    sqlPath = os.path.join(dbname + '_Tags.sql')
    print 'sqlPath'
    print sqlPath
    writeresult = file(sqlPath, 'a+')
    for sql in sqlList:
        print sql
        writeresult.write(sql + ';\n')
        MysqlDBLib.execSQL(conn, sql + ';\n')
    writeresult.close()
    return sqlList
