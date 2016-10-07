# Dojo robotframework

*Le but de ce repository est une découverte de l'outil robot framwork*

## Prérequis
Pour suivre cet atelier, vous devez installer:

- [python 2.7](https://www.python.org/downloads/)
- [pip](#pip)
- [virtualenv](https://pypi.python.org/pypi/virtualenv)


## Intérêt de robotframework
Robotframework permet de déclarer des suites de tests dans un langage naturel, à haut niveau sémantique (ouf ça envoie du pâté). 

Robotframework est une librairie `python` mais il définit un langage totalement différent, plus simple, et accessible à tous types de métier. N'importe quelle personne ayant des notions très basiques d'informatique, capable:

- lancer une commande
- comprendre l'indentation à un niveau de tabulation
- comprendre la notion de section

est capable de développer des tests.

Cela permet d'inclure dans leur rédaction les développeurs, les testeurs, mais aussi les product owners et ainsi s'approcher d'unun d'une méthodologie BDD.


## Installation des environnements

### Pip

Télécharger [les sources de pip]https://pypi.python.org/pypi/pip#downloads), puis exécuter le fichier `setup.py`:
`[sudo] python setup.py`

### Virtualenv
Pour ceux qui ne souhaiteraient pas poluer leur répertoire d'installation python, installer la librarie, installer [virtualenv](https://pypi.python.org/pypi/virtualenv). Puis créer un environnement virtuel dédié à ce tutoriel.
Pour les autres, passer à l'étape suivante.

- installation: `pip install virtualenv`
 -créer un environnement virtuel (dans le répertoire où on veut que l'environnement virtual soit créé): `virtualenv DojoRobotframework`
- chargement: `source  DojoRobotframework/bin/activate`

### Installation des libraries

Taper la commande (dans l'environnement virtuel pour ceux qui en ont un): `pip install -r requirements.txt`

## Structure des fichiers de test

### Le premier, on s'en souvient toujours, même si c'est pas génial
Dans le répertoire **test_suites** se trouve le fichier `01_check_environment.robot`. Ce fichier définit deux tests cases dans la section `*** Test Cases ***`. Chaque *test case* est une succession d'expression robotframework visant à charger une donnée, la vérifier.

**En bref**: ce fichier comporte :

- Deux sections: `Settings` et `Test Cases`
- La section `Test Cases` comporte deux *test case*. Chacun de ces derniers comporte un libellé, et une série d'instructions (appelées **keywords** ) tabulées. 

Exécuter le avec la commande: `pybot test_suites/01_check_environment.robot`

### Les logs générés

On voit en fin de test que les chaque test case est marqué d'un `SUCCESS`ou `FAIL`. En outre robotframework génère trois fichiers:
- output.xml
- log.html
- report.html

### Les keywords ou mots clefs
Les keywords sont proposés par les librairies. Sans rien importer, on n'a que les keywords proposés par la librairie **BuiltIn**. De nombreuses autres librairies existent **nativement** pour ceux qui auraient peur de prendre le python à deux mains.

- String
- DateTime
- Process

Et d'autres encore installable d'un petit coup de `pip`...

Plus de détails [ici](http://robotframework.org/robotframework/#user-guide)
 

Mais on peut aussi implémenter ses propres keywords. Jeter un oeil au fichier `02_keyword.robot`. On y définit dans la section `***Keywords***` le *keyword* `Prompt User` qui prend un argument et renvoie la réponse de l'utilisateur.

L'exécuter.


### Les tags

Grâce à la balise `[Tags]` il est possible de positionner des tags sur les *test cases*

### Critiques? Non critique? 

Il est possible de préciser en ligne de commande quels tags désignent ou non critiques.

- ajout de tags
- exécution
-ouverture de *report.html*, filtrag avec ou sans critiques.

## L'application de démo:

Sous le répertoire **app-to-test** se trouve le fichier `login.py`. Taper `python app-to-test/login.py -h` et familiarisez vous avec.



## Le déroulement



 - Utilisation d'un log
 - Execution et lecture d'un report
 - IDE?
 - *application : faire un premier test qui log*
- Types de test
	- high level test
	- data driven test
- Keywords
	- Library Keywords (dont les librairies builtin)
	- User Keywords
	- *on récupère la lib python, et on fait coder les mots clé à chacun*
- Variables
	- Au niveau d'un test
	- En paramètre d'execution
	- *exercice*
- Organisation des tests
	- Testsuites
	- Setup teardown
	- tags
- Aller plus loin:
	-  Créer ses propres librairies
	-  Utiliser selenium
	-  Integration continue

	## TODO
	[] créer un memo avec la liste des mots clé python de la lib
	
	[] créer l'étape avec la lib python et tous les mots clé à coder
