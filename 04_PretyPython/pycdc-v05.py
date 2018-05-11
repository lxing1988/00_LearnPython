#!/usr/bin/env python3

# encoding: utf-8  

""" 
@version: v1.0 
@author: Bruce Long 
@license: Apache Licence  
@contact: lxing_1988@sina.com 
@site:  
@software: PyCharm 
@file: pycdc-v05.py 
@time: 5/10/18 10:59 PM 
"""

import sys, cmd
from cdctools import *


class PyCDC(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.CDROM = '/eda02_4T/00-Tools_docs'
        self.CDDIR = './'
        self.prompt = "(PyCDC>)"
        self.intro = '''
                        User Guilde
            dir  : dir name
            walk : wald name
            find : char
            ?    : search
            EOF  : exit system
        '''
    
    def help_EOF(self):
        print("exit system")
    
    def do_EOF(self):
        sys.exit()
    
    def help_walk(self):
        print("Scan CD")
    
    def do_walk(self, filename):
        if filename == "":
            filename = input("input file name: ")
        print("scan CDROM : %s" % filename)
        cdWalker(self.CDROM, self.CDDIR + filename)
    
    def help_dir(self):
        print("define save file")
    
    def do_dir(self, pathname):
        if pathname == "":
            pathname = input("search path: ")
        self.CDDIR = pathname
        print("search path:%s" % pathname)
    
    def help_find(self):
        print("define search char")
    
    def do_find(self, keyword):
        if keyword == "":
            keyword = input("define search char: ")
        print("define search char %s" % keyword)


if __name__ == '__main__':
    cdc = PyCDC()
    cdc.cmdloop()
