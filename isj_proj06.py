#!/usr/bin/env python3

import collections


def first_nonrepeating(string1):
    """Prvni neopakujici se znak v řetězci"""
    if(string1==' '):
        return None
    elif(string1=='\t'):
        return None
    if(type(string1)==str):
        results = collections.Counter(string1)
        for k, v in results.items():
            if (v == 1):
                return (k)
    return None
def combine4(*listCisel):
    """Kombinace 4 čísel do jednoho"""
    if(type(listCisel[0])!=list or type(listCisel[1])!=int):
        return None
    for x in listCisel[0]:
        if(type(x)!=int):
            return None

    operatory=['+','-','*','/']
    vysledek=[]

    for i in range(10):
        for y in range(len(listCisel[0])):
            rovnice=""
            if(i==0): rovnice+="("
            elif(i==1):rovnice+="("
            elif(i==2):rovnice+="("
            elif(i==3):rovnice+="(("
            elif(i==4):rovnice+="("
            #ted pridame cisla
            rovnice += str(listCisel[0][y])
            for a in operatory:
                rovnice1=rovnice
                rovnice1+=a
                if(i==4):rovnice1+="("
                elif(i==6):rovnice1+="("
                elif(i==7):rovnice1+="("
                elif(i==8):rovnice1+="(("
                elif(i==9):rovnice1+="("

                range1=list(range(0,4))
                range1.remove(y)

                for z in range1:
                    rovnice2=rovnice1
                    rovnice2 += str(listCisel[0][z])
                    if(i==0):rovnice2+=")"
                    elif(i==1):rovnice2+=")"
                    elif(i==3):rovnice2+=")"
                    for c in operatory:
                        rovnice3 = rovnice2
                        rovnice3 += c
                        if(i==1):rovnice3+="("
                        elif(i==5):rovnice3+="("
                        elif(i==9):rovnice3+="("
                        cisla3 =list(range(0,4))

                        cisla3.remove(y)
                        cisla3.remove(z)

                        for h in cisla3:
                            rovnice4 = rovnice3
                            rovnice4 += str(listCisel[0][h])
                            if(i==2):rovnice4+=")"
                            elif(i==3):rovnice4+=")"
                            elif(i==4):rovnice4+="))"
                            elif(i==6):rovnice4+=")"
                            elif(i==8):rovnice4+=")"
                            for l in operatory:
                                rovnice5 = rovnice4
                                rovnice5 += l
                                cisla4 = list(range(0, 4))
                                cisla4.remove(y)
                                cisla4.remove(z)
                                cisla4.remove(h)
                                rovnice6 = rovnice5
                                rovnice6 += str(listCisel[0][cisla4[0]])
                                if(i==1):rovnice6+=")"
                                elif(i==5):rovnice6+=")"
                                elif(i==7):rovnice6+=")"
                                elif(i==8):rovnice6+=")"
                                elif(i==9):rovnice6+="))"
                                vysledek.append(rovnice6)

    vysledek2 = []
    for o in vysledek:
        try:vysledekRovnice = eval(o)
        except ZeroDivisionError: continue
        if(vysledekRovnice == listCisel[1]): vysledek2.append(o)


    return sorted(set(vysledek2))