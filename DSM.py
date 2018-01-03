###############################################
#                                             #
# Design Structure Matrix Module              #
#                                             #
# simple module for creating and managing DSM #
# Contrib: uChouinard                         #
# V0 2/12/2016                                #
#                                             #
###############################################

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
#import warnings
import pandas as pds



        
class DSM():
    
    def __init__(self, name='none', dsmType='simple', directed='yes'):
        
        
        self.name=name
        self.complist=[]
        if directed is 'yes':
            if dsmType is 'simple':
                self.dsm=nx.DiGraph()
            elif dsmType is 'interactions':
                self.dsm={'s':nx.DiGraph(),'i': nx.DiGraph(),
                      'e':nx.DiGraph(), 'm':nx.DiGraph()}
            elif dsmType is 'dependencies':
                self.dsm={'v':nx.DiGraph(),'h': nx.DiGraph(),
                      'e':nx.DiGraph()}
        else:
            if dsmType is 'simple':
                self.dsm=nx.Graph()
            elif dsmType is 'interactions':
                self.dsm={'s':nx.Graph(),'i': nx.Graph(),
                      'e':nx.Graph(), 'm':nx.Graph()}
            elif dsmType is 'dependencies':
                self.dsm={'v':nx.Graph(),'h': nx.Graph(),
                      'e':nx.Graph()}
        
        self.dsmType=dsmType
       
    
    def addComponent(self, cName):
        
        for name in cName:
            self.complist.append(name)
        
            if self.dsmType=='simple':
                self.dsm.add_node(name)
            
            
            elif self.dsmType=='interactions':
                for keys in self.dsm:
                    self.dsm[keys].add_node(name)
            elif self.dsmType=='dependencies':
                for keys in self.dsm:
                    self.dsm[keys].add_node(name) 
        
    def addRelation(self, cNameFrom, cNameTo, val):
        
        if len(cNameFrom) == len(cNameTo):
            for i in range(len(cNameFrom)):
                if not(cNameFrom[i] in self.complist):
                    self.addComponent([cNameFrom[i]])
            
                if not(cNameTo[i] in self.complist):
                    self.addComponent([cNameTo[i]])
                
            
                if self.dsmType=='simple':
            #if type(val) is float:
                    self.dsm.add_edge(cNameFrom[i], cNameTo[i], weight=val[i])
            #else :
            #    warnings.warn('non valid input value')
        
                if self.dsmType== 'interactions':
            #if type(val) is interactions:
                    for keys in val[i]:
                        self.dsm[keys].add_edge(cNameFrom[i], cNameTo[i], weight=val[i][keys])
                if self.dsmType== 'dependencies':
            #if type(val) is dependencies:
                    for keys in val[i]:
                        self.dsm[keys].add_edge(cNameFrom[i], cNameTo[i], weight=val[i][keys])
        
    
    def display(self):
        if self.dsmType == 'simple':
            
            print nx.to_numpy_matrix(self.dsm, nodelist=self.complist)
        
        elif self.dsmType == 'interactions':
            
            for keys in ['s','e','i','m']:
                print keys
                print nx.to_numpy_matrix(self.dsm[keys], nodelist=self.complist)  
                
        elif self.dsmType == 'dependencies':
            
            for keys in ['v','h','e']:
                print keys
                print nx.to_numpy_matrix(self.dsm[keys], nodelist=self.complist)    
                
    def dispPDFrame(self):
        
        if self.dsmType == 'simple':
            df=pds.DataFrame(data=nx.to_numpy_matrix(self.dsm, nodelist=self.complist), columns=self.complist, index=self.complist)
              
        
        if self.dsmType == 'interactions':
            
            x,y = len(self.complist),len(self.complist)
            A = [ ['']*x for i in range(y) ]
            k=0
            for keys in ['s','e','i','m']:
                myGmat=nx.to_numpy_matrix(self.dsm[keys], nodelist=self.complist)  
                for i in range (x):
                    for j in range(y):
                        #print myGmat[i,j]
                        A[i][j]=A[i][j]+str(myGmat[i,j])+'/  '
                        #if k ==1:
                        #    A[i][j]=A[i][j]+'\n'
                        
                        # if '0.0 0.0 0.0 0.0' in A[i][j]:
                        #    A[i][j]=''
                        k+=1        
            df=pds.DataFrame(data=A, columns=self.complist, index=self.complist)
            
        if self.dsmType == 'dependencies':
            
            x,y = len(self.complist),len(self.complist)
            A = [ ['']*x for i in range(y) ]
            k=0
            for keys in ['v','h', 'e']:
                myGmat=nx.to_numpy_matrix(self.dsm[keys], nodelist=self.complist)  
                for i in range (x):
                    for j in range(y):
                        #print myGmat[i,j]
                        A[i][j]=A[i][j]+str(myGmat[i,j])+'/  '
                        #if k ==1:
                        #    A[i][j]=A[i][j]+'\n'
                        
                        if 'nan' in A[i][j]:
                            A[i][j]=''
                        k+=1        
            df=pds.DataFrame(data=A, columns=self.complist, index=self.complist)
        return df

        

        
        
      
