##from __future__ import division
from feon.sa import *
import numpy as np
import pandas as pd
from feon.tools import gl_quad2d
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec




    




if __name__ == "__main__":
    
    xnum = 40
    ynum = 20
    E = 210e3#弹性模量
    nu = 0.46#泊松比
    
    Epdms = 210e3#弹性模量
    nupdms = 0.46#泊松比
    Esio2 = 55e9
    nupdms = 0.25
    t = 0.025#厚度
    nds={}#节点阵列
    crack=[]
    cnd = []
    cnum = 0
    e={}#单元阵列
    zleng = 0.25
    Jnum=0
    cn = 12
    stmax = 0.0
    stmaxa = []
    stmin = 10000000
    stmina = []
    
    def Cc (i,j):
        crack.append((i,j))
        cnd.append(Node(zleng*i+0.1*zleng,zleng*j))
        global cnum
        cnum = cnum +1
        print (crack, cnd ,cnum)
    def smax ():
        global stmax,stmin
        
        for i in range(xnum-1):
            for j in range(ynum-1):
                thats = e[i][j].stress['sx'][0][0]
                if thats>stmax:
                    stmax = e[i][j].stress['sx'][0][0]
                    k = i
                    l = j
                    
                if thats<stmin:
                    stmin = e[i][j].stress['sx'][0][0]
                    m = i
                    n = j
        stmaxa.append((k,l))
        stmina.append((m,n))
    
    for i in range(xnum):
        for j in range(ynum):
            Jnum=Jnum+1

    for i in range(xnum):
        nds[i] = [Node(zleng*i,zleng*j) for j in range(ynum)]
        
       
    for i in range(xnum-1):
        
        e[i] =[Quad2D11S((nds[i][j],nds[i+1][j],nds[i+1][j+1],nds[i][j+1]),E,nu,t) for j in range(ynum-1)]
    
    for i in range(cn):
        if cn==0:
            break
        Cc(19,ynum-i-1)
       
    
    
    
    
    for i in range(cnum):
        kuilei = ()
        kuilei = crack[i]
        j= kuilei[0]
        k= kuilei[1]-1
        print (j,k)
        if k<(ynum-2):
            
            e[j][k] = Quad2D11S((e[j][k].nodes[0],e[j][k].nodes[1],e[j][k].nodes[2],cnd[i]),E,nu,t)
            k = k+1
            e[j][k] = Quad2D11S((cnd[i],e[j][k].nodes[1],e[j][k].nodes[2],e[j][k].nodes[3]),E,nu,t)
        else:
            e[j][k] = Quad2D11S((e[j][k].nodes[0],e[j][k].nodes[1],e[j][k].nodes[2],cnd[i]),E,nu,t)
            
            
         
      
            

    s = System()
    for i in range(xnum):
        for j in range(ynum):
            s.add_nodes(nds[i][j])
    for i in range(cnum):
        s.add_nodes(cnd[i])
            
    for i in range(xnum-1):
        for j in range(ynum-1):
            s.add_elements(e[i][j])
    for i in range(ynum):
        s.add_node_disp(Jnum-ynum+i,Ux = (xnum-1)*zleng*0.3)
        s.add_node_disp(Jnum-ynum+i,Uy = 0)
    for i in range(ynum):  
        s.add_fixed_sup(i)
    s.solve()
    
    smax()
    
   
    
    
    '''
    plt.show()  
    '''
 
    

