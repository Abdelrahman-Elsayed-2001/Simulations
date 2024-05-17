#Abdelrahman Aly Hassanin
#20191041503

ActionSectionExample=[0,1,2,3,4,5,6,7]
FrequencySectionExample=[161,148,93,66,21,9,2,0]

import scipy.stats
global alpha,total,ChiSquare_0_List,expected,probability,Frequency,numberAction
numberAction=[]
Frequency=[]

def randomNumbers(inputType):
    global alpha,Frequency,numberAction
    if (inputType.upper()=='S'):
        numberAction=ActionSectionExample
        Frequency=FrequencySectionExample
        alpha=0.05

    elif (inputType.upper()=='I'):
        try:
            alpha=float(input('What is alpha ? Enter like(0.05): '))
            numberAction=input("ُEnter No. of Actions, Enter like(0,1,2,3,4,5,6,7): ").split(",")
            Frequency=input("ُEnter Frequency, Enter like(161,148,93,66,21,9,2,0): ").split(",")
            
            n=len(numberAction)
            for i in range(n):
                numberAction[i]=int(numberAction[i])
                Frequency[i]=int(Frequency[i])

        except:
            print("invalid input, try again")
            randomNumbers( input('Use Section Example = S , input Random Numbers = I: ') )
    
    else:
        print("invalid input")
        randomNumbers( input('Use Section Example = S , input Random Numbers = I: ') )
    

def calculate():
    global alpha,total,ChiSquare_0_List,expected,probability,Frequency,numberAction
    n=len(numberAction)
    expected=[0]*n
    probability=[0]*n
    ChiSquare_0_List=[0]*n
    total=sum(Frequency)

    u=0
    s2=0

    for i in range(n):
        u+=(numberAction[i]*Frequency[i])/total

    for i in range(n):
        s2+=( (numberAction[i]**2) * Frequency[i] ) 
    
    s2= ( s2 - (total * u**2) ) / (total-1)

    p=u/s2
    q=1-p
    k=p*u/q

    probability[0]=p**k
    expected[0]=round(probability[0]*total)
    ChiSquare_0_List[0]= ( ( Frequency[0]-expected[0] )**2 / expected[0] )

    for i in range(1,n-1):
        probability[i]= ( (k+i-1) * q ) *probability[i-1] / i
        expected[i]= round(probability[i]*total)
        ChiSquare_0_List[i]= (Frequency[i]-expected[i])**2 / expected[i]
    
    temp=sum(probability)
    probability[n-1]=1-temp
    expected[n-1]= round(probability[n-1]*total)
    ChiSquare_0_List[n-1]= (Frequency[n-1]-expected[n-1])**2 / expected[n-1]

    ChiSquare_0=sum(ChiSquare_0_List)

    dof=n-4
    ChiSquare=scipy.stats.chi2.ppf(1-alpha, df=dof)

    printResultset(ChiSquare,p,k,u,s2,dof,ChiSquare_0)


def printResultset(ChiSquare,p,k,u,s2,dof,ChiSquare_0):
    global alpha,total,ChiSquare_0_List,expected,probability,Frequency,numberAction

    import pandas as pd
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    table = pd.DataFrame({'u':[u],
                    ' s2':[s2],
                    ' p':[p],
                    ' q':[1-p],
                    ' k':[k],
                    ' DOF':[dof]})
    print('\n\n',table,'\n\n')

    table2 = pd.DataFrame({'X':numberAction,
                    ' O(x)':Frequency,
                    ' P(x)':probability,
                    ' E(x)':expected,
                    ' Chi-Square':ChiSquare_0_List,})
    print(table2)


    print("\nH0:sample data represent the actual population.\nHa:sample data 'not' represent the actual population.")
    print("\nChi-Square 0: ",ChiSquare_0,"\nChi-Square from the table: ",ChiSquare)
    if (ChiSquare_0>ChiSquare):
        print("\nReject H0")
    else:
        print("\nDon't Reject H0\n")


def startSemolation():

    inputType=input('Use Section Example = S , input Random Numbers = I: ')
    randomNumbers(inputType)

    calculate()


startSemolation()