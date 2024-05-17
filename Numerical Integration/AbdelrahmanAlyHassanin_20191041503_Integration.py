#Abdelrahman Aly Hassanin
#20191041503

f=input("enter the function ex(x**3): ")
Xrn=input("enter RN for x ex(22,25,18,45,25,27,48,43,40,47,38,33,24,47,42,25,33,50,34,21): ").split(",")
Yrn=input("enter RN for y ex(57,18,0,90,5,77,66,10,76,42,78,88,3,9,77,16,27,60,29,40): ").split(",")
start=float(input("enter start of integration ex(2): "))
end=float(input("enter end of integration ex(5): "))

max=float( eval(f.replace('x',str(end))) + 1 )
area=(end-start)*max

for i in range(len(Xrn)):
    Xrn[i]=int(Xrn[i])
    Yrn[i]=int(Yrn[i])

Xcoordinate=[]
Ycoordinate=[]
func=[]
m=[]
n=[]

for i in range(len(Xrn)):
    Xcoordinate.append( Xrn[i]/10 )
    Ycoordinate.append( (Yrn[i]/100) * max)
    func.append( eval(f.replace('x',str(Xcoordinate[-1]))) )

    if (Xcoordinate[-1]<start or Xcoordinate[-1]>end):
        m.append(0)
        n.append(0)

    else:
        n.append(1)

        if ( func[-1] < Ycoordinate[-1] ):
            m.append(0)
        else:
            m.append(1)

irregular=( sum(m)/sum(n) ) * area


import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

table = pd.DataFrame({'function':[f],
                ' start':[start],
                ' end':[end],
                ' area':[area],
                ' irregular':[irregular],
                ' M':[sum(m)],
                ' N':[sum(n)]})
print('\n\n',table,'\n\n')

table2 = pd.DataFrame({'Random Number for X':Xrn,
                ' X coordinate':Xcoordinate,
                ' Random Number for Y':Yrn,
                ' Y coordinate':Ycoordinate,
                ' '+f:func,
                ' M':m,
                ' N':n})
print(table2,'\n')