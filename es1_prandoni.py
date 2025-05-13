class Macchina:
    def __init__(self, targa, marca, modello, anno):
        self.targa=targa
        self.marca=marca
        self.modello=modello
        self.anno=anno

    def __str__(self):
        return f"{self.marca} {self.modello} ({self.anno}) - Targa: {self.targa}"


class Garage:
    def __init__(self):
        self.lista_macchine=[]

    def array_targhe(self): #ritorna un array che contiene tutte le targhe del garage
        array=[]
        for macchina in self.lista_macchine:
            array.append(macchina.targa)
        return array
    
    def aggiungi_macchina(self, macchina):
        if(macchina.targa in self.array_targhe()): #se la targa è già presente
            print("Impossibile aggiungere la macchina, targa già presente!")
        else:
            self.lista_macchine.append(macchina)
            print("Macchina aggiunta correttamente!")

    def rimuovi_macchina(self, targa):
        if(len(self.lista_macchine)==0):
            print("Impossibile rimuovere la macchina, lista vuota!")
        else:
            for macchina in self.lista_macchine:
                if(macchina.targa==targa):
                    self.lista_macchine.remove(macchina)
                    print("Macchina rimossa con successo!")
                    return
            print("Impossibile rimuovere la macchina, targa non trovata!")

    def elenco_macchine(self):
        if(len(self.lista_macchine)==0):
            print("Garage vuoto!")
        else:
            print("Macchine presenti nel garage:")
            for macchina in self.lista_macchine:
                print(f"- {macchina}")

    def cerca_macchina(self, targa):
        if(len(self.lista_macchine)==0):
            print("Garage vuoto!")
        else:
            for macchina in self.lista_macchine:
                if(macchina.targa==targa):
                    return macchina
        return None
    

garage =Garage()
scelta=0
while True:
    print("Gestisci Garage")
    print("1-Aggiungi macchina")
    print("2-Rimuovi macchina")
    print("3-Visualizza garage")
    print("4-Cerca macchina")
    print("5-Termina programma")
    while True:
        scelta=int(input("Inserisci la tua scelta: "))
        if(scelta>=1 and scelta<=5):
            break
    
    if(scelta==1):
        while True:
            targa=input("Inserisci la targa della macchina: ")
            if(len(targa)==7):
                break
        marca=input("Inserisci la marca della macchina: ")
        modello=input("Inserisci il modello della macchina: ")
        while True:
            anno=int(input("Inserisci l'anno della macchina: "))
            if(anno>0):
                break
        garage.aggiungi_macchina(Macchina(targa,marca,modello,anno))
    
    elif(scelta==2):
        while True:
            targa=input("Inserisci la targa della macchina: ")
            if(len(targa)==7):
                break
        garage.rimuovi_macchina(targa)

    elif(scelta==3):
        garage.elenco_macchine()
    
    elif(scelta==4):
        while True:
            targa=input("Inserisci la targa della macchina: ")
            if(len(targa)==7):
                break
        macchina_trovata=garage.cerca_macchina(targa)
        if(macchina_trovata!=None):
            print(macchina_trovata)
        else:
            print("Macchina non trovata")
        
    else:
        break
    print()

