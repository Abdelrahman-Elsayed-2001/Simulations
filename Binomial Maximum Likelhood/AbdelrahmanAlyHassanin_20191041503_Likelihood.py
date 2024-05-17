#Likelihood BONUS
#Abdelrahman Aly Hassanin
#20191041503

from sympy import *

print("\nP(x,n|p)")
nInput=int(input("enter value of n: "))
xInput=int(input("enter value of x: "))

x , n , p = symbols('x n p')

f=( (factorial(n) / (factorial(n-x)*factorial(x)) ) * (p**x) * ( (1-p)**(n-x) ) )

print("\nL(x,n|p) = ",f)

equation=f.diff(p)

print("\nd L(x,n|p) / dp = \n",equation,"= 0")

general_P = solve(equation,p)

print("\np = ",general_P[0])

general_P=str(general_P[0]).replace('x',str(xInput))
general_P=general_P.replace('n',str(nInput))

print("Maximum Likelihood Estimation = ",general_P," = ",eval(general_P))


