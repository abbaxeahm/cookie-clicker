from math import ceil


class largeNumber:
    def __init__(self, significand: float, exp: int):
        self.significand = significand
        self.exp = exp

    def updateNum(self):
        if self.significand == 0.0:
            self.exp = 0
        elif self.significand >= 1000:
            self.significand /= 1000
            self.exp += 1
        elif self.significand < 1:
            self.significand *= 1000
            self.exp -= 1

    def add(self, term):
        self.significand += term.significand * pow(1000, term.exp - self.exp)

    def sub(self, term):
        print(self.significand)
        print(term.significand)
        if self.exp > term.exp or (self.significand >= term.significand and self.exp == term.exp):
            self.significand -= (term.significand *
                                 pow(1000, term.exp - self.exp))
            return True
        else:
            return False

    def overWrite(self, significand: float, exp: int):
        self.significand = significand
        self.exp = exp


total = largeNumber(0.0, 0)
addPerSec = largeNumber(0.0, 0)
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


def buy(price: largeNumber):
    if total.sub(price):
        print("ny monster")


def perSecUpdate():
    global total
    global addPerSec
    total.add(addPerSec)  # * deltaTime(s)
    total.updateNum()
    addPerSec.updateNum()
    printNum(total)
    printNum(addPerSec)


def printNum(num: largeNumber):
    print(end="1000exp: ")
    print(num.exp)
    print(end="10exp: ")
    print(num.exp*3)
    if num.exp == 1:
        print(int(round(1000 * num.significand)))
    elif num.exp == 0:
        print("%.3f" % round(num.significand, 3))
    elif num.exp < 22:
        print("%.3f" % round(num.significand, 3), end=" ")
        # print(nameOftotalExp[num[1]])
        print(nameOfnumber10[ceil((num.exp-1)/2)-1] +
              ("illion" if num.exp % 2 == 0 else "illiard"))
    elif num.exp < 2000:
        print(ceil((num.exp+1)/2-1))
        s = str(ceil((num.exp+1)/2-1))[::-1]
        print(s)
        print("%.3f" % round(num.significand, 3), end=" ")
        count = 0
        for c in s:
            if int(c) > 0:
                print(nameOfnumber[count][int(c)-1], end="")
            count += 1
        print(("illion" if num.exp % 2 == 0 else "illiard"))
    else:
        print("to large")


while True:
    addPerSec.overWrite(float(input("add per sec")),
                        int(input("add per sec exp")))
    if input() != "":
        buy(largeNumber(1, int(input("buy: "))))
    perSecUpdate()
