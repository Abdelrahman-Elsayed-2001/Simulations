LecturExample_Probabilities=[30.24,50.4,10.8,7.2,0.9,0.45,0.01]
LecturExample_ObservedDistribution =[3075,4935,1135,695,105,54,1]



global N,a,ObservedDistribution,Probabilities

ObservedDistribution=[]
Probabilities=[]


def inputVariables():
    global a

    a=float(input('Enter alpha value ? Enter like(0.01): '))



def randomNumbers(inputType):
    global N,a,ObservedDistribution,Probabilities
    if (inputType.upper()=='L'):
        ObservedDistribution=LecturExample_ObservedDistribution
        Probabilities=LecturExample_Probabilities
        N=sum(ObservedDistribution)
        a=0.01

    elif (inputType.upper()=='I'):
        inputVariables()
        inputRN()




def inputRN():
    global N,ObservedDistribution,Probabilities

    ObservedDistribution=input("ُEnter Observed Distribution like(3075,4935,1135,695,105,54,1) : ").split(",")
    Probabilities=input("ُEnter Probabilities like(30.24,50.4,10.8,7.2,0.9,0.45,0.01) : ").split(",")

    for i in range(len(Probabilities)):
        Probabilities[i]=float(Probabilities[i])
        ObservedDistribution[i]=int(ObservedDistribution[i])

    N=sum(ObservedDistribution)
    

def calculateAndPrint():
    global N,a,ObservedDistribution,Probabilities
    Expected=[]

    import scipy.stats
    CHI_CRITIAL = scipy.stats.chi2.ppf(1 - a, df=len(Probabilities) - 1)


    for i in Probabilities:
        Expected.append(i/(100) * N)
    
    
    ChiSquare_0=0
    for i in range(0,len(Expected)):
        ChiSquare_0 += (ObservedDistribution[i] - Expected[i])**2/(Expected[i])


    print("\nH0: numbers are independent\nHa:numbers are not independent")

    print('\nChi Square 0=',ChiSquare_0,'\nChi Square CRITIAL=', CHI_CRITIAL)

    if(ChiSquare_0<= CHI_CRITIAL):
        print('\nthe H0 is not rejected')
    else:
        print('\nthe H0 is rejected')



def startSemolation():
    inputType=input('Use Lecture Example = L , input Random Numbers = I: ')
    randomNumbers(inputType)

    calculateAndPrint()

startSemolation()