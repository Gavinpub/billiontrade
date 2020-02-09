import sys
import numpy as np

#for v in sys.argv:
#    print(v)

if len(sys.argv) < 2:
    print ("Please specify data file, like as : python trailrun.py datafile.txt")
    #exit()

datafile = "data/test.txt"#sys.argv[1]
startyear = '2018'
STATUS_EMPTY = 1
STATUS_UP_MA20 = 2
STATUS_UP_DAY1 = 3
STATUS_UP_DAY2 = 4
STATUS_UP_DAY3 = 5
STATUS_UP_

priceList = []
actionList = []

class DayPrice:
    date = ""
    price = 0.0
    ma5 = 0.0
    ma10 = 0.0
    ma20 = 0.0

class Action:
    act = "none"
    date = ""
    price = ""
    delta = 0

def loadData(line):
    date = line.split(',')[0]
    price = line.split(',')[4]
    day = DayPrice()
    day.date = date
    day.price = float(price)
    priceList.append(day)

def calMA():
    latestPrices = []
    for i in range(len(priceList)):
        latestPrices.append(priceList[i].price)
        latestPrices = latestPrices[-20:]

        priceList[i].ma5 = np.mean(latestPrices[-5:])
        priceList[i].ma10 = np.mean(latestPrices[-10:])
        priceList[i].ma20 = np.mean(latestPrices[-20:])


def trade():
    count = len(priceList)
    for i in range(count):
        if int(priceList[i].date[:4]) >= int(startyear):
            if noStock :
                # Check buy-in point
                if priceList[i].ma5 > priceList[i].ma20 and priceList[i-1].ma5 <= priceList[i-1].ma20 and \
                    (priceList[i+1].price > priceList[i].price and priceList[i+2].price > priceList[i+1].price):
                    op = Action()
                    op.date = priceList[i+1].date
                    op.act = "Buy"
                    op.price = priceList[i+1].price
                    op.delta = 0

                    noStock = False
            else: # Check sell-out point
                if priceList[i].ma5 < priceList


#Loading data from file
df = open(datafile, 'r')
lineone = df.readline()
stockname = lineone.split(" ")[1]
print("Analyzing stock ", stockname)
print("-" * 40)
df.readline() # read the head line
lines = df.readlines()
for line in lines[:len(lines)-1]:
    loadData(line)
df.close()

#Calculate MA
calMA()

#Print data
for day in priceList:
        print("Date:%s, Price:%.2f, MA5:%.2f, MA10:%.2f, MA20:%.2f"%(day.date, day.price, day.ma5, day.ma10, day.ma20))