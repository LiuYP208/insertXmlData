#!/usr/bin/python

# -*- coding: UTF-8 -*-


import os
import ftplib
import re
import time


class ExFTP(object):
    def __init__(self, host, port, username, password):
        try:
            self.host = host
            self.port = int(port)
            self.username = username
            self.password = password
            self.timeout = 1000
            self.is_dir = False
            self.ftp_dir_name = ''
            self.ftp = ftplib.FTP()
            self.login()  # creat connection
        except:
            print "params error!"

    def login(self):
        try:
            print "host = %s,    user = %s,    password = %s " % (self.host, self.username, self.password)
            self.ftp.connect(self.host, self.port, self.timeout)
            self.ftp.login(self.username, self.password)
            print self.ftp.getwelcome()
        except Exception as e:
            print "hostname error! %s" % e
            exit(-1)

    def colse(self):
        self.ftp.close()

    def ftp_list(self, line):
        list = line.split(' ')
        if self.ftp_dir_name == list[-1] and list[0].startswith('d'):
            self.is_dir = True

    def is_ftp_dir(self, remotedir):
        ftp_path = remotedir.rstrip("/")
        ftp_parent_path = os.path.dirname(ftp_path)

        self.is_dir = False
        if ftp_path == '.' or ftp_path == './' or ftp_path == '':
            self.is_dir = True
        else:
            try:
                self.ftp.retrlines("LIST &s" % ftp_parent_path)
            except ftplib.error_perm:
                return self.is_dir

        return self.is_dir

    def list_dir(self, remotedir):
        try:
            self.ftp.cwd(remotedir)
            fileList = self.ftp.nlst()
            return fileList
        except:
            print "remote dir not exist!"

    def list_dir_reg(self, remotedir, pattern):
        try:
            self.ftp.cwd(remotedir)
            fileList = self.ftp.nlst()

            p = re.compile(pattern)
            matchedFiles = []
            for file in fileList:
                match = p.search(file)
                if match:
                    matchedFiles.append(match.string)

            return matchedFiles
        except:
            print "remote dir not exist!"

    def get_file(self, remotefile, localPath, block_size=512 * 1024):
        try:
            localfile = os.path.join(localPath, os.path.basename(remotefile))
            # localfileOK = localfile + '.OK'

            if not os.path.exists(localfile):
                with open(localfile, "wb") as fp:
                    self.ftp.retrbinary('RETR %s' % remotefile, fp.write, block_size)
                # with open(localfileOK,'w') as p:
                #     p.write('')
                print "%s ---- Download '%s' completed!" % (
                    time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()), os.path.basename(remotefile))
            else:
                print "%s ---- file  " + localfile + "' exist !"
        except ftplib.error_perm:
            print "get file error!"

    def get_dir(self, remotedir, localpath):
        remoteFileList = self.list_dir(remotedir)
        for remotefile in remoteFileList:
            self.get_file(remotefile, localpath)

    def get_dir_reg(self, remotedir, localpath, pattern):
        remoteFileList = self.list_dir_reg(remotedir, pattern)
        for remotefile in remoteFileList:
            self.get_file(remotefile, localpath)

    def put_file(self, localfile, remotePath, block_size=512 * 1024):
        filename = os.path.basename(localfile)
        remotefile = os.path.join(remotePath, filename)
        with open(localfile, 'rb') as fp:
            self.ftp.storbinary("STOR %s" % remotefile, fp, block_size)
            print "%s ---- Upload '%s' completed!" % (
                time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()), os.path.basename(remotefile))

    def put_dir(self, localpath, ftp_path='.', begin=True):
        ftp_path = ftp_path.rstrip("/")
        if os.path.isdir(localpath):
            if begin:
                if not self.is_ftp_dir(ftp_path):
                    self.ftp.mkd(ftp_path)

                ftp_path = os.path.join(ftp_path, os.path.basename(localpath))

            if not self.is_ftp_dir(ftp_path):
                self.ftp.mkd(ftp_path)

            os.chdir(localpath)
            localfiles = os.listdir(".")
            for file in localfiles:
                if os.path.isdir(file):
                    ftp_path = os.path.join(ftp_path, file)
                    self.put_dir(file, ftp_path, False)
                else:
                    self.put_file(file, ftp_path)
