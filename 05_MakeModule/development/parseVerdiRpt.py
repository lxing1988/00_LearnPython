#!/usr/bin/env python3

# encoding: utf-8  

""" 
@version: v1.0 
@author: Bruce Long 
@license: Apache Licence  
@contact: lxing_1988@sina.com 
@site:  
@software: PyCharm 
@file: parseVerdiRpt.py 
@time: 5/11/18 9:34 PM 
"""
import os
import re


class parseVerdiLog():
    def __init__(self, flogname):
        self.fname = flogname
        try:
            self.logFH = open(flogname, 'r')
        except IOError:
            raise AssertionError("File <%s> IO access Error!" % self.fname)
    
    def getLogInfo(self):
        return self.logFH
    
    def closeFH(self):
        if self.logFH:
            self.logFH.close()

    def getModuleName(self):
        for line in self.getLogInfo():
            modNamePat = re.compile(r'Module:\s+.+\((\w+)\)\s*$')
            pinInfoPat = re.compile(r'^\s+(\d+)\)\s+(\w+)\s+:\s+(\w+)\s+\(Size:\s+(\d+)\)\s*$')
            modNameMatch = modNamePat.match(line)
            pinInfoMatch = pinInfoPat.match(line)
            #if modNameMatch:
            #    print(modNameMatch.group(1))
            if pinInfoMatch:
                print(pinInfoMatch.group(1) + pinInfoMatch.group(2) + pinInfoMatch.group(3) + pinInfoMatch.group(4))
            
            
    


if __name__ == "__main__":
    get = parseVerdiLog('./getModIO.log')
    #info = get.getLogInfo()
    get.getModuleName()
        