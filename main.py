from number_theory_functions import *
from random import randrange

def Quize1 ():
    a = 797
    b = 5279
    c = 1000000
    (gcd,x,y) = extended_gcd(a,b)
    if(gcd == 1 and y < 0):
        return x,y
    return False

def Quize2():
    a = 123456
    b = 7896543
    c = 74365753
    e = modular_exponent(b,c,1000)
    n = modular_exponent(a,e,1000)
    return n//100

def Quize3():
    p = 3491
    q = 3499
    e = 3499
    N  = p * q
    phi_N = (p - 1)*(q - 1)
    (_,d,_) = extended_gcd(e,phi_N)
    return modular_exponent(42,d,N)

def Quize4():
    e=11
    N=991
    (d,_,_)=extended_gcd(e,N)
    if(d==1):
        inv=modular_inverse(e,N)
        print("inv : " + str(inv))
        return True
    return False
    
def Quize5 ():
    N = 7917 * 6841
    e = 11
    message = 1308
    return modular_exponent(message,e,N)

