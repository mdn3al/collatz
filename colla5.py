#!/usr/bin/env python

import math
import sys


# Referinta #417376876:
# owim-service-ro@tdm-service.eu

#100001101101100100000101010001000111101000110100101011001100011000001110101111111011110010010011011111010101110111000010111001011010100110011100111110001010000000100001101101100100000101010001000111101000110100101011001100011000001110101111
#10000110110110010000010101000100011110100011010010101100110001100000111010111

#  0   240   0     78   
# 5 d3
#1000011011011001000001010100010001111010001101001010110011000110000011101011111110111100100100110111110101011101110000101110010110101001100111001111100010100000001000011011011001000001010100010001111010001101001010110011000110000011101011111110111100100100110111110101011101110000101110010110101001100111001111100010100000001000011011011001000001001
#1000011011011001000001010100010001111010001101001010110011000110000011101011111110111100100100110111110101011101110000101110010110101001100111001111100010100000001000011011011001000001

#100001101101100100000101010001000111101000110100101011001100011000001110101111111011110010010011011111010101110111000010111001011010100110011100111110001010000000
#100001101101100100000101010001000111101000110100101011001100011000001110101111111
#011110010010011011111010101110111000010111001011010100110011100111110001010000000

#100001101101100100000101010001000111101000110100101011001100011000001110101111
#10000110110110010000010101000100011110100011010010101100110001100000111010111111101111001001001101111101010111011100001011100101101010011001110011111000101000000010000110110110010000010101000100011110100011010010101100110001100000111010111
#

pi5 = 0b100001101101100100000101010001000111101000110100101011001100011000001110101111111011110010010011011111010101110111000010111001011010100110011100111110001010000000
 
sabc = 0b100001101101100100000101010001000111101000110100101011001100011000001110101111

lb=lambda t: math.log(t)/math.log((2))
l=int(lb(pi5))
lc=int(lb(sabc))

n=2
if len(sys.argv)>1:
    n=int(sys.argv[1])
    print "argumentul este",sys.argv[1]

gen=(pi5*( 2**((l+1)*n)-1)/(2**(l+1)-1) )*2**(lc+1)+sabc
print gen
print bin(gen)

