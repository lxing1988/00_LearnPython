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
from vlogModule import *


class parseVerdiLog():
    def __init__(self, flogname):
        self.fname = flogname
        self.modules = []
        try:
            self.logFH = open(flogname, 'r')
        except IOError:
            raise AssertionError("File <%s> IO access Error!" % self.fname)
    
    def getLogInfo(self):
        return self.logFH
    
    def closeFH(self):
        if self.logFH:
            self.logFH.close()
    
    def getModulesInfo(self):
        modNamePat = re.compile(r'^\s*Module:\s+.+\((\w+)\)\s*$')
        pinInfoPat = re.compile(r'^\s+(\d+)\)\s+(\w+)\s*:\s+(\w+)\s+\(Size:\s+(\d+)\)\s*$')
        blankPat   = re.compile(r'^\s*$')
        foundNewModule = False
        foundNewPin = False
        modref = None
        for line in self.getLogInfo():
            modNameMatch   = modNamePat.match(line)
            pinInfoMatch   = pinInfoPat.match(line)
            blankLineMatch = blankPat.match(line)
            
            if blankLineMatch:
                continue
            
            if modNameMatch:
                if foundNewPin:
                    modref.showModuleInfo()
                    self.modules.append(modref)
                modref = None
                moduleName = modNameMatch.group(1)
                modref = moduleInfo(moduleName)
                foundNewModule = True
                foundNewPin = False
                continue
            
            if pinInfoMatch:
                foundNewModule = False
                foundNewPin = True
                id = pinInfoMatch.group(1)
                dirc = pinInfoMatch.group(2)
                name = pinInfoMatch.group(3)
                size = pinInfoMatch.group(4)
                modref.pushPinInfo(id, dirc, name, size)
                continue
        # push the last found submodule
        if foundNewPin:
            self.modules.append(modref)
        self.closeFH()


if __name__ == "__main__":
    get = parseVerdiLog('./getModIO.log')
    # info = get.getLogInfo()
    get.getModulesInfo()
