SectionExample=[36,91,51,2,54,6,58,6,58,2,54,1,48,97,43,22,83,25,79,95,42,87,73,17,2,42,95,38,79,29,65,9,55,97,39,83,31,77,17,62,3,49,90,37,13,17,58,11,51,92,33,78,21,66,9,54,49,90,35,84,26,74,22,62,12,90,36,83,32,75,31,94,34,87,40,7,58,5,56,22,58,77,71,10,73,23,57,13,36,89,22,68,2,44,99,27,81,26,85]


import scipy.stats
global significance,N,randomNumbersList,Oi,ChiSquare_0_List,ChiSquare_0,Ei
randomNumbersList=[]
N=10
Oi=[0]*N
ChiSquare_0_List=[0]*N

def inputVariables():
    global significance,N,Oi

    significance=float(input('What is the level of significance ? Enter like(0.95): '))



def randomNumbers(inputType):
    global significance,N,randomNumbersList
    if (inputType.upper()=='G'):
        inputVariables()
        generateRN()

    elif (inputType.upper()=='S'):
        randomNumbersList=SectionExample
        significance=0.95
        N=10

    elif (inputType.upper()=='I'):
        inputVariables()
        inputRN()


def generateRN():
    global randomNumbersList
    n=int(input("Enter Number of numbers 'example(100)': "))
    import random
    for i in range(n):
        randomNumbersList.append(int(random.uniform(0,100)))


def inputRN():
    global randomNumbersList
    randomNumbersList=input("ُEnter random Numbers like(85,31,72,23,75,37,44,17,43,11) : ").split(",")
    for i in range(len(randomNumbersList)):
        randomNumbersList[i]=int(randomNumbersList[i])

def calculate():
    global randomNumbersList,Oi,ChiSquare_0_List,N,ChiSquare_0,Ei
    Ei=round(len(randomNumbersList)/N)
    for i in randomNumbersList:
        if (i<=10):
            Oi[0]+=1
        elif (i<20):
            Oi[1]+=1
        elif (i<30):
            Oi[2]+=1
        elif (i<40):
            Oi[3]+=1
        elif (i<50):
            Oi[4]+=1
        elif (i<60):
            Oi[5]+=1
        elif (i<70):
            Oi[6]+=1
        elif (i<80):
            Oi[7]+=1
        elif (i<90):
            Oi[8]+=1
        elif (i<100):
            Oi[9]+=1
    
    for i in range(0,N):
        ChiSquare_0_List[i] = ( (Oi[i] - Ei)**2 ) / Ei

    ChiSquare_0=sum(ChiSquare_0_List)


def printResultset():
    global significance,N,randomNumbersList,Oi,Ei,ChiSquare_0_List

    import pandas as pd
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    table = pd.DataFrame({'interval':['0:9','10:19','20:29','30:39','40:49','50:59','60:69','70:79','80:89','90:99'],
                    ' Oi':Oi,
                    ' Ei':[Ei]*N,
                    ' (Oi-Ei)^2/Ei':ChiSquare_0_List,})
    print('\n\n',table,'\n\n')


    
def startSemolation():
    global significance,N,randomNumbersList,Oi

    inputType=input('Generate Random Numbers = G , Use Section Example = S , input Random Numbers = I: ')
    randomNumbers(inputType)

    calculate()

    ChiSquare=scipy.stats.chi2.ppf(significance, df=N-1)
    print("\nChiSquare_0: ",ChiSquare_0,"\nChiSquare: ",ChiSquare)
    if (ChiSquare_0>ChiSquare):
        print("\n\nReject H0: Rondom Numbers are not Uniform")
    else:
        print("\n\nDon't Reject H0: Rondom Numbers are Uniform")

    printResultset()


startSemolation()