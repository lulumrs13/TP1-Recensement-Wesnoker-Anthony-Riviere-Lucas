import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#initialiser les totaux à zéro
total_fossile = 0
total_renouvelable = 0

#ouvrir le fichier CSV
with open('RTE_2020.csv', mode='r', encoding='utf-8') as csvfile:
   
    #créer un objet reader qui va lire le fichier CSV
    csvreader = csv.reader(csvfile)
    
    #Obtenir les en tetes des colonnes
    headers = next(csvreader)
    
    #trouver les indices des collonnes pour les energies fossiles et renouvelables
    charbon = headers.index('Charbon')
    fioul = headers.index('Fioul')
    gaz = headers.index('Gaz')
    nucléaire = headers.index('Nucleaire')
    
    eolien = headers.index('Eolien')
    solaire = headers.index('Solaire')
    hydraulique = headers.index('Hydraulique')
    bioenergies = headers.index('Bioenergies')

    #lire chaque ligne du fichier CSV
    for row in csvreader:
       
        # ignorer les lignes sans données
        if row[charbon] == '':
            continue
        if row[fioul] == '':
            continue
        if row[gaz] == '':
            continue
        if row[nucléaire] == '':
            continue
        if row[eolien] == '':
            continue
        if row[solaire] == '':
            continue
        if row[hydraulique] == '':
            continue
        if row[bioenergies] == '':
            continue

        #additionner la production d'energies fossiles
        total_fossile += int(row[charbon]) + int(row[fioul]) + int(row[gaz]) + int(row[nucléaire])

        #additionner la production d'énergies renouvelables
        total_renouvelable += int(row[eolien]) + int(row[solaire]) + int(row[hydraulique]) + int(row[bioenergies])

#afficher les totaux
print(f'Production totale énergies fossiles: {total_fossile}')
print(f'Production totale énergies renouvelables: {total_renouvelable}')

##########################################################################################################

#programme secondaire pour affichier le graphique 

#initialiser les listes pour stocker les données
dates = []
production_fossile = []
production_renouvelable = []

#définir la date de départ
dd = datetime(2020, 1, 1)

#ouvrir le fichier CSV
with open('RTE_2020.csv', mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)  # Ignorer les en-têtes

    #indices des colonnes
    charbon = headers.index('Charbon')
    fioul = headers.index('Fioul')
    gaz = headers.index('Gaz')
    nucléaire = headers.index('Nucleaire')

    eolien = headers.index('Eolien')
    solaire = headers.index('Solaire')
    hydraulique = headers.index('Hydraulique')
    bioenergies = headers.index('Bioenergies')
    

    #lire chaque ligne du fichier CSV
    for i, row in enumerate(csvreader):
        # ignorer les lignes sans données
        if row[charbon] == '':
            continue
        if row[fioul] == '':
            continue
        if row[gaz] == '':
            continue
        if row[nucléaire] == '':
            continue
        if row[eolien] == '':
            continue
        if row[solaire] == '':
            continue
        if row[hydraulique] == '':
            continue
        if row[bioenergies] == '':
            continue
        #calculer la date et l'heure
        ttdate = dd + timedelta(minutes=15*i)
        dates.append(ttdate)

        #ajouter les valeurs d'énergies fossiles et renouvelables
        #valeurs manquantes représentées par chaines vides et remplacées par 0
        fossile = sum([int(row[charbon] or 0), int(row[fioul] or 0), int(row[gaz] or 0), int(row[nucléaire] or 0)])
        renouvelable = sum([int(row[eolien] or 0), int(row[solaire] or 0), int(row[hydraulique] or 0), int(row[bioenergies] or 0)])
        
        production_fossile.append(fossile)
        production_renouvelable.append(renouvelable)

#tracer le graphique
plt.plot(dates, production_fossile, label='Fossile')
plt.plot(dates, production_renouvelable, label='Renouvelable')

plt.xlabel('Date')
plt.ylabel('Production énergie (Mwatt/h)')
plt.title('Production énergie fossile vs renouvelable en 2020')
plt.grid(True)

plt.show()