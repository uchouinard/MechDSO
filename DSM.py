###############################################
#                                             #
# Design Structure Matrix Module              #
#                                             #
#                                             #
# Contrib: uChouinard                         #
#                                             #
#                                             #
###############################################


import numpy as np
import matplotlib.pyplot as plt

class DSM():
    
    def __init__(self, nElems=1, compList={}, dataType='simple'):
        
        if dataType=='simple':
            self.dsm=np.array([[0.]])
        elif dataType=='interactions':
            self.dsm=np.array([[[0., 0. , 0. , 0.]]])
        self.compList=compList
        self.dataType=dataType
    
    
    def addComponent(self, compName):
        
        if not self.compList:
            
            self.compList[compName]=0
            print self.compList
            
        elif compName not in self.compList:
            clen=len(self.compList)
            
            self.compList[compName]=clen
            print self.compList
            
            if self.dataType=='simple':
                tmpDSM=np.zeros((clen+1, clen+1))
            elif self.dataType=='interactions':
                tmpDSM=np.zeros((clen+1, clen+1,4))
            
            tmpDSM[:clen, :clen]=self.dsm
            
            self.dsm=tmpDSM
            
    def addRelation(self, cFrom, cTo, val=1. ):
        
        if cFrom not in self.compList:
            self.addComponent(cFrom)
        if cTo not in self.compList:
            self.addComponent(cTo)
        
        self.dsm[self.compList[cFrom] , self.compList[cTo]]=val
    
    
    def __str__(self):
        
        resStr=' '
         
        cKeys = sorted(self.compList, key=lambda x : self.compList[x])
        for i in cKeys:
            
            resStr+= '\t' + i
        resStr += '\n'
        
        for i in range(len(cKeys)):
            
            resStr+= cKeys[i]
            for j in range(len(cKeys)):
                
                resStr+= '\t'+ str(self.dsm[i,j])
            resStr+='\n'
        return resStr
        
        
      
