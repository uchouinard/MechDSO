import DSM as dsmx
import random as rnd
import copy

def example1():
    myDSM=dsmx.DSM('example')


    ## adding components
    myDSM.addComponent(['c1'])
    myDSM.addComponent(['c2'])
    myDSM.addComponent(['c3'])

    # 
    myDSM.display()

    print "--------"

    ## adding relations between existing components

    myDSM.addRelation(['c1'], ['c2'], [1])
    myDSM.addRelation(['c3'], ['c1'], [1])
    myDSM.addRelation(['c2'], ['c3'], [1])
    
    myDSM.display()
    print "--------"


    ## adding relations with non existing elements

    myDSM.addRelation(['c4'], ['c5'], [1.0])
    myDSM.display()

    #using pandas for better visualisation
    myDSM.dispPDFrame()
    
    
def example2():
    ### simple examples un-directional dsm
    myDSMU=dsmx.DSM('example undirectional','simple','no')


    ## adding components
    
    myDSMU.addComponent(['c1'])
    myDSMU.addComponent(['c2'])
    myDSMU.addComponent(['c3'])

    # 
    myDSMU.display()

    print "--------"

    ## adding relations between existing components

    myDSMU.addRelation(['c1'], ['c2'], [1])
    myDSMU.addRelation(['c3'], ['c1'], [1])
    myDSMU.addRelation(['c2'], ['c3'], [1])

    myDSMU.display()
    print "--------"


    ## adding relations with non existing elements

    myDSMU.addRelation(['c4'], ['c5'], [1.0])

    myDSMU.display()


def example3():
    ### simple examples for array inputs
    myDSM=dsmx.DSM('example array')
    
    #print 'creating a list of elements'
    myList=list(range(0,10))
    #print myList


    ## adding components
    myDSM.addComponent(myList)
    
    #print 'creating two shuffled list'
    rnd.shuffle(myList)
    myList1=copy.copy(myList)
    
    rnd.shuffle(myList)
    myList2=copy.copy(myList)
    #print myList1
    #print myList2
    #print "--------"
    # 
    myDSM.display()

    print "--------"

    ## adding relations between existing components

    myDSM.addRelation(myList1, myList2, [1.0]*len(myList))


    myDSM.display()
    print "--------"


    ## adding relations with non existing elements

    #using pandas for better visualisation
    myDSM.dispPDFrame()
    
    
def example4():
    ## Example using Interactions
    #Based on  interactions of Pimmler and Eppinger (1994)
    ## http://web.mit.edu/eppinger/www/pdf/Pimmler_DTM1994.pdf
    ##    required = 2  
    ##    desired = 1
    ##    indifferent = 0 (default value)
    ##    undesired = -1 
    ##    detrimental = -2
    ##
    ##     create a dict of format [ S E 
    ##                             I M ]
    ###########################################################


    myDSM2=dsmx.DSM(name='example 2', dsmType='interactions')


    #adding components
    myDSM2.addComponent(['c1'])
    myDSM2.addComponent(['c2'])
    myDSM2.addComponent(['c3'])

    # 
    myDSM2.display()

    print "--------"


    ## adding relations between existing components

    # using complete interaction list
    myDSM2.addRelation(['c1'], ['c2'], [{'s':1, 'e':0, 'i':0 ,'m':-2}])
    myDSM2.addRelation(['c3'], ['c1'], [{'s':0, 'e':1, 'i':1 ,'m':0}])

    #one interaction at a time
    myDSM2.addRelation(['c2'], ['c3'], [{'s':2}])
    myDSM2.addRelation(['c2'], ['c3'], [{'e':-1}])
    myDSM2.addRelation(['c2'], ['c3'],  [{'i':0}])
    myDSM2.addRelation(['c2'], ['c3'], [{'m':-1}])

    #using lists of components and interactions, and new components

    myDSM2.addRelation(['c4', 'c6'], ['c5', 'c4'], [{'s':1, 'e':1, 'i':1 ,'m':1},{'s':-1, 'e':1, 'i':-1 ,'m':-2}])


    myDSM2.display()
    print "--------"


    myDSM2.dispPDFrame()
