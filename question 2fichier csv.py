import csv 
with open('titanic.csv', "r") as fichier: 
    table = csv.DictReader(fichier) 
    table_titanic=[] 
for ligne in table: 
    table_titanic.append(dict(ligne))

print(table_titanic)

nb_passager = len(table_titanic)
print("le nombrede passagers est de ", nb_passager)

nb_class_1 = 0
nb_class_2 = 0
nb_class_3 = 0
for ligne in table:
    if ligne['Pclass'] == 3:
        nb_class_1  += 1
    elif ligne['Pclass'] == 2:
        nb_class_2 += 1