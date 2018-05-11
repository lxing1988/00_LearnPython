#!/usr/bin/env python3

# encoding: utf-8  

""" 
@version: v1.0 
@author: Bruce Long 
@license: Apache Licence  
@contact: lxing_1988@sina.com 
@site:  
@software: PyCharm 
@file: vlogModule.py 
@time: 5/11/18 11:21 PM 
"""


class moduleInfo():
    def __init__(self, moduleName):
        self.moduleName = moduleName
        self.pinsInfo = []
    
    def pushPinInfo(self, id, pinDirection, pinName, pinWidth):
        pinInfo = {'id':id,
                   'pinDirection':pinDirection,
                   'pinName':pinName,
                   'pinWidth':pinWidth}
        #print("Push a new pin")
        self.pinsInfo.append(pinInfo)
    
    def showModuleInfo(self):
        print("Module Name : %s" % self.moduleName)
        for mod in self.pinsInfo:
            print("%4d - %16s - %16s - %4d" % (int(mod['id']), mod['pinDirection'], mod['pinName'], int(mod['pinWidth'])))
            #print("Direction : %s" % mod['pinDirection'])
            #print("pinName : %s" % mod['pinName'])
            #print("pinWidth : %d" % int(mod['pinWidth']))

if __name__ == "__main__":
    mod = moduleInfo("Test")
    for id in range(10):
        mod.pushPinInfo(id, 'input', ('tst' + str(id)), id)
    mod.showModuleInfo()