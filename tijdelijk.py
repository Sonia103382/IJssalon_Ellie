prijzen={
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = 3*0.8
reclame_tekst = (f"vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}")
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
el =reclame_tekst4
el = [reclame_tekst4.lower() for reclame_tekst4 in el]
for i in el:
    if (len (i) >=5):
        print(i.upper())
    else:
        print(i.lower())
        "opnieuw"