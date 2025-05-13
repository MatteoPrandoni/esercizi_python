from math import sqrt

class Pagella:

    def __init__(self,lista):
        self.voti=lista

    def __repr__(self):
        info=""
        if(len(self.voti)==0):
            info="Pagella vuota!"
        else:
            for voto in self.voti:
                info+=f"- {voto}\n"
        return info
    
    def media(self):
        if(len(self.voti)==0):
            return -1
        else:
            media=0
            for voto in self.voti:
                media+=voto
            return media/len(self.voti)
        
    def __getitem__(self,i):
        if(i<len(self.voti)):
            return self.voti[i]
        else:
            return -1
    
    def __eq__(self, pagella):
        if(len(self.voti)==len(pagella.voti)):
            return self.voti == pagella.voti
        else:
            print("Le pagelle hanno un diverso numero di materie e non possono essere confrontate")
            return None
    
    def __sub__(self,pagella):
        if(len(self.voti)==len(pagella.voti)):
            array=[]
            for i in range(len(self.voti)):
                array.append(self.voti[i]-pagella.voti[i])
            return Pagella(array)
        else:
            print("Le pagelle hanno un diverso numero di materie e non possono essere confrontate")
            return None

    def impegno(self):
        somma=0
        for voto in self.voti:
            somma+=(voto*voto)
        return sqrt(somma)
    
pagella1=Pagella([6,9,7])
pagella2=Pagella([7,4,8])

pagella3=pagella1

#test metodo __repr__
print(pagella1)

#test metodo media()
print(pagella1.media()) #output : 7.33333333
print()

#test metodo __getitem__
print(pagella2[1],pagella2[2]) #output : 4 8
print(pagella1[6]) #output -1 (out of index)
print()

#test metodo __eq__  Output: "Le due pagelle sono uguali"
if(pagella1==pagella3):
    print("Le due pagelle sono uguali")
else:
    print("Le due pagelle NON sono uguali")
print()

pagella4=Pagella([3,7])
#test metodo __eq__  Output: "Le pagelle hanno un diverso numero di materie e non possono essere confrontate.Le due pagelle NON sono uguali"
if(pagella1==pagella4):
    print("Le due pagelle sono uguali")
else:
    print("Le due pagelle NON sono uguali")
print()

#test metodo __sub__ 
"""output:
- -1
- 5
- -1
"""
print(pagella1-pagella2) 

#test metodo impegno output : 10.0
pagella5=Pagella([6,8])
print(pagella5.impegno())