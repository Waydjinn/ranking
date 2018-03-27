import numpy as np

def init ():
    f = open("/home/waydjinn/Rank/matrice1","r")
    t = int(f.readline())
    tab = []
    
     
    i = 0
    while i < t:
        line = f.readline().strip().split(' ')
        l = line.pop(0)
        for i in range(0,len(line)):
            if '.' in line[i]: 
                tab.append((line[i-1],line[i]))
        i=i+1
    print tab
    for n in range(len(tab)-1,0,-1):     
        for i in range(n):
            if tab[i][0] > tab[i+1][0]:
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
        
        
    print tab
    
    p = [item[1] for item in tab]
    u = [] 
    u = int(tab[0][0])

    for i in range(0,len(tab)-1,1):
        if tab[i][0] != tab[i+1][0]:
             u[i] = i

    print u
        


    print p 
    


    f.close()
    return


init()
