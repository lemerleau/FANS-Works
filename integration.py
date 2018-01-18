'''
'''
import numpy as np
import random as r
g=[]
f_list=[]
u_list=[]
n=1000
def uniform(a,b):
        x=r.random()
        return (b-a)*x+a
def f(x):
        return np.log(np.log(x))       
for i in range(1000):
        k=uniform(2,10)
        g.append(k)
#print g
for j in g:
        f_x=f(j)   
        f_list.append(f_x) 
#print f_list
for i in range(1000):
        u=uniform(0, np.max(f_list))
        u_list.append(u)
#print u_list
i=0
new_list=[]

for i in range(n) :
        if u_list[i]<f(g[i]):
                new_list.append(g[i])      
#print new_list    
sol =0      
for x in new_list:
        sol= sol + (8./1000)*f(x)
print sol     
                       
                   
