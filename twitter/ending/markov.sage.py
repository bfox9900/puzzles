

# This file was *autogenerated* from the file markov.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_300 = Integer(300)
#p = 5
#m = matrix(RDF,[[0,0,1/4,3/4],[1/4,0,3/4,0],[0,3/4,0,1/4],[3/4,1/4,0,0]])

#print(f"Base {p}")
#print(m)
#print(m^100)
#print()

def least_power(p):
    header = [mod(-_sage_const_1 ,p)]*(p-_sage_const_1 )

    for i in range(_sage_const_1 ,p-_sage_const_1 ):
        header[i] = -(i+_sage_const_1 )*header[i-_sage_const_1 ]

    m = (matrix(QQ, p-_sage_const_1 , p-_sage_const_1 , lambda i, j: header.count(mod((i+_sage_const_1 ),p)/mod((j+_sage_const_1 ),p))))/(p-_sage_const_1 )

    for i in range(_sage_const_1 ,p):
        c = (m**i).list().count(_sage_const_0 )
        if c==_sage_const_0 :
            print(f"For base {p} all values found at power {i}")
            c = (m**(i+_sage_const_1 )).list().count(_sage_const_0 )
            print(f"For base {p} count {c} found at power {i+1}")
            return

for p in prime_range(_sage_const_300 ):
    least_power(p)
