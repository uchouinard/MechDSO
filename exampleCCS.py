def exampleCCS():
    ##########################################################
    ## pimmler & eppinger climate control system example 1994
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

    import DSM as dsmx
    ccs=dsmx.DSM(name='Climate Control System', dsmType='interactions', directed='no')


    '''
    ccs.addComponent('Radiator A')
    ccs.addComponent('Engine Fan B')
    ccs.addComponent('Heater Core C')
    ccs.addComponent('Heater Hoses D')
    ccs.addComponent('Condenser E')
    ccs.addComponent('Compressor F')
    ccs.addComponent('Evaporator Case G')
    ccs.addComponent('Evaporator Core H')
    ccs.addComponent('Accumulator I')
    ccs.addComponent('Refrigeration Controls J')
    ccs.addComponent('Air Controls K')
    ccs.addComponent('Sensors L')
    ccs.addComponent('Command Distribution M')
    ccs.addComponent('Actuators N')
    ccs.addComponent('Blower Controller O')
    ccs.addComponent('Blower Motor P')

    '''
    #input all components (not required)
    ccs.addComponent(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'])


    #input interactions
    ccs.addRelation(['A'],['B'], [{'s':2, 'e':0, 'i':0, 'm':2}])
    ccs.addRelation(['A'],['E'], [{'s':2, 'e':-2, 'i':0, 'm':0}])

    ccs.addRelation(['B'],['E'], [{'s':2, 'e':0, 'i':0, 'm':2}])
    ccs.addRelation(['B'],['M'], [{'s':1, 'e':0, 'i':0, 'm':0}])

    ccs.addRelation(['C'],['D'], [{'s':1, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['C'],['G'], [{'s':2, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['C'],['H'], [{'s':-1, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['C'],['P'], [{'s':0, 'e':0, 'i':0, 'm':2}])

    ccs.addRelation(['D'],['I'], [{'s':-1, 'e':0, 'i':0, 'm':0}])

    ccs.addRelation(['E'],['F'], [{'s':0, 'e':2, 'i':0, 'm':2}])
    ccs.addRelation(['E'],['H'], [{'s':-2, 'e':2, 'i':0, 'm':2}])

    ccs.addRelation(['F'],['H'], [{'s':0, 'e':2, 'i':0, 'm':2}])
    ccs.addRelation(['F'],['I'], [{'s':1, 'e':0, 'i':0, 'm':2}])
    ccs.addRelation(['F'],['J'], [{'s':0, 'e':0, 'i':2, 'm':0}])
    ccs.addRelation(['F'],['K'], [{'s':0, 'e':0, 'i':2, 'm':0}])
    ccs.addRelation(['F'],['M'], [{'s':1, 'e':0, 'i':0, 'm':0}])

    ccs.addRelation(['G'],['H'], [{'s':2, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['G'],['N'], [{'s':2, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['G'],['O'], [{'s':2, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['G'],['P'], [{'s':2, 'e':0, 'i':0, 'm':2}])

    ccs.addRelation(['H'],['I'], [{'s':1, 'e':0, 'i':0, 'm':2}])
    ccs.addRelation(['H'],['P'], [{'s':0, 'e':0, 'i':0, 'm':2}])

    ccs.addRelation(['I'],['J'], [{'s':1, 'e':0, 'i':0, 'm':0}])

    ccs.addRelation(['J'],['K'], [{'s':0, 'e':0, 'i':2, 'm':0}])
    ccs.addRelation(['J'],['M'], [{'s':1, 'e':0, 'i':0, 'm':0}])

    ccs.addRelation(['K'],['L'], [{'s':0, 'e':0, 'i':2, 'm':0}])
    ccs.addRelation(['K'],['M'], [{'s':1, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['K'],['N'], [{'s':0, 'e':0, 'i':2, 'm':0}])
    ccs.addRelation(['K'],['O'], [{'s':0, 'e':0, 'i':2, 'm':0}])

    ccs.addRelation(['L'],['M'], [{'s':1, 'e':0, 'i':0, 'm':0}])

    ccs.addRelation(['M'],['N'], [{'s':1, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['M'],['O'], [{'s':1, 'e':0, 'i':0, 'm':0}])
    ccs.addRelation(['M'],['P'],[{'s':1, 'e':0, 'i':0, 'm':0}])

    ccs.addRelation(['O'],['P'], [{'s':2, 'e':0, 'i':0, 'm':2}])
    
    ccs.display()
    
