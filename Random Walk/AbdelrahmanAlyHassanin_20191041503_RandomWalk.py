#Abdelrahman Aly Hassanin
#20191041503

global possibleSteps,stepProbability,direction,rn
possibleSteps=[-1,-1,-1,-1]
stepProbability=[-1,-1,-1,-1]

def getlast(index,arr):
    for j in range(index,-1,-1):
        if (arr[j]!=-1):
            return arr[j]
    return 0

def stepsProbabilty():
    global possibleSteps,rn,direction,stepProbability

    rn=input("enter RN ex(60,20,0,60,80,50,70,70,90,80,40,80,20,60,20,10,30,90,80,40): ").split(",")

    for i in range(len(rn)):
        rn[i]=int(rn[i])

    stepName=['Forward','Backward','Left','Right']

    for i in range(4):
            possibleSteps[i]=bool(int(input("is system have {} step? No=0 Yes=1 : ".format(stepName[i]))))

    for i in range(4):
        if i!=0:
            Cumulative=getlast(i,stepProbability)
        else:
            Cumulative=-1
        if (possibleSteps[i]):
            stepProbability[i]=Cumulative+int(input("enter the Probabilty of {} step: ".format(stepName[i])))

    direction=[0]*len(rn)
    for j in range(len(rn)):
        for k in range(4):
            if (possibleSteps[k]):
                if (rn[j]<=stepProbability[k]):
                    direction[j]=stepName[k]
                    break


stepsProbabilty()

x=0
y=0
Xcoordinate=[]
Ycoordinate=[]

for i in range(len(rn)):
    match direction[i]:
        case "Forward":
            y+=1
            Ycoordinate.append(y)
            Xcoordinate.append(x)
            continue
        case "Backward":
            y+=1
            Ycoordinate.append(y)
            Xcoordinate.append(x)
            continue
        case "Left":
            x-=1
            Ycoordinate.append(y)
            Xcoordinate.append(x)
            continue
        case 'Right':
            x+=1
            Ycoordinate.append(y)
            Xcoordinate.append(x)
            continue

step=[0]*len(rn)
for i in range(len(rn)):
    step[i]=i+1


import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

table = pd.DataFrame({'step': step,
                ' Random Numbers':rn,
                ' direction':direction,
                ' X coordinate':Xcoordinate,
                ' Y coordinate':Ycoordinate})
print('\n',table,'\n')