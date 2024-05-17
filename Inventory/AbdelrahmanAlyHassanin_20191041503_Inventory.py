#Abdelrahman Aly Hassanin
#20191041503

rn_lead_Example=[50,100,30,40,80]
rn_demand_Example=[24,35,65,81,54,3,87,27,73,70,47,45,48,17,9,42,87,26,36,40,7,63,19,88,94]

global start, nCycles, nDaysCycle, capacity
global startedStock, order, rn_demand, demand, EndedStock, lead, rn_lead, Short ,oldOrder,leadNumbers,demand_probability,lead_probability

startedStock=[]
order=[]
rn_demand=[]
demand=[]
EndedStock=[]
lead=[]
rn_lead=[]
Short=[]

leadNumbers=[]
demand_probability=[]
lead_probability=[]
oldOrder=[0,0]

def generateRN():
    global rn_lead,rn_demand,nCycles,nDaysCycle
    n=nDaysCycle*nCycles

    import random
    for i in range(n):
        rn_lead.append(int(random.uniform(1,101)))
        rn_demand.append(int(random.uniform(1,101)))

def inputVariables():
    global start, nCycles, nDaysCycle,capacity,oldOrder
    start=int(input("how mach units you start? "))
    
    if ( input("Is there a pre-order? (YES or NO)").upper()=="YES" ):
        oldOrder[0]=int(input("which day order will arrive? "))
        oldOrder[1]=int(input("how mach unit will arrive at day{}").format(oldOrder[0]))

    nCycles=int(input("Number of Cycles? "))
    nDaysCycle=int(input("Number of Days in Cycle? "))
    capacity=int(input("what is the capacity of inventory ? "))

def inputRN():
    global rn_lead,rn_demand

    rn_lead=input("ُEnter leads random Numbers like(50,100,30,40,80) : ").split(",")
    rn_demand=input("ُEnter Demand random Numbers like(24,35,65,81,54,3,87,27,73,70,47,45,48,17,9,42,87,26,36,40,7,63,19,88,94) : ").split(",")
    
    for i in range(len(rn_lead)):
        rn_lead[i]=int(rn_lead[i])
        if(rn_lead[i]==0):
            rn_lead[i]==100
            
    for i in range(len(rn_demand)):
        rn_demand[i]=int(rn_demand[i])
        if(rn_demand[i]==0):
            rn_demand[i]==100

        

def randomNumbers(status):
    global start, nCycles, nDaysCycle, capacity
    global rn_demand, rn_lead ,oldOrder
    
    status=str(status)
    match status.upper():
        case "S":
            rn_demand=rn_demand_Example
            rn_lead=rn_lead_Example
            oldOrder=[2,8]
            start=3
            nCycles=5
            nDaysCycle=5
            capacity=11
            return "S"

        case "G":
            inputVariables()
            generateRN()
            return "G"

        case "I":
            inputVariables()
            inputRN()
            return "I"

        case _:
            print("invaled input")
            inputType=input('Generate Random Numbers = G , Use Section Example = S , input Random Numbers = I: ')
            randomNumbers(inputType)
            return inputType


def ProbabiltyInput(inputType):
    global rn_demand,demand,rn_lead,leadNumbers,demand_probability,lead_probability
    if (inputType.upper() == "S"):
        demand_probability=[[0,10] , [1,35] , [2,70] , [3,91] , [4,100]]
        lead_probability=[[1,60] , [2,90] , [3,100]]
    else:
        n=int(input("how many lead time possible? "))
        for i in range(n):
            lead_probability.append(input("enter lead time and it's probability like this => time,probability : ").split(','))
            if (i!=0):
                lead_probability[i][1]=int(lead_probability[i][1])+int(lead_probability[i-1][1])
        
        n=int(input("how many demand possible? "))
        for i in range(n):
            demand_probability.append(input("enter demand and it's probability like this => demand,probability : ").split(','))
            if (i!=0):
                demand_probability[i][1]=int(demand_probability[i][1])+int(demand_probability[i-1][1])
    
    for i in range(nCycles*nDaysCycle):
        for j in range(len(demand_probability)):
            if (rn_demand[i]<=int(demand_probability[j][1])):
                demand.append(int(demand_probability[j][0]))
                break
    
    for i in range(len(rn_lead)):
        for j in range(len(lead_probability)):
            if (rn_lead[i]<=int(lead_probability[j][1])):
                leadNumbers.append( int(lead_probability[j][0]))
                break


def getlast(arr,old):
    for j in range(len(arr)-1,-1,-1):
        if (arr[j]!='-'):
            return arr[j]
    return oldOrder[old]


def calculate():
    global start, nCycles, nDaysCycle, capacity
    global startedStock, order, rn_demand, demand, EndedStock, lead, rn_lead, Short ,oldOrder,leadNumbers
        
    startedStock.append(start)
    order.append(oldOrder[1])
    lead.append(oldOrder[0]+1)

    if(startedStock[-1]-demand[0] < 0):
        Short.append(startedStock[0]-demand[0])
        EndedStock.append(0)
    else:
        EndedStock.append(startedStock[-1]-demand[0])
        Short.append(0)

    for i in range(1,nDaysCycle*nCycles):
        if (i==getlast(lead,0)-1):
            if (EndedStock[-1]+getlast(order,1)-Short[-1] >= 0):
                startedStock.append(EndedStock[-1]+getlast(order,1)+Short[-1])
                if (startedStock[-1]-demand[i]>=0):
                    EndedStock.append(startedStock[-1]-demand[i])
                    Short.append(0)
                else:
                    EndedStock.append(0)
                    Short.append(startedStock[-1]-demand[i])
            else:
                startedStock.append(0)
                Short.append(EndedStock[-1]+getlast(order,1)+Short[-1]-demand[i])
                EndedStock.append(0)

            order.append('-')
            lead.append('-')
        
        else:
            startedStock.append(EndedStock[-1])

            if(startedStock[-1]-demand[i] < 0):
                Short.append(startedStock[i]-demand[i]+Short[-1])
                EndedStock.append(0)
            else:
                EndedStock.append(startedStock[i]-demand[i])
                Short.append(0)
            if ( (nDaysCycle-1) == (i%nDaysCycle) ):
                order.append(capacity-EndedStock[i])
                lead.append(i+leadNumbers.pop(0)+2)
            else:
                order.append('-')
                lead.append('-')


def printResultset():
    global start, nCycles, nDaysCycle, capacity
    global startedStock, order, rn_demand, demand, EndedStock, lead, rn_lead, Short ,oldOrder

    import pandas as pd
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    day=range(1,nCycles*nDaysCycle+1)
    table = pd.DataFrame({
        'Day':day,
        'started Stock':startedStock,
        'demand':demand,
        'EndedStock':EndedStock,
        'Short':Short,
        'order':order,
        'arrival day':lead})

    print(table)

    print("Average End of Inventory = ", sum(EndedStock)/(nCycles*nDaysCycle) ,"units")
    
    c=0
    for i in range(0,nCycles*nDaysCycle):
        if (Short[i] != 0):
            c+=1

    print("The number of shortage times = ",c," times out of ",(nCycles*nDaysCycle),"days.")

def startSemolation():

    print("\nNote: all inputs must be from 1 to 100, if you enter number 0 it will be change to 100")
    inputType=input('Generate Random Numbers = G , Use Section Example = S , input Random Numbers = I: ')
    inputType=randomNumbers(inputType)
    ProbabiltyInput(inputType)

    calculate()

    printResultset()


startSemolation()