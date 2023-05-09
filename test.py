from math import *


def f(x):
    
    return cos(x)- pow(x,3);

def biseccion(a,b,error):
    m1=a;
    m=b;
    k=0;
    
    if (f(a)*f(b)>0):
        print('La funcion no cambi a de signo');
    
    while(abs(m1-m)>error):
        m1=m;
        m=(a+b)/2
        if(f(a)*f(m)<0): #cambia el signo de en [a,m]
            b=m;
        if(f(m)*f(b)<0): #cambia el signo de en [m,b]
            a=m;
        print('el intervalo es [,a,',b,']')
        k=k+1;
        
    print ('x',k,'=',m,' es una buena aproximacion')
            
biseccion(0,1,0.001)
    