#Abdelrahman Aly Hassanin
#20191041503

rn_NT_Example=[85,31,72,23,75,37,44,17,43,11]
rn_demand_Example=[3,38,65,88,96,23,8,54,14,16]

global n, dailyNewspapers, NPsCost, price, scrap,inputType
global day, rn_NT, rn_demand, newsType, demand, salesRevenue, lostProfit, scarpRevenue, daylyProfit

day=[]
rn_NT=[]
rn_demand=[]
newsType=[]
demand=[]
salesRevenue=[]
lostProfit=[]
scarpRevenue=[]
daylyProfit=[]

def generateRN():
    global n,rn_NT,rn_demand
    n=int(input("Enter Number of Days 'example(10)': "))
    import random
    for i in range(n):
        rn_NT.append(int(random.uniform(0,100)))
        rn_demand.append(int(random.uniform(0,100)))

def inputVariables():
    global dailyNewspapers,NPsCost,scrap,price

    dailyNewspapers=int(input("Enter Number of Daily Newspapers Purchased 'example(70)': "))
    NPsCost=dailyNewspapers*-int(input("Enter the Cost of Newspaper (cent) 'example(33)': "))
    price=int(input("Enter the price of Newspaper (cent) 'example(50)': "))
    scrap=int(input("Enter the price of scrap Newspaper (cent) 'example(5)': "))

def inputRN():
    global rn_NT,rn_demand,n
    rn_NT=input("ُEnter Type of News random Numbers like(85,31,72,23,75,37,44,17,43,11) : ").split(",")
    rn_demand=input("ُEnter Demand random Numbers like(3,38,65,88,96,23,8,54,14,16) : ").split(",")
    n=len(rn_NT)
    for i in range(n):
        rn_NT[i]=int(rn_NT[i])
        rn_demand[i]=int(rn_demand[i])

def randomNumbers(status):
    global rn_NT,rn_demand,n,dailyNewspapers,NPsCost,price,scrap,inputType
    status=str(status)
    match status.upper():
        case "S":
            rn_NT=rn_NT_Example
            rn_demand=rn_demand_Example
            n=10
            dailyNewspapers=70
            NPsCost=-33*dailyNewspapers
            price=50
            scrap=5
            return
        case "G":
            inputVariables()
            generateRN()
            return
        case "I":
            inputVariables()
            inputRN()
            return 
        case _:
            print("invaled input")
            inputType=input('Generate Random Numbers = G , Use Section Example = S , input Random Numbers = I: ')
            randomNumbers(inputType)
            return

def NT_Probabilty():
    global newsType , rn_NT,n,inputType

    if (inputType.upper()=='S'):
        NTs='Good,Fair,Poor'.split(",")
        NTs_probability='35,45,20'.split(",")
    else:
        NTs=input("ُEnter News types like(Good,Fair,Poor) : ").split(",")
        NTs_probability=input("Enter News types probabilities like(35,45,20) : ").split(",")
    
    if len(NTs_probability)==len(NTs):

        for i in range(len(NTs_probability)):
            NTs_probability[i]=int(NTs_probability[i])

        NTs_probabilityRange=[-1]*len(NTs_probability)
        NTs_probabilityRange[0]=NTs_probability[0]-1

        for i in range(1,len(NTs_probability)):
            NTs_probabilityRange[i]=NTs_probability[i]+NTs_probabilityRange[i-1]

        for j in range(n):
            for k in range(len(NTs)):
                if (rn_NT[j]<=NTs_probabilityRange[k]):
                    newsType.append(NTs[k])
                    break
        
        demand_Probabilty(NTs)
    else:
        print("invaled input")
        NT_Probabilty()


def demand_Probabilty(NTs):
    global newsType,rn_demand,demand,n,inputType

    demandProbability=[[]]*len(NTs)

    if (inputType.upper()=='S'):
        demandList='40,50,60,70,80,90,100'.split(",")
    else:
        demandList=input("ُEnter all possible daily demand like(40,50,60,70,80,90,100) : ").split(",")


    if (inputType.upper()=='S'):
        demandProbability[0]='3,5,15,20,35,15,7'.split(",")
        demandProbability[1]='10,18,40,20,8,4'.split(",")
        demandProbability[2]='44,22,16,12,6'.split(",")
    else:
        print("section Example: \ngood like(3,5,15,20,35,15,7)\nfair like(10,18,40,20,8,4)\npoor like(44,22,16,12,6)")
        for i in range(len(NTs)):
            demandProbability[i]=input("Enter demand probabilities for {} news : ".format(NTs[i])).split(",")


    
    for i in range(len(NTs)):
        for j in range(len(demandProbability[i])):
            demandProbability[i][j]=int(demandProbability[i][j])

            if(j>0):
                demandProbability[i][j]+=demandProbability[i][j-1]
            else:
                demandProbability[i][j]=demandProbability[i][j]-1
    
    for i in range(n):
        for j in range(len(NTs)):
            if (newsType[i].upper()==NTs[j].upper()):
                for k in range(len(demandProbability[j])):
                    if (rn_demand[i]<=demandProbability[j][k]):
                        demand.append(int(demandList[k]))
                        break
    

def calculate():
    global n, price, scrap,dailyNewspapers,NPsCost
    global demand, salesRevenue, lostProfit, scarpRevenue, daylyProfit

    for i in range(n):
        store=dailyNewspapers-demand[i]

        if (store >= 0):
            salesRevenue.append(demand[i]*price)

            scarpRevenue.append(store * scrap )
            lostProfit.append(0)
        else:
            salesRevenue.append(dailyNewspapers*price)

            lostProfit.append( store * 17)
            scarpRevenue.append(0)
        
        daylyProfit.append( (salesRevenue[i]+scarpRevenue[i]+lostProfit[i]+NPsCost)/100 )


def printResultset():
    global dailyNewspapers, NPsCost, price, scrap
    global day, rn_NT, rn_demand, newsType, demand, salesRevenue, lostProfit, scarpRevenue, daylyProfit

    import pandas as pd
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    table = pd.DataFrame({'Daily Newspapers (cent)':[dailyNewspapers],
                    ' Daily Newspapers Cost (cent)':[NPsCost],
                    ' Newspapers Price (cent)':[price],
                    ' Scrap Price (cent)':[scrap],
                    ' total Profit ($)':[sum(daylyProfit)]})
    print('\n\n',table,'\n\n')

    table2 = pd.DataFrame({'Day':day,
                    ' RN News Type':rn_NT,
                    ' News Types':newsType,
                    ' RN Demand':rn_demand,
                    ' Demand':demand,
                    ' Sales Revenue (cent)':salesRevenue,
                    ' lost Profit (cent)':lostProfit,
                    ' Scarp Revenue (cent)':scarpRevenue,
                    ' Dayly Profit ($)':daylyProfit})
    print(table2)


def startSemolation():
    global n, dailyNewspapers, NPsCost, price, scrap , inputType
    global day, rn_NT, rn_demand, newsType, demand, salesRevenue, lostProfit, scarpRevenue, daylyProfit


    print("Note: all inputs must be from 0 to 99")
    inputType=input('Generate Random Numbers = G , Use Section Example = S , input Random Numbers = I: ')
    randomNumbers(inputType)
    NT_Probabilty()


    for i in range(n):
        day.append(i+1)

    calculate()

    printResultset()


startSemolation()