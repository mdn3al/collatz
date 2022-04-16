#!/usr/bin/env python

import math
import sys

#2
#0b1100101001000101100001111110011010110111001
#4
#0b110010100100010110000111111001101011011101001111000000110010100100010110000111

#7
# 6452761920871129381231399963150567565387

#        11001010010001011000011
pi4 = 0b110010100100010110000111111001101011011101001111000000
 
sabc = 0b110010100100010110000111

lb=lambda t: math.log(t)/math.log((2))
l=int(lb(pi4))
lc=int(lb(sabc))

n=2
if len(sys.argv)>1:
    n=int(sys.argv[1])
    print "argumentul este",sys.argv[1]

gen=(pi4*( 2**((l+1)*n)-1)/(2**(l+1)-1) )*2**(lc+1)+sabc
print gen
print bin(gen)




'''
Binary expression of ancestors in the Collatz graph
Tristan Stérin

1907.00775
'''
