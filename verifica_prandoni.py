import random

#richiesta1
concorso_cucina={
    "Rossi Mario": [("Antipasto",(8,7,9),"Junior chef"),("Primo",(7,8,8),"Junior chef"),("Secondo",(9,9,8),"Junior chef"),("Dessert",(8,8,9),"Junior chef")],
    "Bianchi Luigi": [("Antipasto",(7,7,8),"Senior chef"),("Primo",(8,9,7),"Senior chef"),("Secondo",(7,8,7),"Senior chef"),("Dessert",(9,8,8),"Senior chef")],
    "Verdi Giulia": [("Antipasto",(9,8,8),"Junior chef"),("Primo",(8,7,9),"Junior chef"),("Secondo",(8,8,8),"Junior chef"),("Dessert",(7,9,8),"Junior chef")]
}

#richiesta2
concorso_cucina["Prandoni Matteo"]=[("Antipasto",(8,9,8),"Senior chef"),("Primo",(7,8,7),"Senior chef"),("Secondo",(9,8,8),"Senior chef"),("Dessert",(7,9,8),"Senior chef")]

#richiesta3
def aggiungi_quinta_categoria():
    for chef in concorso_cucina.keys():
        for categoria_piatto, voti, categoria_chef in concorso_cucina[chef]:
            concorso_cucina[chef].append(("Piatto unico",(random.randint(1,10),random.randint(1,10),random.randint(1,10)),categoria_chef))
            print(f"Votazioni del piatto unico aggiunte correttamente per lo chef {chef}")
            break
aggiungi_quinta_categoria()

#richiesta4
def isPresente(chef):
    if(chef in concorso_cucina.keys()):
        return True
    else:
        return False

def stampaChef(chef):
    if(isPresente(chef)):
        print(f"\nCognome e nome: {chef}")
        for categoria_piatto, voti, categoria_chef in concorso_cucina[chef]:
            print(f"Categoria chef: {categoria_chef}")
            break
        for categoria_piatto, voti, categoria_chef in concorso_cucina[chef]:
            print(f"\nCategoria piatto: {categoria_piatto}")
            print("Votazioni:")
            print(f"\t-Creatività: {voti[0]}")
            print(f"\t-Gusto: {voti[1]}")
            print(f"\t-Presentazione: {voti[2]}")
    else:
        print("ERRORE! Chef non presente!")


chef=str(input("Inserisci il nome dello chef da visualizzare: "))
stampaChef(chef)

#richiesta5
def stampaPiatto(piatto):
    print(f"Chef che hanno cucinato un {piatto}: ")
    piattoPresente=False
    for chef in concorso_cucina.keys():
        for categoria_piatto, voti, categoria_chef in concorso_cucina[chef]:
            if(categoria_piatto==piatto):
                print(f"\nCognome e nome: {chef}")
                print(f"Categoria chef: {categoria_chef}")
                print("Votazioni:")
                print(f"\t-Creatività: {voti[0]}")
                print(f"\t-Gusto: {voti[1]}")
                print(f"\t-Presentazione: {voti[2]}")
                piattoPresente=True
    if(piattoPresente==False):
        print(f"ERRORE! Nessuno chef ha cucinato un {piatto}")

piatto=str(input("Inserisci la categoria del piatto da visualizzare: "))
stampaPiatto(piatto)

#richiesta6 
def totale_massimo(concorso_cucina, piatto, tipo_chef):
    piatto_e_chef_presenti=False
    max=0
    for chef in concorso_cucina.keys():
        tot=0
        for categoria_piatto, voti, categoria_chef in concorso_cucina[chef]:
            if(categoria_piatto==piatto and categoria_chef==tipo_chef):
                tot+=voti[0]
                tot+=voti[1]
                tot+=voti[2]
                piatto_e_chef_presenti=True
            if(tot>max):
                max=tot
                chef_max=chef
    if(piatto_e_chef_presenti):
        return [max,chef_max]
    else:
        return 0

def media(concorso_cucina, piatto, tipo_chef):
    piatto_e_chef_presenti=False
    media=0
    cont=0
    for chef in concorso_cucina.keys():
        for categoria_piatto, voti, categoria_chef in concorso_cucina[chef]:
            if(categoria_piatto==piatto and categoria_chef==tipo_chef):
                media+=voti[0]
                media+=voti[1]
                media+=voti[2]
                cont+=1
                piatto_e_chef_presenti=True
    if(piatto_e_chef_presenti):
        return media/cont
    else:
        return 0

piatto=str(input("Inserisci la categoria del piatto: "))
tipo_chef=str(input("Inserisci la categoria dello chef: "))
if(totale_massimo(concorso_cucina, piatto, tipo_chef)==0):
    print("ERRORE, impossibile calcolare il totale! Piatto e/o chef non presenti!")
else:
    print(f"Votazione massima: {totale_massimo(concorso_cucina, piatto, tipo_chef)[0]}, ottenuta dallo chef {totale_massimo(concorso_cucina, piatto, tipo_chef)[1]}")

if(media(concorso_cucina, piatto, tipo_chef)==0):
    print("ERRORE, impossibile calcolare la media! Piatto e/o chef non presenti!")
else:
    print(f"Votazione media: {media(concorso_cucina, piatto, tipo_chef):.2f}")

#richiesta7
def inserisci_dati_nuovo_chef():
    lista=[]
    lista_categoria_piatto=["Antipasto","Primo","Secondo","Dessert","Piatto unico"]
    categoria_chef=str(input("Inserisci la categoria dello chef: "))
    for piatto in lista_categoria_piatto:
        while True:
            creativita=int(input(f"Inserisci la creatività del piatto {piatto}:"))
            if(creativita>0):
                break
        while True:
            gusto=int(input(f"Inserisci il gusto del piatto {piatto}:"))
            if(gusto>0):
                break
        while True:
            presentazione=int(input(f"Inserisci la presentazione del piatto {piatto}:"))
            if(presentazione>0):
                break
        lista.append(piatto,(creativita,gusto,presentazione),categoria_chef)
    return lista

def inserisci_nuovo_chef(concorso_cucina, nominativo, dati):
    if(isPresente(nominativo)==False):
        concorso_cucina[nominativo]=dati
        print("Chef aggiunto correttamente!")
    else:
        print("ERRORE! chef già presente")

nominativo=str(input("Inserisci il nome dello chef: "))
dati=inserisci_dati_nuovo_chef()
inserisci_nuovo_chef(concorso_cucina, nominativo, dati)