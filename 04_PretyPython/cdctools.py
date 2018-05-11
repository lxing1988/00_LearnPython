#!/usr/bin/env python3

# encoding: utf-8  

""" 
@version: v1.0 
@author: Bruce Long 
@license: Apache Licence  
@contact: lxing_1988@sina.com 
@site:  
@software: PyCharm 
@file: cdctools.py.py 
@time: 5/10/18 10:52 PM 
"""

import os

def cdWalker(cdrom, cdcfile):
    export = ""
    for root, dirs, files in os.walk(cdrom):
        export+="\n %s;%s;%s" % (root,dirs,files)
    open(cdcfile,'w').write(export)

if __name__ == "__main__":
    CDROM='/eda02_4T/00-Tools_docs'
    cdWalker(CDROM,'./books.cdc')