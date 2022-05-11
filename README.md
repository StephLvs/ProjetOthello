# ProjetOthello

_A minute to learn… A lifetime to master!_

## Auteurs

- Elise Grelaud : 195247
- Stéphanie Reyes Loveranes : 195379

## Informations sur le jeu Othello

But : Créer une IA étant capable de jouer de manière intelligente au jeu Othello.
Nom de l'IA : MaterialGworlz111
Port par défaut : 2000

## Guide d'installation

1. Cloner ou télécharger le dossier _PI2CChampionshipRunner_ via [GitHub](https://github.com/qlurkin/PI2CChampionshipRunner.git) ou en écrivant dans le terminal :

```shell
git clone https://github.com/qlurkin/PI2CChampionshipRunner.git
```

2. Cloner ou télécharger le dossier _ProjetOthello_ via [GitHub](https://github.com/elisenium/ProjetOthello.git) ou en écrivant dans le terminal :

```shell
git clone https://github.com/elisenium/ProjetOthello.git
```

### Comment jouer...

#### contre une autre IA

- Démarrer le serveur :
    - Ouvrir un 1er terminal dans le dossier _PI2CChampionshipRunner_ et taper :
    ```shell
    python server.py othello
    ```
- Inscrire l'IA auprès du serveur
    - Adapter l'adresse IP dans `playerAddress` du fichier Bot1.py
    - Ouvrir un 2e terminal dans le dossier _ProjetOthello_ et taper :
    ```shell
    python Bot1.py
    ```
Le jeu se lance dès que deux joueurs sont connectés au serveur.

#### contre une IA Random
- Démarrer le serveur
    - Ouvrir un 1er terminal dans le dossier _PI2CChampionshipRunner_ et taper :
    ```shell
    python server.py othello
    ```
- Inscrire l'IA auprès du serveur
    - Adapter l'adresse IP dans `playerAddress` du fichier Bot1.py
    - Ouvrir un 2e terminal dans le dossier _ProjetOthello_ et taper :
    ```shell
    python Bot1.py
    ```
- Inscrire le Bot Random auprès du serveur
    - Ouvrir un terminal dans le dossier _ProjetOthello_ et taper :
    ```shell
    python RandomAI.py
    ```
    Le jeu devrait se lancer en Bot1 Vs. Random-Bot.

## Stratégie de l'IA

Afin que notre IA puisse choisir le meilleur coup possible, nous avons créé une liste nommée `weighted_board`. Cette liste est classée du meilleur au pire coup que l'IA pourrait choisir. Cette sélection priorise d'abord les quatres coins du plateau de jeu. Plus la position du numéro de la case est proche du début de la liste `weighted_board`, mieux c'est. La case la plus proche du début de la liste sera donc choisie en priorité sur tous les `possibleMoves`.

```python
weighted_board = [0,7,56,63,2,5,58,61,16,23,40,47,3,4,24,31,32,39,59,60,18,21,42,45,19,20,26,29,34,37,43,44,11
                  ,12,25,27,28,30,33,35,36,38,51,52,10,13,17,22,41,46,50,53,1,6,8,15,48,55,57,62,9,14,49,54]
```

## Bibliothèques utilisées
- json
- socket
- secrets (choice)
- copy