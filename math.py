from math import ceil
total = [0.0, 0]
addPerSec = [0.0, 0]
nameOfnumber10 = ["M", "B", "Tr", "Quadr",
                  "Quint", "Sext", "Sept", "Oct", "Non", "Dec"]

nameOfnumber = [["Un", "Duo", "Tre", "Quattuor", "Quinqua", "Se", "Septe", "Octo", "Nove"],
                ["Deci", "Viginti", "Triginta", "Quadraginta", "Quinquaginta",
                    "Sexaginta", "Septuaginta", "Octoginta", "Nonaginta"],
                ["Centi", "Duocenti", "Trecenti", "Quadringenti", "Quingenti",
                "Sescenti", "Septingenti", "Octingenti", "Nongenti"]]

# 1	Un	N Deci	NX Centi
# 2	Duo	MS Viginti	N Ducenti
# 3	Tre(*)	NS Triginta	NS Trecenti
# 4	Quattuor	NS Quadraginta	NS Quadringenti
# 5	Quinqua	NS Quinquaginta	NS Quingenti
# 6	Se(*)	N Sexaginta	N Sescenti
# 7	Septe(*)	N Septuaginta	N Septingenti
# 8	Octo	MX Octoginta	MX Octingenti
# 9	Nove(*)	Nonaginta	Nongenti


def buy(price):
    global total
    if affordeble(price):
        total[0] -= getSignificandOfTerm1Exp(total[1], price)


def affordeble(price):
    return total[1] > price[1] or total[0] >= price[0]


def getSignificandOfTerm1Exp(term1Exp, term2):
    return term2[0] * pow(1000, term2[1] - term1Exp)


def updateNum(num):
    if num[0] == 0.0:
        return [0.0, 0]
    elif num[0] >= 1000:
        return [num[0] / 1000, num[1] + 1]
    elif num[0] < 1:
        return [num[0] * 1000, num[1] - 1]
    else:
        return num


def perSecUpdate():
    global total
    global addPerSec
    total[0] += getSignificandOfTerm1Exp(total[1], addPerSec)  # * deltaTime(s)
    total = updateNum(total)
    addPerSec = updateNum(addPerSec)
    printNum(total)
    printNum(addPerSec)


def printNum(num):
    print(end="1000exp: ")
    print(num[1])
    print(end="10exp: ")
    print(num[1]*3)
    if num[1] == 1:
        print(int(round(1000 * num[0])))
    elif num[1] == 0:
        print("%.3f" % round(num[0], 3))
    elif num[1] < 22:
        print("%.3f" % round(num[0], 3), end=" ")
        # print(nameOftotalExp[num[1]])
        print(nameOfnumber10[ceil((num[1]-1)/2)-1] +
              ("illion" if num[1] % 2 == 0 else "illiard"))
    elif num[1] < 2000:
        print(ceil((num[1]+1)/2-1))
        s = str(ceil((num[1]+1)/2-1))[::-1]
        print(s)
        count = 0
        for c in s:
            if int(d) > 0:
                print(nameOfnumber[count][int(c)-1], end="")
            count += 1
        print(("illion" if num[1] % 2 == 0 else "illiard"))
    else:
        print("to large")


while True:
    addPerSec[0] = float(input("add per sec"))
    addPerSec[1] = int(input("add per sec exp"))
    if input() != "":
        buy([1, int(input("buy: "))])
    perSecUpdate()
