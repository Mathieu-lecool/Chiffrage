FICHIER_A_CHIFFRER = ""
FICHIER_DE_RECEPTION = ""

lettre = ["e", "u", "o", "s", "i", "d", "f", "l", "c", " ", ",", "'", "."]
chiffrage = ["yU8t", "O4AS", "53uN", "jY6b", "2Hom", "FD7v", "g5Lq", "p17r", "rGw5", "eRt7", "qr2b", "4sdC", "lb4Q"]

content = open(FICHIER_A_CHIFFRER, "r").read()
open(FICHIER_DE_RECEPTION, "w").write("")
content_split_a = content.split("a")
nb_contents = len(content_split_a)-1
fic = open(FICHIER_DE_RECEPTION, "a")
for i in range(0, nb_contents):
    fic.write(content_split_a[i]+"X2bZ")
fic.write(content_split_a[nb_contents])
fic.close()

for i in range(0, len(lettre)-1):
    content = open(FICHIER_DE_RECEPTION, "r").read()
    content_split = content.split(lettre[i])
    nb_contents = len(content_split)-1
    fic = open(FICHIER_DE_RECEPTION, "w")
    for i in range(0, nb_contents):
        fic.write(content_split[i]+chiffrage[i])
    fic.write(content_split[nb_contents])
    fic.close()