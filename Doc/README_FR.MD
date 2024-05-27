# MDW NoCodePython

Fatigué de regarder des milliers de tutoriels sans apprendre Python ?  
Fatigué de ne pas avoir un moyen facile d'apprendre ?  

Avec **NoCodePython**, c'est fini. Ce programme est facile à utiliser et conçu pour les débutants qui veulent commencer à pratiquer sans avoir à apprendre les bases d'abord. Avec **NoCodePython**, vous pouvez créer vos propres applications et scripts sans avoir besoin de savoir programmer en Python, il suffit d'utiliser le langage naturel.

**NoCodePython** n'est pas fait pour remplacer le système de programmation traditionnel, mais il sert à transformer le langage naturel en code, ce qui permet d'expérimenter et d'apprendre la logique plus rapidement.

## Que pouvez-vous faire avec **NoCodePython** ?

Pour le moment, le développement est limité à l'utilisation de Python de base, sans bibliothèques supplémentaires. Cependant, le développement continue et on ne sait pas jusqu'où il ira.

## Comment programmer avec **NoCodePython** ?

**NoCodePython** a sa propre syntaxe mais essaie d'être aussi naturelle que possible.

### Syntaxe actuelle

**Remarque :**  
Il existe des expressions spécifiques pour les chaînes, comme `imprime <texte à imprimer>`, qui n'imprimera que le texte, qu'il ait des guillemets ou non ; en fait, il ne doit pas en avoir. En revanche, dans `concatène texteA avec texteB dans VariableEnregistrer`, il est nécessaire que si `texteA` ou `texteB` ne sont pas des variables, ils soient entourés de guillemets.

### Déclaration de variables

Pour enregistrer une variable, vous devez lui donner un contenu et un nom.

Exemples :
```
enregistre "contenu" dans nomVariable
enregistre 10 dans âge
```

### Utiliser des variables

Exemple :
```
enregistre 23 dans nombre1
ajoute nombre1 avec 23 dans résultat
```

### Imprimer à la console

Il y a deux modes : variables et chaînes.

- `imprime variable` : imprimera le contenu de la variable.
- `imprime` : imprimera ce que vous introduisez comme une chaîne.

Exemples :
```
imprime Bonjour le monde
enregistre "Bonjour le Monde" dans chaîne
imprime variable chaîne
```

### Opérations

Les opérations peuvent se faire de la manière suivante :

Exemple :
```
ajoute 23 avec 21 dans résultat
```
(Il enregistrera le résultat dans la variable `résultat`).

Pour les autres opérations, c'est la même chose avec leurs noms respectifs :
- ajoute
- soustrait
- multiplie
- divise
- élève (donner un exposant à quelque chose)
- extrait (faire la racine de quelque chose)

### Travailler avec du texte

Pour concaténer du texte, nous utilisons `concaténer`.

Exemple :
```
concatène "contenu1" avec "contenu2" dans résultat
```
(Il enregistrera le résultat dans la variable `résultat`).

### Conditionnelles

Les conditionnelles fonctionnent sur une ligne avec des virgules. Voyons quelques exemples :

```
enregistre 1 dans nombre
si 1 est égal à nombre, alors imprime C'est égal, enregistre égal dans comment_c_est
```

```
enregistre 2 dans nombre
si 3 est inférieur à nombre, alors imprime C'est inférieur, sinon imprime C'est supérieur
```

### Boucles

Nous avons plusieurs types de boucles, en commençant par les plus faciles.

Répéter quelque chose `n` fois.

Exemple :
```
répète 32 fois imprime 23
```
(Il imprimerait `23` 32 fois).

Un autre exemple :
```
enregistre 0 dans compteur
répète 10 fois ajoute 1 avec compteur dans compteur
imprime compteur
```

Il est évident que ce code a besoin d'optimisation, mais c'est la version 0.1.1v, donc il est possible qu'il y ait des erreurs ainsi que des défauts d'optimisation.

Un autre type est pendant que quelque chose se passe, fais quelque chose.

```
enregistre 0 dans compteur
pendant que compteur est inférieur à 10, fais imprime C'est inférieur, ajoute 1 avec compteur dans compteur
```

Il y a un autre type qui parcourt les listes mais il présente encore des erreurs, pour l'instant, nous avons ces deux-là.

### Les opérateurs

Il n'y a pas grand-chose à expliquer sur les opérateurs, ce sont juste ceux-ci :

- est égal à
- est différent de
- est supérieur à
- est inférieur à
- est supérieur ou égal à
- est inférieur ou égal à
```