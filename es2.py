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

print(f"Media globale: {media_globale(tupla_vendite):.2f}")
