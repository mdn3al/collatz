#!/usr/bin/env python
import sys
def cola(n):
    if (n % 2) == 0 :
        n=n/2
    else:
        n=3*n+1
    return n

def cola2(n):
    m=1
    while (n % 2) == 0 :
        n=n/2
    m=n
    if n>1:
        n=3*n+1
    return n
def cola3(n):
     if (n % 2) == 1 :
             n=3*n+1
     while (n % 2)==0:
        n=n/2
     return n

def collatz(n):
    print n
    while n>1:
         n=cola3(n)
         print n
 
def invColla(y):
    if (y % 3) == 0:
        return 0
    if (2*y -1) % 3==0 :
        return (2*y -1) / 3
    else :
        return (4*y -1) / 3
def invCollaz(y):
    if (y % 3) == 0:
        return 0 # no preimage
    if (2*y ) % 3==1 :
        return (2*y -1) / 3
    else :
        return (4*y -1) / 3

m=5
if len(sys.argv)>1:
    # m=int(sys.argv[1])
    m=long(sys.argv[1])
print m," c ",cola(m)
print m," ic ",invColla(m)
    
    
'''
172. Toshio Urata and Hisao Kajita (1998), Collatz Problem III, (Japanese), Epsilon (The
Bulletin of the Society of Mathematics Education of Aichi Univ. of Education) [Aichi
Kyoiku Daigaku Sugaku Kyoiku Gakkai shi] 40 (1998), 57–65.
which takes odd
The authors study the speeded-up Collatz function φ(x) = 3x+1
2 e
integers to odd integers. They describe the infinite
number
of
preimages
of a given x as
n
4 n (2x)−1
:
n
≥
0}
if
x
≡
1
(mod
3)
and
{
:
n
≥
0}
if
x
≡
2
(mod
3). They
{ 4 x−1
3
3
encode the trajectory of this function with a vector (p 1 , p 2 , p 3 , ...) which keeps track of the
64powers of 2 divided out at each iteration. More generally they consider the speeded-up
(ax + d)-function, with a, d odd. For y 0 an initial value (with y 0 6 = − a d ), the iterates are
+d
y i = ay 2 i−1
pi+1 . They encode this iteration for n steps by an n × n matrix
Arxiv 3x_survey_eng
                                                                                                                        Mon 21 Jun 2021 22:45:30 EEST
'''

