tupla_competizioni=(
    ("Chef A","Piatto1",8.5, 5),
    ("Chef B","Piatto2",7.2, 4),
    ("Chef C","Piatto3",9.0, 6),
    ("Chef A","Piatto4",7.8, 5),
    ("Chef B","Piatto5",8.1, 4),
)

#richiesta 1
def media_punteggio_competizioni(tupla_competizioni):
    media=0
    cont=0
    for(nome_chef,nome_piatto,punteggio,num_giudici) in tupla_competizioni:
        media+=punteggio
        cont+=1
    return media/cont

#richiesta2
def media_punteggio_chef(tupla_competizioni, chef):
    media=0
    cont=0
    a=False
    for(nome_chef,nome_piatto,punteggio,num_giudici) in tupla_competizioni:
        if(nome_chef==chef):
            a=True
    if(a):#se lo chef è presente nella tupla, procedo al calcolo della media e ritorno il valore
        for(nome_chef,nome_piatto,punteggio,num_giudici) in tupla_competizioni:
            if(nome_chef==chef):
                media+=punteggio
                cont+=1
        return media/cont
    else:#altrimenti ritorna 0 
        return 0

#richiesta3
def competizioni_con_piu_giudici(tupla_competizioni):
    max=0
    lista_max=[]
    for(nome_chef,nome_piatto,punteggio,num_giudici) in tupla_competizioni:
        if(num_giudici>max):
            max=num_giudici
    for(nome_chef,nome_piatto,punteggio,num_giudici) in tupla_competizioni:
        if(num_giudici==max):
            lista_max.append((nome_chef,nome_piatto,punteggio,num_giudici))
    return lista_max

#richiesta4
def competizioni_con_meno_giudici(tupla_competizioni):
    min=100000
    lista_min=[]
    for(nome_chef,nome_piatto,punteggio,num_giudici) in tupla_competizioni:
        if(num_giudici<min):
            min=num_giudici
    for(nome_chef,nome_piatto,punteggio,num_giudici) in tupla_competizioni:
        if(num_giudici==min):
            lista_min.append((nome_chef,nome_piatto,punteggio,num_giudici))
    return lista_min


scelta=0
#menù 
while(scelta!=5):
    print("\n1-Visualizza la media dei punteggi totale")
    print("2-Visualizza la media dei punteggi di uno chef")
    print("3-Visualizza la/e competizione/i con più giudici")
    print("4-Visualizza la/e competizione/i con meno giudici")
    print("5-Termina programma")
    #validazione input scelta
    while(True):
        scelta=int(input("\nInserisci la tua scelta: "))
        if(scelta>0 and scelta<=5):
            break
    
    if(scelta==1):
        print(f"\nLa media totale dei punteggi è {media_punteggio_competizioni(tupla_competizioni) :.2f}")
    elif(scelta==2):
        chef=str(input("Inserisci il nome dello chef: "))
        if(media_punteggio_chef(tupla_competizioni,chef)==0): #se lo chef non è presente nella tupla, ritorna 0
            print(f"Lo chef {chef} non ha partecipato a nessuna competizione!")#messaggio di errore
        else:
            print(f"La media dei punteggi dello chef {chef} è {media_punteggio_chef(tupla_competizioni,chef):.2f}") #altrimenti stampa il risultato
    elif(scelta==3):
        print(f"La/e competizione/i con più giudici: {competizioni_con_piu_giudici(tupla_competizioni)}")
    elif(scelta==4):
        print(f"La/e competizione/i con meno giudici: {competizioni_con_meno_giudici(tupla_competizioni)}")