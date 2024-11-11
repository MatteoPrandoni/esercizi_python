tupla_vendite = (
                (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
                (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
                (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
                (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )

def media_globale(tupla_vendite):
    media=0
    cont=0
    for materia, prodotto in tupla_vendite:
        media+=prodotto[1][1]
        cont+=1
    return media/cont

def media(tupla_vendite,categoria,tipo_pagamento):
    media=0
    cont=0
    for materia, prodotto in tupla_vendite:
        if(materia[1]==categoria and prodotto[1][0]==tipo_pagamento):
            media+=prodotto[1][1]
            cont+=1
    return media/cont

def venditaMax(tupla_vendite):
    max=0
    valori_max=[]
    #trovo il valore massimo
    for materia, prodotto in tupla_vendite:
        if(prodotto[1][1]>max):
            max=prodotto[1][1]
    #riempimento dell'array valori_max
    for materia, prodotto in tupla_vendite:
        if(prodotto[1][1]==max):
            valori_max.append(prodotto[0])
    return(max,valori_max)

def venditaMin(tupla_vendite):
    min=1000000
    for materia, prodotto in tupla_vendite:
        if(materia[0]=="RepartoA" and prodotto[1][1]<min):
            min=prodotto[1][1]
    return min
            
def venditaPer(tupla_vendite):
    somma_totale=0
    somma_repartoA=0
    somma_repartoB=0
    for materia, prodotto in tupla_vendite:
        somma_totale+=prodotto[1][1]
        if(materia[0]=="RepartoA"):
            somma_repartoA+=prodotto[1][1]
        elif(materia[0]=="RepartoB"):
            somma_repartoB+=prodotto[1][1]
    return((somma_repartoA/somma_totale)*100,(somma_repartoB/somma_totale)*100)
    
scelta=0
while(True):
    print("\n1-Media totale")
    print("2-Media inserendo categoria e tipo di pagamento")
    print("3-Visualizza i dettagli della vendita massima")
    print("4-Visualizza la vendita minima del reparto A")
    print("5-Visualizza la percentuale delle vendite per reparto rispetto al totale")
    print("6-Termina programma")
    while(True):
        scelta=int(input("\nInserisci la tua scelta: "))
        if(scelta>=0 and scelta<=6):
            break
    if(scelta==1):
        #implementazione richiesta 1
        print(f"\nMedia globale: {media_globale(tupla_vendite):.2f}")
    elif(scelta==2):
        #implementazione richiesta2
        categoria=str(input("\nInserisci la categoria: "))
        #validazione input tipo_pagamento
        while(True):
            tipo_pagamento=str(input("Inserisci il tipo di pagamento ('contanti' o 'carta di credito'): "))
            if(tipo_pagamento=="contanti" or tipo_pagamento=="carta di credito"):
                break
        #controllo se i dati inseriti sono nella tupla_vendite (se si a=True, se no a=False)
        dati_presenti=False
        for materia, prodotto in tupla_vendite:
                if(materia[1]==categoria and prodotto[1][0]==tipo_pagamento):
                    dati_presenti=True
        if(dati_presenti):
            print(f"\nLa media per i prodotti di categoria {categoria} pagati in {tipo_pagamento} è {media(tupla_vendite,categoria,tipo_pagamento):.2f}")
        else:
            print(f"\nERRORE! Categoria o tipo di pagamento errati!")
    elif(scelta==3):
        #implementazione richiesta3
        print(f"\nValore massimo: {venditaMax(tupla_vendite)[0]} del/i prodotto/i: {venditaMax(tupla_vendite)[1]} ")
    elif(scelta==4):
        #implementazione richiesta4
        print(f"\nValore minimo del repartoA: {venditaMin(tupla_vendite)}")
    elif(scelta==5):
        #implementazione richiesta5
        print(f"\nPercentuale vendite repartoA: {venditaPer(tupla_vendite)[0]:.2f}%")
        print(f"Percentuale vendite repartoB: {venditaPer(tupla_vendite)[1]:.2f}%")
    else:
        break

