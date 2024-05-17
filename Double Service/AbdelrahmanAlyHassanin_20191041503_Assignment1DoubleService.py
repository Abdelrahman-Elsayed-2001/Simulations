#Abdelrahman Aly Hassanin Aly Elsayed
#20191041503

rn_iatExample=[0,94,73,70,82,25,35,61,42,48,26,88,31,90,55,95,58,70,15,73,65,74,75]
rn_stExample=[32,96,89,32,67,48,63,99,98,66,85,58,6,39,15,2,48,63,85,61,40,16,18]

def inputData():
    random = input('Generate Random Numbers = G , Use Section Example = S , input Random Numbers = I: ')
    fServer = input('First Server A for Able, B For Baker: ')
    if (random.lower() == 's'):
        n=len(rn_iatExample)
    else:
        n = int(input('Number of castomers: '))

    return random,fServer,n

random,fServer,n=inputData()

castomer = list(range(1, n+1))
rn_iat=[-1]*n
rn_st=[-1]*n
iat=[0]*n
clock=[0]*n
wt=[0]*n
timeSpent=[0]*n
ableB=[-1]*n
ableST=[-1]*n
ableE=[-1]*n
ableIdle=[-1]*n
bakerB=[-1]*n
bakerST=[-1]*n
bakerE=[-1]*n
bakerIdle=[-1]*n


def generateRN(n):
    import random
    for i in range(0,n):
        rn_iat[i]=int(random.uniform(0,100))
        rn_st[i]=int(random.uniform(0,100))

def able(st):
    for k in range(n3):
        if (st<=ST_probabilityRange_Able[k]):
            return ST_minutes_Able[k]

def baker(st):
    for k in range(n4):
        if (st<=ST_probabilityRange_Baker[k]):
            return ST_minutes_Baker[k]


def getlast(index,arr):
    for j in range(index,-1,-1):
        if (arr[j]!=-1):
            return arr[j]
    return -1


def nextEmployee(index,fServer):

    a=getlast(index,ableE)-clock[index+1] 
    b=getlast(index,bakerE)-clock[index+1]
    if ( (a<=0 and b <=0) or a==b ):
        if (fServer.upper()=='A'):
            return 0
        elif (fServer.upper()=='B'):
            return 1
    elif (a<b):
        return 0
    else:
        return 1

def iatProbabilty():

    ita_minutes=input("ُEnter iat minutes like(1 2 3 4) : ").split()
    iat_probability=input("Enter iat probabilities for minutes like(25 40 20 15) : ").split()
    
    n2=len(ita_minutes)
    for i in range(n2):
        ita_minutes[i]=int(ita_minutes[i])
        iat_probability[i]=int(iat_probability[i])

    ita_probabilityRange=[-1]*n2
    ita_probabilityRange[0]=iat_probability[0]-1

    for i in range(1,n2):
        ita_probabilityRange[i]=iat_probability[i]+ita_probabilityRange[i-1]

    for j in range(n):
        for k in range(n2):
            if (rn_iat[j]<=ita_probabilityRange[k]):
                iat[j]=ita_minutes[k]
                break

        for i in range(1,n):
            clock[i]=clock[i-1]+iat[i]

def startSemolation(fServer,n):
    employee=-1
    iatProbabilty()

    if (fServer.upper()=='A'):
        employee= 0
    elif (fServer.upper()=='B'):
        employee= 1

    if (employee==0):
        ableB[0]=0
        ableIdle[0]=0
        ableST[0]=able(rn_st[0])
        ableE[0]=ableST[0]+ableB[0]
        timeSpent[0]=ableST[0]

    elif (employee==1):
        bakerB[0]=0
        bakerIdle[0]=0
        bakerST[0]=baker(rn_st[0])
        bakerE[0]=bakerST[0]+bakerB[0]
        timeSpent[0]=bakerST[0]

    employee=nextEmployee(0,fServer)

    for i in range(1,n):
        if (employee==0):
            end=getlast(i,ableE)
            if (end<0):
                end+=1
            if end>clock[i]:
                ableB[i]=end
            else:
                ableB[i]=clock[i]
            ableIdle[i]=ableB[i]-end
            ableST[i]=able(rn_st[i])
            ableE[i]=ableST[i]+ableB[i]
            wt[i]=ableB[i]-clock[i]
            timeSpent[i]=ableST[i]+wt[i]

        elif (employee==1):
            end=getlast(i,bakerE)
            if (end<0):
                end+=1
            if end>clock[i]:
                bakerB[i]=end
            else:
                bakerB[i]=clock[i]
            bakerIdle[i]=bakerB[i]-end
            bakerST[i]=baker(rn_st[i])
            bakerE[i]=bakerST[i]+bakerB[i]
            wt[i]=bakerB[i]-clock[i]
            timeSpent[i]=bakerST[i]+wt[i]
        
        if (i!=n-1):
            employee=nextEmployee(i,fServer)

if (random.upper()=='I'):
    for i in range(0,n):
        rn_iat[i]=int(input("iat random number for customer {}: ".format(i+1)))
        rn_st[i]=int(input("ST random number for customer{}: ".format(i+1)))
elif(random.upper()=='G'):
    generateRN(n)
elif(random.upper()=='S'):
    rn_iat=rn_iatExample
    rn_st=rn_stExample


ST_minutes_Able=input("ُEnter minute number like(2 3 4 5) : ").split()
ST_probability_Able=input("Enter minutes probability like(30 28 25 17) : ").split()

n3=len(ST_probability_Able)
for i in range(n3):
    ST_minutes_Able[i]=int(ST_minutes_Able[i])
    ST_probability_Able[i]=int(ST_probability_Able[i])

ST_probabilityRange_Able=[-1]*n3
ST_probabilityRange_Able[0]=ST_probability_Able[0]-1
for i in range(1,n3):
    ST_probabilityRange_Able[i]=ST_probability_Able[i]+ST_probabilityRange_Able[i-1]


ST_minutes_Baker=input("ُEnter minutes like(2 3 4 5) : ").split()
ST_probability_Baker=input("Enter minutes probability like(35 25 20 20) : ").split()

n4=len(ST_probability_Baker)

for i in range(n4):
    ST_minutes_Baker[i]=int(ST_minutes_Baker[i])
    ST_probability_Baker[i]=int(ST_probability_Baker[i])

ST_probabilityRange_Baker=[-1]*n4
ST_probabilityRange_Baker[0]=ST_probability_Baker[0]-1
for i in range(1,n4):
    ST_probabilityRange_Baker[i]=ST_probability_Baker[i]+ST_probabilityRange_Baker[i-1]


startSemolation(fServer,n)

#print('customer',castomer)
#print('rn_iat',rn_iat)
#print('rn_st',rn_st)
#print('iat',iat)
#print('clock',clock)
#print('wt',wt)
#print('timeSpent',timeSpent)
#print('ableB',ableB)
#print('ableST',ableST)
#print('ableE',ableE)
#print('ableIdle',ableIdle)
#print('bakerB',bakerB)
#print('bakerST',bakerST)
#print('bakerE',bakerE)
#print('bakerIdle',bakerIdle)

import pandas as pd
table = pd.DataFrame({'customer':castomer,
                   'RN-IAT':rn_iat,
                   'IAT':iat,
                   'clock':clock,
                   'RN-ST':rn_st,
                   'Able ST Begins':ableB,
                   'Able ST':ableST,
                   'Able ST Ends':ableE,
                   'Baker ST Begins':bakerB,
                   'Baker ST':bakerST,
                   'Baker ST Ends':bakerE,                   
                   'Wating Time':wt,
                   'Time spent in System':timeSpent,
                   'Able Idle Time':ableIdle,
                   'Baker Idle Time':bakerIdle})

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(table)
