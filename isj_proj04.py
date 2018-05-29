#!/usr/bin/env python3
def can_be_a_set_member_or_frozenset(*item):
    """Metoda na zjisteni jestli item muze byt mnozina"""
    #promenna na to jestli item obsabuje zakazany prvek
    naslo = 0
    if type(item) == int:
        return item

    for x in item:
        #kontrola jestli item neobsabuje neco zakazane
        if isinstance(x, (list, set, frozenset, dict)):
            #ulozeni ze byla nalezen zakazany prvek
            naslo = 1
    #jestli to byl zakazany prvek vrati se frozenset
    #jinak se vrati item
    if (naslo):
       return frozenset(*item)
    else:
        naslo = 0
        for x in item:
            if isinstance(x, tuple):
                return tuple(x)
        return int(*item)


def all_subsets(lst):
    """Metoda na vsechny podmnoziny"""
    #vlozime si na zacatku prazdnou mnozinu
    set = [[]]
    #Iterujeme kazdy prvek z listu
    for x in lst:
        #iterace vsech podmnozin
        for y in set:
            # pridani nove podmnoziny skladajici se z podmnoziny a prvku listu
            set =set+ [list(y)+[x]]
    #vratime mnozinu vsech podmnozin
    return set


def all_subsets_excl_empty(*lst, exclude_empty=True):
    """Metoda na vsechny podmnoziny s moznosti smazani prazdne podmnoziny"""
    #metoda funguje pro
    #overeni jestli je nutnost k smazani prazdne podmnoziny
    #pokud je zadan all_subsets_excl_empty bez exclude empty parametru je tedy true a vymaze
    #pokud je zadan all_subsets_excl_empty s false tak se nastaví exclude empty na false a nesmaze ho
    #pokud je zadan all_subsets_excl_empty s true tak zůstane stále true a vymaze prazdnou mnozinu
    if (exclude_empty):
        #pouzijeme metodu all_subsets
        set=all_subsets(lst)
        #smazeme prazdnou mnozinu
        set.remove([])
        #vratime nasi mnozinu
        return set
    #pokud bylo exclude empty nastaveno na false funguje stejne jako all_subsets
    return all_subsets(lst)
