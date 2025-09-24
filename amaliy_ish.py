def moon(year, month):
    months1=[31,28,31,30,31,30,31,31,31,31,30,31]
    months2=[31,29,31,30,31,30,31,31,31,31,30,31]
    if year%4==0:
        return sum(months1), months1[month - 1]
    elif year%4!=0:
        return sum(months2), months2[month - 1]
    

print(moon(1233,4))