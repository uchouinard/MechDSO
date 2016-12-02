###############################################
#                                             #
# Design Structure Matrix Module              #
#                                             #
#                                             #
# Contrib: uChouinard                         #
# V0 2/12/2016                                #
#                                             #
###############################################


import numpy as np
import matplotlib.pyplot as plt
import pandas as pds


class DesignSM():
    
    
    def __init__(self, name):
        
        
        self.name=name
        self.compList= {}
        self.dsm= np.empty([0,0])
        print self.dsm
        
    
    
    def addComponent(self, cName):
        self.compList[cName]=len(self.compList.keys())

        if len(self.compList.keys())==1:
            self.dsm=np.zeros([1,1])
        else:
            self.dsm=np.append(self.dsm, np.zeros([self.dsm.shape[1], 1]).T, axis=0)           
            self.dsm=np.append(self.dsm, np.zeros([self.dsm.shape[0], 1]), axis=1)

    def addRelation(self, cNameFrom, cNameTo, val=1):
        
        if not(cNameFrom in self.compList):
            self.addComponent(cNameFrom)
        if not(cNameTo in self.compList):
            self.addComponent(cNameTo)
        
        self.dsm[self.compList[cNameFrom], self.compList[cNameTo] ]=val
        
    
    
    def display(self):
        print self.dsm
        #print self.compList
        
      
