"""
    Note per l'esecuzione
    1)
    -input regione: "Veneto"
    -input coltura: "grano"
    Media: 1000.00
    Valore Max: 1300
    Mesi nel quale si è registrato=["gennaio"]

    2)
    -input regione: "Toscana"
    -input coltura: "pomodori"
    Media: 1133.33
    Valore Max: 1200
    Mesi nel quale si è registrato=["febbraio","marzo"]
    """

tupla_produzione_agricola=(
    ("Toscana",[
        ("gennaio",("grano",1200)),
        ("gennaio",("mais",900)),
        ("gennaio",("pomodori",1000)),
        ("febbraio",("grano",1400)),
        ("febbraio",("mais",1300)),
        ("febbraio",("pomodori",1200)),
        ("marzo",("grano",1100)),
        ("marzo",("mais",1500)),
        ("marzo",("pomodori",1200)),
    ]),

    ("Lombardia",[
        ("gennaio",("grano",1300)),
        ("gennaio",("mais",1000)),
        ("gennaio",("pomodori",800)),
        ("febbraio",("grano",1600)),
        ("febbraio",("mais",900)),
        ("febbraio",("pomodori",1200)),
        ("marzo",("grano",1300)),
        ("marzo",("mais",1100)),
        ("marzo",("pomodori",1400)),
    ]),

    ("Campania",[
        ("gennaio",("grano",1100)),
        ("gennaio",("mais",1000)),
        ("gennaio",("pomodori",900)),
        ("febbraio",("grano",1200)),
        ("febbraio",("mais",1400)),
        ("febbraio",("pomodori",1100)),
        ("marzo",("grano",1000)),
        ("marzo",("mais",900)),
        ("marzo",("pomodori",1100)),
    ]),

    ("Veneto",[ 
        ("gennaio",("grano",1300)),
        ("gennaio",("mais",1000)),
        ("gennaio",("pomodori",800)),
        ("febbraio",("grano",700)),
        ("febbraio",("mais",1200)),
        ("febbraio",("pomodori",1100)),
        ("marzo",("grano",1000)),
        ("marzo",("mais",1300)),
        ("marzo",("pomodori",1400)),
    ]),

)

def analizza_produzione_agricola(input_regione,input_coltura):
    media=0
    cont=0
    max=0
    lista_max=[]
    for regione,dati in tupla_produzione_agricola: #nella veriabile regione viene messo il primo elemento della tupla (es:"Toscana"), mentre in dati vengono messi tutti gli altri valori
        if(regione==input_regione): #controllo se la regione corrisponde a quella che ho inserito in input (già validata)
            for mese,(coltura,raccolti) in dati:#solo se corrisponde divido la tupla dati in mese (es:"gennaio"), (coltura(es:"grano"), raccolti(es:1400))
                if(coltura==input_coltura): #se la coltura è uguale a quella che ho inserito in input (già validata) procedo con il calcolo della media
                    media+=raccolti 
                    cont+=1
                    if(raccolti>max):   #trovo il valore max
                        max=raccolti
            #appena esco dal for ho il valore max del raccolto, la somma dei raccolti e il numero di mesi
            for mese,(coltura,raccolti) in dati:   #in questo for appendo a lista_max i mesi nella quale si è verificato il raccolto di valore max 
                if(coltura==input_coltura):
                    if(raccolti==max):
                        lista_max.append(mese)
    media/=cont
    return (media,(max,lista_max)) 
        
    

regione_presente=False
coltura_presente=False
#validazione input di input_regione
while(regione_presente==False):
    input_regione=input("Inserisci la regione: ")
    for regione,dati in tupla_produzione_agricola:
        if(regione==input_regione):
            regione_presente=True 
    if(regione_presente):#se regione_presente == True, esco dal ciclo while
        break
    else:
        print("ERRORE! Regione non presente nella tupla")#altrimenti messaggio di errore e me lo richiede

while(coltura_presente==False):
    input_coltura=input("Inserisci la coltura: ")
    for regione,dati in tupla_produzione_agricola:
        for mese,(coltura,raccolti) in dati:
            if(coltura==input_coltura and regione==input_regione):
                coltura_presente=True   #coltura_presente diventa True solo se la coltura è presente per quella determinata regione
    if(coltura_presente):#se coltura_presente == True, esco dal ciclo while
        break
    else:
        print("ERRORE! Coltura non presente nella tupla")#altrimenti messaggio di errore e me lo richiede


print(f"\nMedia raccolti della coltura {input_coltura} nella regione {input_regione}: {analizza_produzione_agricola(input_regione,input_coltura)[0]:.2f}")
print(f"Il raccolto massimo della coltura {input_coltura} nella regione {input_regione} è {analizza_produzione_agricola(input_regione,input_coltura)[1][0]}, registrato nel/i mese/i {analizza_produzione_agricola(input_regione,input_coltura)[1][1]}")
