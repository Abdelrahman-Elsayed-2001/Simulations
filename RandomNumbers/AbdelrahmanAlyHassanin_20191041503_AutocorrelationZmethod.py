LecturExample=[0.12,0.01,0.23,0.28,0.89,0.31,0.64,0.28,0.83,0.93,0.99,0.15,0.33,0.35,0.91,0.41,0.6,0.27,0.75,0.88,0.68,0.49,0.05,0.43,0.95,0.58,0.19,0.36,0.69,0.87]

global N,M,m,a,i,RN,P

RN=[]

def inputVariables():
    global N,M,m,a,i

    i = int(input('Enter starting index ')) -1
    m = int(input('Enter number of steps '))
    a=float(input('Enter alpha value ? Enter like(0.05): '))

    


def randomNumbers(inputType):
    global N,M,m,a,i,RN
    if (inputType.upper()=='G'):
        inputVariables()
        generateRN()

    elif (inputType.upper()=='L'):
        RN=LecturExample
        N=len(LecturExample)
        a=0.05
        i = 3-1
        m = 5
        M = 4

    elif (inputType.upper()=='I'):
        inputVariables()
        inputRN()


def generateRN():
    global N,RN
    N=int(input("Enter Number of numbers 'example(100)': "))
    import random
    for ii in range(N):
        RN.append( int(random.uniform(0,100))/100 )


def inputRN():
    global N,RN,M
    RN=input("ُEnter random Numbers like(0.12,0.01,0.23,0.28,0.89,0.31,0.64,0.28,0.83,0.93) : ").split(",")
    for ii in range(len(RN)):
        RN[ii]=float(RN[ii])
    N=len(RN)
    M = ((N-i)/m)-1

def calculateAndPrint():
    global N,M,m,a,i,RN,P

    temp=RN[i]*RN[i+m]
    print('\ntemp=(' , RN[i] , ')(', RN[i+m] ,')', end='')

    for i in range(i+m, N-(i+m)+1, m):
        print(' + (' , RN[i] , ')(', RN[i+m] , ')',end='')
        temp+=RN[i]*RN[i+m]
    

    P=(1/(M+1)) * temp - 0.25
    print('\n\nP = ',  '1/',M+1,'(' , temp , ') - 0.25 = ',P )

    from math import sqrt
    sigma = (sqrt(13*M + 7))/(12*(M+1))
    print('sigma= sqrt(13*M + 7))/(12*(M+1)) = ',sigma )


    Z0 = P/sigma
    print('Z0 = ',  'P/sigma = ',Z0 )


    import scipy.stats as st
    Z = st.norm.ppf(1-a)

    print("\nH0: numbers are independent\nHa:numbers are not independent\n")
    if(Z0 >= -Z and Z0<= Z):
        print('the H0 is not rejected')
    else:
        print('the H0 is rejected')



def startSemolation():
    global N,M,m,a,i,RN
    inputType=input('Generate Random Numbers = G , Use Lecture Example = L , input Random Numbers = I: ')
    randomNumbers(inputType)

    calculateAndPrint()

startSemolation()