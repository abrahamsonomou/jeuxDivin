import random

# verification de la siasiie du nombre
def verification(texte):
    verification=True
    n=0
    while verification:
        n=input("Donner {}".format(texte))
        try:
            n=int(n)
            verification=False
        except :
            print("Veuillez saisir un entier ")
    
    return n

# generation du nombre aleatoire
nbcahe=random.randint(0,100)

trouve=True
essai=1
# definition de la fonction jeu
def jeu():
    global trouve
    global essai
    while trouve and essai <=3:
        rep=verification("le nombre caché: ")
        if(rep <nbcahe):
            print("Plus grand")
        if(rep >nbcahe):
            print("Plus petit")
        if rep==nbcahe:
            # print("Bravo vous avez gagné avec {} essais".format(essai))
            # input("")
            trouve=False
            break
            return True
        if essai==3:
            trouve==False
            break
        essai+=1
    if essai==3 or trouve==True:
        # print("Vous avez perdu du Courage !")
        # input("")
        return False

if(jeu()):
    print("Bravo vous avez gagné avec {} essais".format(essai))
    choix=input("Voulez-vous continuer O/N? ")
    if choix =="O" or choix=="o":
        jeu()
    else:
        print("Aurevoir !")
else:
    print("Vous avez perdu du Courage !")
    input("")
        