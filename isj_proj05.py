#!/usr/bin/env python3
import collections
from math import factorial

class Polynomial:
    """Trida pro polynomy"""
    def __new__(cls, *args, **kwargs):
        """Vytvoreni noveho objektu"""
        return super().__new__(cls)

    def __init__(poly, *args, **kwargs):
        """Vlozeni argumetnu do listu"""
        #vytvoreni listu se lisi podle vstupu
        poly.__listargumentu=[]
        if ((len(args) == 1) and (type(args[0]) == list) and (len(kwargs) == 0)):
            poly.__listargumentu=args[0]

        elif ((len(args) == 0) and (len(kwargs) != 0)):
            n = 0
            arglist = collections.OrderedDict(sorted(kwargs.items()))
            for x, y in arglist.items():
                while n != int(x[1:]):
                    n += 1
                    poly.__listargumentu.append(0)
                n += 1
                poly.__listargumentu.append(y)


        elif ((len(args) != 0) and (len(kwargs) == 0)):
            for x in args:
                poly.__listargumentu.append(x)
        for x in poly.__listargumentu[::-1]:
            if((x == 0) and (len(poly.__listargumentu) != 1)):
                poly.__listargumentu.pop()
            else:
                break


    def __eq__(poly, druhy):
        """Porovnani v´dvou polonymu"""
        #Bud true nebo false
        rovnost = (poly.__toString(poly.__listargumentu) == str(druhy))
        return rovnost
    def __add__(poly, druhy):
        """Scitani polynomu"""
        prvniL=poly.__listargumentu
        druhyL=druhy.hodnoty()

        if(len(prvniL)>len(druhyL)):
            prvniL, druhyL = druhyL, prvniL
        n = 0
        vysledek = []
        delka=len(druhyL) - len(prvniL)

        for x in range(delka): prvniL.append(0)
        for x in prvniL: vysledek.append(x + druhyL[n]); n += 1
        return poly.__toString(vysledek)
    def __str__(poly):
        """Prevod na rovnice ve tvaru retezce"""
        return poly.__toString(poly.__listargumentu)

    def __pow__(poly,exponent):
        """Vynasobeni polynomu cislem"""
        n = exponent
        a=poly.__listargumentu[1]
        b = poly.__listargumentu[0]
        cnr = lambda n, r: factorial(n) / (factorial(r) * factorial(n - r))
        listvysledku=[]
        for r in range(n + 1):
            coff = str(cnr(n, r))
            listvysledku.append(int(float(coff*(a**(n-r))) * float(b**r)))

        return poly.__toString(listvysledku[::-1])


    def hodnoty(druhy):
        """Scitani polynomu"""
        return druhy.__listargumentu

    def derivative(poly):
        """Derivace polynomu"""
        vysledek = []
        if (len(poly.__listargumentu) == 1):
            vysledek.append(0)
        for i in range(1, len(poly.__listargumentu)): vysledek.append(i *poly.__listargumentu[i])
        vys=Polynomial(vysledek)
        return vys

    def __vysledekpolynomu(poly, poc):
        """Vypocet polynomu pri zadane hodnote"""
        vysledek = 0
        exponent = len(poly.__listargumentu) - 1
        for x in poly.__listargumentu[::-1]:  vysledek += x * poc ** exponent; exponent -= 1
        return vysledek

    def at_value(poly, *args):
        """Pri zadanem jednom argumentu vraci hodnotu a pri druhem jejich rozdil"""
        if(len(args) == 0):
            return 0

        elif(len(args) == 1):
            return poly.__vysledekpolynomu(args[0])

        elif(len(args) == 2):
            return (poly.__vysledekpolynomu(args[1]) - poly.__vysledekpolynomu(args[0]))

    def __toString(poly, listargumentu):
        """Prevod na rovnice ve tvaru retezce"""

        prvnicislo = True
        rovnice = ""
        exponent = len(listargumentu)-1

        for x in listargumentu[::-1]:
            if(x < 0 and prvnicislo):
                prvnicislo = False
                rovnice += " - "
            elif(prvnicislo):
                prvnicislo = False
            #pro dalsi argumenty
            elif (x < 0 and (prvnicislo == False)):
                rovnice += " - "
            elif(x > 0 and (prvnicislo == False)):
                rovnice += " + "
            x = abs(x)

            if((exponent == 0) and (len(poly.__listargumentu) == 1) or (exponent == 0) and x):
                rovnice +=str(x)
            elif(x == 0):

                rovnice +=""

            elif(exponent == 1):

                if(x == 1):
                    rovnice += "x"
                else:
                    rovnice+=str(x)+"x"
            else:

                if(x == 1):
                    rovnice += "x^" + str(exponent)
                else:
                    rovnice += str(x) + "x^" + str(exponent)


            exponent -= 1

        return rovnice





