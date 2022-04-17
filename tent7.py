from math import ceil
from time import sleep
a = "444"
b = True
powerOf1000 = 0
addPerSec = 0
addPerSecExp = 0
startOfNumber = 1.0
nameOfpowerOf1000 = ["",
                     "",
                     "million",
                     "billion",
                     "trillion",
                     "quadrillion",
                     "quintillion"]
nameOfnumber10 = ["M", "B", "Tr", "Quadr",
                  "Quint", "Sext", "Sept", "Oct", "Non", "Dec"]

nameOfnumber = [["Un", "Duo", "Tre", "Quattuor", "Quinqua", "Se", "Septe", "Octo", "Nove"],
                ["Deci", "Viginti", "Triginta", "Quadraginta", "Quinquaginta",
                    "Sexaginta", "Septuaginta", "Octoginta", "Nonaginta"],
                ["Centi", "Duocenti", "Trecenti", "Quadringenti", "Quingenti",
                "Sescenti", "Septingenti", "Octingenti", "Nongenti"]]
grammar = {""}

# 1	Un	N Deci	NX Centi
# 2	Duo	MS Viginti	N Ducenti
# 3	Tre(*)	NS Triginta	NS Trecenti
# 4	Quattuor	NS Quadraginta	NS Quadringenti
# 5	Quinqua	NS Quinquaginta	NS Quingenti
# 6	Se(*)	N Sexaginta	N Sescenti
# 7	Septe(*)	N Septuaginta	N Septingenti
# 8	Octo	MX Octoginta	MX Octingenti
# 9	Nove(*)	Nonaginta	Nongenti

illion = "illion"
illiard = "illiard"
longScale = False


def affordable(price, priceExp):
    global startOfNumber
    print(startOfNumber, powerOf1000)
    if powerOf1000 > priceExp or startOfNumber >= price:
        startOfNumber -= price * pow(1000, priceExp - powerOf1000)
        print(price * pow(1000, priceExp - powerOf1000))


while True:
    # sleep(1)
    addPerSec = float(input("add per sec"))
    addPerSecExp = int(input("add per sec exp"))
    # startOfNumber += addPerSec * pow(1000, addPerSecExp - powerOf1000)

    if startOfNumber == 0:
        powerOf1000 = 0
    elif startOfNumber >= 1000:
        startOfNumber /= 1000
        powerOf1000 += 1
    elif startOfNumber < 1:
        startOfNumber *= 1000
        powerOf1000 -= 1

    if addPerSec == 0:
        addPerSecExp = 0
    elif addPerSec >= 1000:
        addPerSec /= 1000
        addPerSecExp += 1
    elif addPerSec < 1:
        addPerSec *= 1000
        addPerSecExp -= 1

    if powerOf1000 == 1:
        print(int(1000 * round(startOfNumber)))
    elif powerOf1000 == 0:
        print("%.3f" % round(startOfNumber, 3))
    elif powerOf1000 < 22:
        print("%.3f" % round(startOfNumber, 3), end=" ")
        # print(nameOfpowerOf1000[powerOf1000])
        print(nameOfnumber10[ceil((1+powerOf1000)/2)-2] +
              (illion if powerOf1000 % 2 == 0 else illiard))

    print(end="persec: ")
    print(addPerSecExp)
    print(addPerSecExp*3)
    if addPerSecExp == 1:
        print(int(1000 * round(addPerSec)))
    elif addPerSecExp == 0:
        print("%.3f" % round(addPerSec, 3))
    elif addPerSecExp < 22:
        print("%.3f" % round(addPerSec, 3), end=" ")
        # print(nameOfpowerOf1000[addPerSecExp])
        print(nameOfnumber10[ceil((addPerSecExp-1)/2)-1] +
              (illion if addPerSecExp % 2 == 0 else illiard))
    elif addPerSecExp < 2000:
        print(ceil((addPerSecExp+1)/2-1))
        print(str(ceil((addPerSecExp+1)/2-1))[::-1])
        s = str(ceil((addPerSecExp+1)/2-1))[::-1]
        count = 0
        for d in s:
            if int(d) > 0:
                print(nameOfnumber[count][int(d)-1], end="")
            count += 1
        print((illion if addPerSecExp % 2 == 0 else illiard))
    else:
        print("millinillion")
    if powerOf1000 == 4 and b:
        affordable(1, 4)
        b = False
# Quintrigintilliard
