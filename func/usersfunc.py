# !/usr/bin/python
# coding: UTF-8
# mysql 数据插入 Tags

import sys

reload(sys)

sys.setdefaultencoding('utf-8')
import os
import xmltodict
import MySQLdb
import lib.MysqlDBLib as MysqlDBLib


def UsersFunc(filename, dbname, conn):
    sqlList = []
    tablename = 'Users'
    print filename
    with open(filename) as fd:
        doc = xmltodict.parse(fd.read())
        rows = doc['users']['row']
        for row in rows:
            # print row
            Id = 'null'
            Reputation = 'null'
            CreationDate = 'null'
            DisplayName = 'null'
            LastAccessDate = 'null'
            WebsiteUrl = 'null'
            Location = 'null'
            AboutMe = 'null'
            Views = 'null'
            UpVotes = 'null'
            DownVotes = 'null'
            AccountId = 'null'

            for i in row:
                # print i
                if i == '@Id':
                    Id = row['@Id']
                if i == '@Reputation':
                    Reputation = row['@Reputation']
                if i == '@CreationDate':
                    CreationDate = row['@CreationDate']
                if i == '@DisplayName':
                    DisplayName = row['@DisplayName']
                if i == '@LastAccessDate':
                    LastAccessDate = row['@LastAccessDate']

                if i == '@WebsiteUrl':
                    WebsiteUrl = row['@WebsiteUrl']
                if i == '@Location':
                    Location = row['@Location']
                if i == '@AboutMe':
                    AboutMe = row['@AboutMe']
                if i == '@Views':
                    Views = row['@Views']

                if i == '@UpVotes':
                    UpVotes = row['@UpVotes']
                if i == '@DownVotes':
                    DownVotes = row['@DownVotes']
                if i == '@AccountId':
                    AccountId = row['@AccountId']
            AboutMe = MySQLdb.escape_string(AboutMe)
            sqlstr = "INSERT INTO %s (Id, Reputation, CreationDate, DisplayName, LastAccessDate, WebsiteUrl, Location, AboutMe,Views, UpVotes, DownVotes, AccountId) VALUES (%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                tablename, Id, Reputation, CreationDate, DisplayName, LastAccessDate, WebsiteUrl, Location, AboutMe,
                Views, UpVotes, DownVotes, AccountId)
            sqlList.append(sqlstr)
    sqlPath = os.path.join(dbname + '_Users.sql')
    print 'sqlPath'
    print sqlPath
    writeresult = file(sqlPath, 'a+')
    for sql in sqlList:
        print sql
        writeresult.write(sql + ';\n')
        # MysqlDBLib.execSQL(conn, sql + ';\n')
    writeresult.close()
    return sqlList
