import csv
import matplotlib.pyplot as plt

#chargement des donnees
donnees = []
with open('donnees_2008.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader) 
    for row in reader:
        row[9] = int(row[9])
        donnees.append(row)

donnees16 = []
with open('donnees_2016.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        row[9] = int(row[9])
        donnees16.append(row)

donnees21 = []
with open('donnees_2021.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader) 
    for row in reader:
        row[5] = int(row[5])
        donnees21.append(row)

#filtrage des donnees pour l yonne
yonne_89 = [row for row in donnees if row[2] == '89']
yonne_2016 = [row for row in donnees16 if row[2] == '89']
yonne_2021 = [row for row in donnees21 if row[1] == '89']

#filtrage des donnees pour Auxerre
auxerre_89 = [row for row in donnees if row[1] == '89013']
auxerre_2016 = [row for row in donnees16 if row[1] == '89013']
auxerre_2021 = [row for row in donnees21 if row[0] == '89013']

#calcul de la population pour chaque annee
population_2008 = sum(row[9] for row in yonne_89)
population_2016 = sum(row[9] for row in yonne_2016)
population_2021 = sum(row[5] for row in yonne_2021)

#calcul de la population d Auxerre pour chaque année
population_auxerre_2008 = sum(row[1] for row in auxerre_89)
population_auxerre_2016 = sum(row[1] for row in auxerre_2016)
population_auxerre_2021 = sum(row[0] for row in auxerre_2021)

#creation du graphique
annees = [2008, 2016, 2021]
populations_yonne = [population_2008, population_2016, population_2021]
populations_auxerre = [population_auxerre_2008, population_auxerre_2016, population_auxerre_2021]

#courbe de l'Yonne
plt.plot(annees, populations_yonne, label='Yonne', color='blue')

#courbe pour Auxerre
plt.plot(annees, populations_auxerre, label='Auxerre', color='green')

plt.title('Évolution de la population de l Yonne et d Auxerre')
plt.xlabel('Annee')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()

