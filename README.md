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

Grâce à la balise `[Tags]` il est possible de positionner des tags sur les *test cases*.

Par exemple, dans le cas où nous aurions le test suivant


```robotframework
*** Test Cases ***
Test Something
	[Tags] addon_non_mandatory
	Should Be Equal 10 	8
```


### Critiques? Non critique? 

Outre le fait de permettre le regroupement de nos tests par thématique, on peut ausi spécifier la non criticité d'une thématique en ajoutant l'option `--noncritical`. Dans notre cas, si on ajoute  `--noncritical  addon_non_mandatory`, on spécifie que **tous** les tests portant le tag `addon_non_mandatory` ne sont pas critiques.

Exercice:

- Ajouter des tags sur  `02_keyword.robot` de façon à rendre les tests sur l'humeur et  la compagnie non critiques
- Exécuter et constater que le fichier **report.html** filtre bien les tests spécifiés. 

### Variables

Les variables sont, comme dans tout langage très utilisée en robotframework.
Elles peuvent avoir trois portée:

- globale: leur portée est visible sur toutes les test suites. Si une test suite en modifie la valeur, cela impactera les autres. Elles peuvent être déclarées en ligne de commande (cf plus bas) ou avec le mot clef `set global variable`
- test suite: sa durée de vie est cloisonnée à une test suite. Ces variables sont déclarées par le mot clef `set suite variable` ou par la section `*** Variables ***`:

```robotframework
*** Variables ***
${MA_VARIABLE_1}		Toto
${MA_VARIABLE_2}		1
```

- test: durée de vie cantonnée à un test. Elles peuvent être déclarées par le mot clef `set test variable` ou à la volée (ici on `MY_TEST_VARIABLE` vaudra `TotoTitiTata`):

```robotframework
*** Test Cases ***
Some Test
	${MY_TEST_VARIABLE}=	Concat		Toto	Titi	Tata
```
	


Les variables globales peuvent être déclarées en ligne de commande (très pratique pour spécifier un type de configuration) grâce à l'option `-v`ou `--variable`dans sa version longue:

```bash
$> pybot -v MA_VARIABLE_1:Toto --variable MA_VARIABLE_2:1 testsuite_directory/
```


### Init et clean

### Organisation des tests

- Une test suite
- Organisation par arborescence

###

## L'application de démo:

Sous le répertoire **app-to-test** se trouve le fichier `login.py`. Taper `python app-to-test/login.py -h` et familiarisez vous avec.



## Le déroulement

### Intro
- Pourquoi utiliser robot
	 - inter-métier
	 - toute techno
- Installation des envs

### Cours
- Qu'est-ce qu'un test robot
 - Format d'un fichier robot (tabs) 
 - IDE ?
 - Execution et lecture d'un report

	:pencil2: ```exo: premier exo. Comment on fait? on montre ton premier exo et on demande d'un ajouter d'autre? Ou pour l'instant on ne leur fait rien rédiger et juste ils lancent le test?```

- Types de test
	- high level test
	- data driven test
- Keywords
	- Library Keywords (dont les librairies builtin)
	- User Keywords

	:pencil2: ```on récupère ton super keyword de prompt et on leur demande de coder des tests qui l'utilise?```

- Variables
	- Au niveau d'un test
	- En paramètre d'execution

	:pencil2: ```exercice? ou c'est suffisant d'attendre la deuxième partie?```

- Organisation des tests
	- Testsuites
	- Setup teardown
	- tags

### Pratique:	
- Presentation de l'application à tester

	:pencil2: ```manipuler l'appli pour comprendre le fonctionnement```

- Presentation de la lib Python fournie

	```imprimer la liste des keyword? car pas d'IDE```

- A vous de jouer

	:pencil2: ```voir comment on peut fournir le squelette...```

### Aller plus loin:

-  Créer ses propres librairies
-  Utiliser selenium (demo)
-  Integration continue, parallelisme



## TODO
	[] créer un memo avec la liste des mots clé python de la lib
	
	[] créer l'étape avec la lib python et tous les mots clé à coder
