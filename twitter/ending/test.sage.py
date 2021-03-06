

# This file was *autogenerated* from the file test.sage
from sage.all_cmdline import *   # import sage library

_sage_const_8 = Integer(8); _sage_const_23 = Integer(23); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1)
d = _sage_const_8 
p = _sage_const_23 

def last(x,p):
    if x<p:
        return(mod(factorial(x),p))
    else:
        y = floor(x/p)
        r = (mod(x,p)).lift()
        if (mod(y,_sage_const_2 )==_sage_const_1 ):
            return(-last(y,p)*mod(factorial(r),p))
        else:
            return(last(y,p)*mod(factorial(r),p))

print(p,d)
i = (d-_sage_const_1 )*((p**(p-_sage_const_1 )-_sage_const_1 )/(p-_sage_const_1 ))+_sage_const_1 
print(i,last(i,p))
print()

print(p,d)
i = (d-_sage_const_1 )*((p**(p-_sage_const_1 )-_sage_const_1 )/(p-_sage_const_1 ))+p**(p-_sage_const_2 )
print(i,last(i,p))

#print(i.str(base=p),len(i.str(base=p)))
#j = (d-1)*((p^p-1)/(p-1)) + 1

#x = factorial(i)
#y = factorial(j)

#print(x.str(base=p))
#print(y.str(base=p))

#m = x.ord(p)
#x = x/p^m

#n = y.ord(p)
#y = y/p^n

#print(mod(x,p))
#print(mod(y,p))

#x = factorial(i)
#m = x.ord(p)
#x = x/p^m
#print(mod(x,p))

