#!/usr/bin/env python

import math
import sys

# virusul gozi mihai paunescu 30VI2021 arestat

       
pi3=0b100101111011010000
sab=0b11100011100011100011100011100011100011100
sabc=0b1001011
lb=lambda t: math.log(t)/math.log((2))

l=int(lb(pi3))
lc=int(lb(sabc))

n=2
if len(sys.argv)>1:
    n=int(sys.argv[1])
    print "argumentul este",sys.argv[1]
#gen=(pi3/(2.0**(l+1)-1)*2**((l+1)*n)-pi3/(2.0**(l+1)-1))*2**7+0b1001011
#gen=(pi3*( 2**((l+1)*n)-1)/(2**(l+1)-1) )*2**(lc+1)+0b1001011
gen=(pi3*( 2**((l+1)*n)-1)/(2**(l+1)-1) )*2**(lc+1)+sabc
print gen
print bin(gen)
