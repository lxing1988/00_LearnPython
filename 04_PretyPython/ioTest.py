#!/usr/bin/env python3

# encoding: utf-8  

""" 
@version: v1.0 
@author: Bruce Long 
@license: Apache Licence  
@contact: lxing_1988@sina.com 
@site:  
@software: PyCharm 
@file: ioTest.py.py 
@time: 5/11/18 8:24 PM 
"""


class openfile():
    def __init__(self):
        pass
    
    def open(self, fname):
        return open(fname,'r')


if __name__ == "__main__":
    of = openfile()
    fh = of.open('./books.cdc')
    print(list(fh))