def allAccess(f):
    fin=open(f)
    my_dict=dict()
    access_name=['MGMT-TRANSIT', 'SERVER-INSIDE-XCOMP-RADIUS']
    for line in fin:
        myword=line.strip()
        for index in access_name:
            if index in myword:
                my_dict[index]=[line]
    return my_dict
print(allAccess('running-config.cfg'))
        
    
