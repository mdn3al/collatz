#!/usr/bin/env python

import math
import sys

#101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101001

#10110011110011000000011100000101111110000100011000111011101100101011111001010100111110110110111101010001110100100101100100110010001101110111101111110110001010101101011110011101101011000110110000101000101111000011100110010111010110100011111111101001100001100111111100011111010000001111011100111000100010011010100000110101011000001001001000010101110001011011010011011001101110010001000010000001001110101010010100001100010010100111001001111010111010000111100011001101000101001011100000000010110011110011000000011100000101111110000100011000111011101100101011111001010100111110110110111101010001110100100101100100110010001101110111101111110110001010101101011110011101101011000110110000101000101111000011100110010111010110100011111

#101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101010100101000011000100101001110010011110101110100001111000110011010001010010111000000000101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101001
#101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101

#10110011110011000000011100000101111110000100011000111011101100101011111001010100111110110110111101010001110100100101100100110010001101110111101111110110001010101101011110011101101011000110110000101000101111000011100110010111010110100011111111101001100001100111111100011111010000001111011100111000100010011010100000110101011000001001001000010101110001011011010011011001101110010001000010000001001110101010010100001100010010100111001001111010111010000111100011001101000101001011100000000010110011110011000000011100000101111110000100011000111011101100101011111001010100111110110110111101010001110100100101100100110010001101110111101111110110001010101101011110011101101011000110110000101000101111000011100110010111010110100011111111101001100001100111111100011111010000001111011100111000100010011010100000110101011000001001001000010101110001011011010011011001101110010001000010000001001110101010010100001100010010100111001001111010111010000111100011001101000101001011100000000010110011110011000000011100000101111110000100011000111011101100101011111001010100111110110110111101010001110100100101100100110010001101110111101111110110001010101101011110011101101011000110110000101000101111000011100110010111010110100011111
#1011001111001100000001110000010111111000010001100011101110110010101111100101010011111011011011110101000111010010010110010011001000110111011110111111011000101010110101111001110110101100011011000010100010111100001110011001011101011010001111111110100110000110011111110001111101000000111101110011100010001001101010000011010101100000100100100001010111000101101101001101100110111001000100001000000100111010101001010000110001001010011100100111101011101000011110001100110100010100101110000000001011001111001100000001110000010111111000010001100011101110110010101111100101010011111011011011110101000111010010010110010011001000110111011110111111011000101010110101111001110110101100011011000010100010111100001110011001011101011010001111

#101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101010100101000011000100101001110010011110101110100001111000110011010001010010111000000000101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101010100101000011000100101001110010011110101110100001111000110011010001010010111000000000101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101001
#101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101010100101000011000100101001110010011110101110100001111000110011010001010010111000000000101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101
#101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101010100101000011000100101001110010011110101110100001111000110011010001010010111000000000101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101010100101000011000100101001110010011110101110100001111000110011010001010010111000000000
#101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101010100101000011000100101001110010011110101110100001111000110011010001010010111000000000

#101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101001
#1011001111001100000001110000010111111000010001100011101110110010101111100101010011111011011011110101000111010010010110010011001000110111011110111111011000101010110101111001110110101100011011000010100010111100001110011001011101011010001111111110100110000110011111110001111101000000




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

pi6 = 0b101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101010100101000011000100101001110010011110101110100001111000110011010001010010111000000000
 
sabc = 0b101100111100110000000111000001011111100001000110001110111011001010111110010101001111101101101111010100011101001001011001001100100011011101111011111101100010101011010111100111011010110001101100001010001011110000111001100101110101101000111111111010011000011001111111000111110100000011110111001110001000100110101000001101010110000010010010000101011100010110110100110110011011100100010000100000010011101001


lb=lambda t: math.log(t)/math.log((2))
l=int(lb(pi6))
lc=int(lb(sabc))

n=2
if len(sys.argv)>1:
    n=int(sys.argv[1])
    print "argumentul este",sys.argv[1]

gen=(pi6*( 2**((l+1)*n)-1)/(2**(l+1)-1) )*2**(lc+1)+sabc
print gen
print bin(gen)

