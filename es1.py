dati_pioggia=[
    ("Milano",[("gennaio",15),("febbraio",12),("marzo",14),("aprile",20),("maggio",11),("giugno",8),("luglio",7),("agosto",7),("settembre",11),("ottobre",16),("novembre",18),("dicembre",21)]),
    ("Brescia",[("gennaio",13),("febbraio",15),("marzo",14),("aprile",17),("maggio",9),("giugno",6),("luglio","N/D"),("agosto",4),("settembre",7),("ottobre",12),("novembre",14),("dicembre",17)]),
    ("Bergamo",[("gennaio","N/D"),("febbraio",12),("marzo",14),("aprile",13),("maggio",10),("giugno",6),("luglio","N/D"),("agosto",8),("settembre",11),("ottobre",17),("novembre",18),("dicembre",23)])
    ]

def analizza_citta(input_citta):
    media=0
    cont=0
    max=0
    min=100000
    lista_max=[]
    lista_min=[]
    for citta,dati in dati_pioggia:
        if(citta==input_citta):
            #calcolo della media
            for mese,valore in dati:
                if(valore!="N/D"):
                    media+=valore
                    cont+=1
                    if(valore>max):
                        max=valore
                        lista_max=[mese]
                    elif(valore==max):
                        lista_max.append(mese)
                    if(valore<min):
                        min=valore
                        lista_min=[mese]
                    elif(valore==min):
                        lista_min.append(mese)
    media/=cont
    return (media,(max,lista_max),(min,lista_min))
      

input_citta=str(input("Inserisci il nome della città: "))
a=False  #per verificare che la citta inserita in input sia nella lista dati_pioggia
for citta,*dati in dati_pioggia:
    if(citta==input_citta):
        a=True

if(a==True):#la città è presente
    print(f"Pioggia (in mm): {analizza_citta(input_citta)[0]:.2f}")
    print(f"Valore max: {analizza_citta(input_citta)[1][0]} registrata nel/i mese/i {analizza_citta(input_citta)[1][1]}")
    print(f"Valore min: {analizza_citta(input_citta)[2][0]} registrata nel/i mese/i {analizza_citta(input_citta)[2][1]}")
else:
    print(f"ERRORE! La città {input_citta} non è inserita nella lista!")
                                                                                                                                                                                                                                
    