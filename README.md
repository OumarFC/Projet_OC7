# Projet 7 : Résolvez des problèmes en utilisant des algorithmes en Python

![logo.png](logo.png)


## Sommaire

+ [Objectif du projet ](#Objectif)
+ [Installation du projet](#Installation)
+ [Installation des packages](#Packages)
+ [Le fichier .gitignore](#gitignore)


## Objectif

Ce projet consiste à créer differents algorithmes afin de maximiser les benefices des investisseurs 
de l'entreprise AlgoInvest&Trade, une société financière spécialisé dans l'investissement.

la contrainte est que l'on a un montant maximum d'investissement et un choix d'actions limités

les differents alogorithmes :

- "bruteforce.py" : alogorithme de brute force
- "optimisez.py"  : agorithme optimisé en programmation dynamique

La dernière partie consiste à tester les algorithmes sur differents dataset de 1000 actions et les comparer avec 
les solutions obtenues auparavant. ces differentes données se trouvent dans le dossier <<donnee>>


## Installation
  
1- Télécharger et installer la dernière version de Python.
   Pour ma part j'ai installé la version python 3.10.6
		 
2 - Depuis votre terminal sous windows ( cmd )  

Verifiez que vous avez pip installer sur la machine
pour cela lancer la commande 

```pip --help```

- Créer votre dossier projet sous windows
	     
```
mkdir < MyProject07 > 
```
où MyProject07 est le nom de votre projet,
placez-vous dans le repertoire projet
```
cd < MyProject07 > 
```
Créer votre environnement virtuel
```
pip -m venv < myenv > 
```
Où myenv est le nom pour votre environnement virtuel.
Activez votre environnement virtuel.
```
cd < myenv\scripts> 
activate.bat
```

##packages

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```
Sous windows lancer la commande:

pip install -r requirement.txt

```
afin d'installer toutes les librairies.

```
## gitignore

Exclure l'environnement virtuel des commits sur le serveur distant 
	
Créez le fichier .gitignore à la racine de votre projet:   

```~\MyProject07\.gitignore ```

Editez le fichier .gitignore et ajouter les fichiers et repertoire que vous souhaitez exclure