import os
def myPattern(string1,string2,f1,f2):
    fin1 = open (f1)
    fin2 = open (f2,'w')
    for line in fin1:
        if string1 in line:
            flash=line.replace(string1,string2)
            fin2.write(flash)
        fin2.write(line)
    return fin2

myPattern('172','192','running-config.cfg','new-config.cfg')
