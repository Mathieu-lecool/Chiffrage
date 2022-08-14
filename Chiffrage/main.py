from sys import platform
from subprocess import call

annulaire = {
    "e" : "yU8t",
    "u" : "O4AS",
    "ù" : "47Sq",
    "o" : "53uN",
    "s" : "jY6b",
    "i" : "2Hom",
    "d" : "FD7v",
    "f" : "g5Lq",
    "l" : "p17r",
    "c" : "rGw5",
    "ç" : "gS7c",
    "ê" : "i7fM",
    "è" : "o59I",
    "é" : "52Gt",
    "à" : "8dM2",
    " " : "eRt7",
    "," : "qr2b",
    "'" : "4sdC",
    "-" : "d5bl",
    "." : "lb4Q",
    "!" : "Lk4j",
    "?" : "4lxJ",
}

def _chiffrage(cible, travail):
    content = open(cible, "r").read()
    open(travail, "w").write("")
    content_split_a = content.split("a")
    nb_contents = len(content_split_a)-1
    fic = open(travail, "a")
    for i in range(0, nb_contents):
        fic.write(content_split_a[i]+"X2bZ")
    fic.write(content_split_a[nb_contents])
    fic.close()

    for lettre in annulaire:
        content = open(travail, "r").read()
        content_split = content.split(lettre)
        nb_contents = len(content_split)-1
        fic = open(travail, "w")
        for y in range(0, nb_contents):
            fic.write(content_split[y]+annulaire[lettre])
        fic.write(content_split[nb_contents])
        fic.close()

def _dechiffrage(cible, travail):
    content = open(cible, "r").read()
    open(travail, "w").write("")
    content_split_a = content.split("X2bZ")
    nb_contents = len(content_split_a)-1
    fic = open(travail, "a")
    for i in range(0, nb_contents):
        fic.write(content_split_a[i]+"a")
    fic.write(content_split_a[nb_contents])
    fic.close()

    for lettre in annulaire:
        content = open(travail, "r").read()
        content_split = content.split(annulaire[lettre])
        nb_contents = len(content_split)-1
        fic = open(travail, "w")
        for y in range(0, nb_contents):
            fic.write(content_split[y]+lettre)
        fic.write(content_split[nb_contents])
        fic.close()

if platform == "win32": commande = "cls"
elif platform == "linux": commande = "clear"
while True:
    if input("Quel est le mot de passe ? ") == "ENTRE TON MOT DE PASSE": #-----------------------
        call(commande, shell=True)
        choix = input("1 : Chiffrer\n2 : Déchiffrer\n")
        for chiffre in choix:
            try:
                if chiffre == "1":
                    _chiffrage(input("Entrez le chemain du fichier que vous voulez chiffrer : "), input("Entrez le chemain du fichier dans lequel le résulat apparaîtra : "))
                elif chiffre == "2":
                    _dechiffrage(input("\nEntrez le chemain du fichier que vous voulez déchiffrer : "), input("Entrez le chemain du fichier dans lequel le résulat apparaîtra : "))
            except: pass
        call(commande, shell=True)
        break
    else:
        print("Mot de passe incorrect !")
        call(commande, shell=True)
