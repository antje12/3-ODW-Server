#!/usr/bin/env python
from __future__ import print_function, absolute_import, division

import logging
import mysql.connector

from errno import ENOENT
from stat import S_IFDIR, S_IFREG
from time import time

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn, fuse_get_context


class Context(LoggingMixIn, Operations):
    'Example filesystem to demonstrate fuse_get_context()'

    def getattr(self, path, fh=None):
        if path == "/":
            st = dict(st_mode=(S_IFDIR | 0o755), st_nlink=2)
        else:
            filename = path[1:] # Remove leading /
        
         # TODO: If filename does not exist, raise exception: raise FuseOSError(ENOENT)
         # If file exists, set: st = dict(st_mode=(S_IFREG | 0o755), st_size=filesize)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT filesize FROM File where filename = '" + filename + "'")
        myresult = mycursor.fetchone()

        st = dict(st_mode=(S_IFREG | 0o755), st_size=myresult)

        st['st_ctime'] = st['st_mtime'] = st['st_atime'] = time()
        return st

    def read(self, path, size, offset, fh):

        def encoded(x):
            return ('%s\n' % x).encode('utf-8')        

        filename = path[1:]

        mycursor = mydb.cursor()
        mycursor.execute("SELECT filecontent FROM File where filename = " + filename)
        myresult = mycursor.fetchone()

        return myresult

        # TODO: if filename does not exist, raise: raise FuseOSError(ENOENT)
        # If filename exists, return file content

    def readdir(self, path, fh):
        Files = []
        # TODO: Files should contain list of filenames in directory.

        mycursor = mydb.cursor()
        mycursor.execute("SELECT filename FROM File")
        myresult = mycursor.fetchall()

        for fn in myresult:
            Files.append(fn)

        return ['.', '..'] + Files

    # Disable unused operations:
    access = None
    flush = None
    getxattr = None
    listxattr = None
    open = None
    opendir = None
    release = None
    releasedir = None
    statfs = None


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('mount')
    args = parser.parse_args()

    # TODO: Establish mysql connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fileSystemDB")

    logging.basicConfig(level=logging.WARNING)
    fuse = FUSE(
        Context(), args.mount, foreground=True, ro=True, allow_other=True)
