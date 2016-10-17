# Dojo robotframework

*Le but de ce repository est une découverte de l'outil robot framwork
Pour suivre cet atelier, vous devez installer:
[python 2.7](https://www.python.org/downloads/) +
[pip](#pip) + [virtualenv](https://pypi.python.org/pypi/virtualenv)*


## Intro
### Intérêt de robotframework
#### Un langage pour tous les métiers
Robotframework permet de déclarer des suites de tests dans un langage naturel, à haut niveau sémantique (ouf ça envoie du pâté). 

Robotframework est une librairie `python` mais il définit un langage totalement différent, plus simple, et accessible à tous types de métier. N'importe quelle personne ayant des notions très basiques d'informatique, capable:

- lancer une commande
- comprendre l'indentation à un niveau de tabulation
- comprendre la notion de section

est capable de développer des tests.

Cela permet d'inclure dans leur rédaction les développeurs, les testeurs, mais aussi les product owners et ainsi s'approcher d'une méthodologie BDD.

#### Capable de tester toutes vos technos
Robotframework n'est pas lié à une techno. Ses nombreuses librairies (ainsi que le fait de pouvoir développer les votres) lui permet de piloter n'importe quel produit pilotable par un ordinateur.

### Installation des environnements

#### Pip

Télécharger [les sources de pip]https://pypi.python.org/pypi/pip#downloads), puis exécuter le fichier `setup.py`:
`[sudo] python setup.py`

#### Virtualenv
Pour ceux qui ne souhaiteraient pas polluer leur répertoire d'installation python, installer la librarie, installer [virtualenv](https://pypi.python.org/pypi/virtualenv). Puis créer un environnement virtuel dédié à ce tutoriel.
Pour les autres, passer à l'étape suivante.

- installation: `pip install virtualenv`
 -créer un environnement virtuel (dans le répertoire où on veut que l'environnement virtual soit créé): `virtualenv DojoRobotframework`
- chargement: `source  DojoRobotframework/bin/activate`

#### Installation des libraries

Taper la commande (dans l'environnement virtuel pour ceux qui en ont un): `pip install -r requirements.txt`

## Un peu de théorie

### Structure des fichiers de test

#### Le premier, on s'en souvient toujours, même si c'est pas génial
Dans le répertoire **test_suites** se trouve le fichier `01_check_environment.robot`. Ce fichier définit deux tests cases dans la section `*** Test Cases ***`. Chaque *test case* est une succession d'expression robotframework visant à charger une donnée, la vérifier.

**En bref**: ce fichier comporte :

- Deux sections: `Settings` et `Test Cases`
- La section `Test Cases` comporte deux *test case*. Chacun de ces derniers comporte un libellé, et une série d'instructions (appelées **keywords** ) tabulées. 

Exécuter le avec la commande: `pybot test_suites/01_check_environment.robot`

#### Les logs générés

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


### Variables

Les variables sont, comme dans tout langage très utilisées en robotframework.
Elles peuvent avoir trois portées:

- *globale*: leur portée est visible sur toutes les test suites. Si une test suite en modifie la valeur, cela impactera les autres. Elles peuvent être déclarées en ligne de commande (cf plus bas) ou avec le mot clef `set global variable`
- *test suite*: sa durée de vie est cloisonnée à une test suite. Ces variables sont déclarées par le mot clef `set suite variable` ou par la section `*** Variables ***`:

```robotframework
*** Variables ***
${MA_VARIABLE_1}		Toto
${MA_VARIABLE_2}		1
```

- *test*: durée de vie cantonnée à un test. Elles peuvent être déclarées par le mot clef `set test variable` ou à la volée (ici on `MY_TEST_VARIABLE` vaudra `TotoTitiTata`):

```robotframework
*** Test Cases ***
Some Test
	${MY_TEST_VARIABLE}=	catenate	Toto	Titi	Tata
```
	
---
	
Les variables globales peuvent être déclarées en ligne de commande (très pratique pour spécifier un type de configuration) grâce à l'option `-v`ou `--variable`dans sa version longue:

```bash
$> pybot -v MA_VARIABLE_1:Toto --variable MA_VARIABLE_2:1 testsuite_directory/
```

### Comment écrire ses tests
#### Les testsuites
Un fichier correspond à une *testsuite*. 
Rien est obligatoire mais il est conseillé de réunir au sein d'un même fichier des tests fonctionnellement liés (car ils pourront partager des variables, de la doc, etc...).

Les tests au sein d'une *testsuite* seront déroulés de manière séquentiele, alors que deux testsuites pourraient très bien être lancées en parallèle.

Les campagnes de tests peuvent aussi être lancées sur des dossiers, incluant toute les testsuites contenues.

Normalement, les *test cases* d'une *test suite* doivent qualifier une même fonctionnalité et **si possible** être indépendants les uns des autres.

#### Gerkins est aussi possible

Il est aussi possible d'écrire ses tests en suivant le style *given-when-then* rendu célèbre par l'approche [behavior driven development](http://en.wikipedia.org/wiki/Behavior_Driven_Development). Jetez un oeil au fichier `03_data_driven_test`.

---


#### Phases d'initialisation et de clôture

Comme tout framework de test qui se respecte, la section `*** Settings ***` permet de déclarer:

- une phase d'initialisation d'une suite de tests grâce au mot `Suite Setup`  
- une phase de nettoyage d'une suite de tests grâce au mot `Suite Teardown`

Puis, localement à un `test case`, on peut aussi y préciser une phase d'initalisation et de nettoyage au **niveau de ce test**. Par exemple:


```robotframework
Some Test
	[Setup]  log to console     Initiating
	[Teardown]  run keyword if test failed      fatal error   Cannot continue
	should be equal     3       2
```

Ici, avant le déroulement du test, le message *Initiating* sera affiché à la console. Le test sera ensuite déroulé (et va échouer... ). En phase de *teardown*, le mot clef  `run keyword if test failed` va être déroulé. Comme sont nom l'indique, ce mot clef prend en paramétre un autre mot clef, `fatal error` et les arguments de ce mot clef, la chaîne `Cannot continue` ici. 

Petite parenthèse, `fatal error` interrompt la suite en cours. Ici on montre comment un test est déterminant pour les tests qui suivent.

---

#### Les tags

Grâce à la balise `[Tags]` il est possible de positionner des tags sur les *test cases*.

Par exemple, dans le cas où nous aurions le test suivant


```robotframework
*** Test Cases ***
Test Something
	[Tags] addon_non_mandatory
	Should Be Equal 10 	8
```


##### Critiques? Non critique? 

Outre le fait de permettre le regroupement de nos tests par thématique, on peut aussi spécifier la non criticité d'une thématique en ajoutant l'option `--noncritical`. Dans notre cas, si on ajoute  `--noncritical  addon_non_mandatory`, on spécifie que **tous** les tests portant le tag `addon_non_mandatory` ne sont pas critiques.

:pencil2: Exercice:

- Ajouter des tags sur  `02_keyword.robot` de façon à rendre les tests sur l'humeur et  la compagnie non critiques
- Exécuter et constater que le fichier **report.html** filtre bien les tests spécifiés. 


## En pratique

### A vous de jouer

#### L'application de démo

Sous le répertoire **app-to-test** se trouve le fichier `login.py`. Taper `python app-to-test/login.py -h` et familiarisez vous avec.

#### La librairie Python fournie

Nous l'avons évoqué, RobotFramework permet de créer ses propres librairies (en python ou java). Pour cette exercice nous vous fournisson une librairies python (dans le répertoire lib) définissant quelques mots-clés vous permettant de manipuler l'application de démo.

#### Au boulot!

Editez le fichier `04_login_app_tests.robot`. Il contient des tests à compléter afin de valider le fonctionnement de l'application `login.py`



# Aller plus loin


-  Utilisez la puissance de librairie BuiltIn (`· Wait Until Keyword Succeeds`, `Run Keyword And Expect Error`, ...)
-  Créer ses propres librairies
-  Utiliser selenium (demo)
-  Integration continue, parallelisme


# Merci!

Quelques liens pour la route:

- [la doc] (http://robotframework.org/robotframework/)
- [de très bon conseils sur la rédaction des tests] (https://github.com/robotframework/HowToWriteGoodTestCases/blob/master/HowToWriteGoodTestCases.rst)

