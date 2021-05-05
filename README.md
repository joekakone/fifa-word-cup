# FIFA WORLD CUP - Analysis
Collecte - Analyse - Visualisation

## Description
### Objetcif
1. Scraper des données depuis un tableau dans une page web
2. 

### Données
Les données sont disponibles sur cette page https://www.foxsports.com/soccer/fifa-world-cup/history


## Collecte
```sh
python collect.py
```
Cette étape consiste à récupérer les données depuis la page web et à les écrire dans un fichier `.csv`. Implémentation avec `Requests` et `BeautifulSoup`

## Analyse
Remarquons qu'il n'y a pas eu d'édition en *194X* à cause de la guerre. Seulement X pays l'ont gagné depuis sa création.

## Visualisation
Construire un tableau de board ou une story avec Tableau Software
1. Indicateurs clés
    * Nombre d'éditions
    * Nombre de matchs
    * Nombre de buts
    * Nombre de pays vainqueurs
2. Diagrammes en barres
    * Top 5 des pays organisateurs
    * Top 5 des pays vainqueurs
3. Courbe temporelle (Nombre de buts par édition)

## Source
https://www.foxsports.com/soccer/fifa-world-cup/history
