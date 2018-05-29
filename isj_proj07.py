#!/usr/bin/env python3

class TooManyCallsError(Exception):
    """Trida pro  decoratory"""
    pass
def limit_calls(max_calls=2,error_message_tails='called too often'):
    """Log"""
    def decorate(funkce):
        def wrapper(*args):
            wrapper.calls += 1
            if wrapper.calls >max_calls:
                raise TooManyCallsError("function \"" + str(funkce.__name__) + "\" - " + error_message_tails)
            return funkce(*args)

        wrapper.calls = 0
        return wrapper

    return decorate
class Log():
    """Vypis logu"""
    def __init__(log,nazev):
        """Init"""
        log.__soubor= open(nazev,'w')
    def __enter__(log):
        """Zacatek"""
        log.__soubor.write("Begin"+'\n')
        return log
    def __exit__(log, exc_type, exc_val, exc_tb):
        """Konec"""
        log.__soubor.write("End"+'\n')
        log.__soubor.close()
    def logging(log,nazev1):
        """Vnitrni vypis"""
        log.__soubor.write(nazev1 + '\n')
def ordered_merge(*pole,**sel):
    """Vraceni listu cisel"""
    select=[]
    vysledky=[]
    listy=[]
    if 'selector' not in sel:
        return select
    else:
        select = sel["selector"]
    for i in pole:
        listy.append(list(i))
    for a in select:
        vysledky.append(listy[a][0])
        listy[a].remove(listy[a][0])
    return vysledky