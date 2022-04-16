#include <stdio.h>
//#define NDEBUG
#include <assert.h>


unsigned long gcd(a,b)unsigned long a,b;{
if(a==0) return b;
if(b==0) return a;
if(a==1 || b==1) return 1;
if(((a&1)==0)&&((b&1)==0))  return 2*gcd(a/2,b/2);
        else {
            if((a&1)==0) return gcd(a/2,b);
            if((b&1)==0) return gcd(a,b/2);
            if(a>b) return gcd(b,(a-b)/2);
            else return gcd((b-a)/2,a);
        }
}
unsigned long gcdnr(a,b)unsigned long a,b;{
unsigned long r=0;
while(a && b){
    if(((a&1)==0)&&((b&1)==0))  {
                a>>=1,b>>=1;
                r+=1;a>>=1,b>>=1;
            }else {
                if((a&1)==0)  a>>=1;
                if((b&1)==0)  b>>=1;
                if(((a&1)==1)&&((b&1)==1)){
                        if(a>b)  a=(a-b)>>1;
                        else  b=(b-a)>>1;}
            }
    
}
if(a==0) return b<<r;
if(b==0) return a<<r;
return 0;// if error
}
unsigned long collatz(unsigned long x){
unsigned long y=1;
 while (x>1){
   while((x&1)==0) { assert( 1==gcd(y,x) );// invariant
        x=x/2;  }
   y=x;
   if(x>1)  // x is odd
        x=3*x+1;
   
 }
 return x; // x==1
}
main(argn,argv)char *argv[];{
long a=8,b=4,n;

if (argn>1) printf(" has arguments %s \n",argv[0]);
if(argn>2){
    a=atoi(argv[1]);
    n=atoi(argv[2]);
}else{
    printf(" a= ");scanf("%d",&a);
    printf(" n= ");scanf("%d",&n);
}

printf(" cmmdc %d  %d ",gcd(a,b),collatz(a)); 

return 0;}
