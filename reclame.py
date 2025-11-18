from algemene_functies import mijn_functie2
def aanbieding_1(smaak,prijs,korting):
    uitvoer = f"vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {(prijs)-korting*(prijs)} euro."
    return uitvoer
print(aanbieding_1("aardbei",4,0.1))   
def inkomsten_totaal(inkomsten):
    [inkomsten]
    btw = inkomsten * 0.09
    uitvoer = f"het totaal van alle inkomsten deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden."
    return uitvoer
print (inkomsten_totaal(220+430+125+160+205+90+345))
def laag_en_hoog(mijn_lijst):
    uitvoer = max(mijn_lijst), min(mijn_lijst)
    return uitvoer
print (laag_en_hoog([220,430,125,160,205,90,345]))
def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
    gemiddelde = totaal / aantal
    return f"de gemiddelde inkomsten deze week zijn {gemiddelde} euro."
print (gemiddelde([220,430,125,160,205,90,345]))
def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer
print (meervoudig([10,5,3,2,1,2,9]))
def combinatie(invoer_lijst_2,):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie2(korte_lijst[0],korte_lijst[1])
    return uitvoer
print (combinatie([12,3,5,14]))