# Automata-Theory-Algorithms

Academic project that implements automata theory algorithms for Finite State Machines and Deterministic Finite State Machines

## Modes d'exécution

Le programme étant découpé en plusieurs modules réutilisables, il est possible d’appeler chaque fonction indépendamment des autres. Cependant il offre par défaut plusieurs modes d’exécution qui enveloppent les principales fonctionnalités, ces modes sont:

- Mode génération automatique de langages: en utilisant la commande
  $ python ./index.py -g <n>
  Ce mode permet de générer n langages automatiquement sous le format txt, générer les automates synchronisés, déterminés et minimales correspondants. Ensuite crée l’image de chacun de ces derniers
- Mode batch: En lisant les fichiers du dossier Files, créer des automates et exécuter leurs algorithmes pour les mettre dans le dossier Results sous format JSON et PNG.
  $ python ./index.py -f
- Mode génération d’automates de Thompson: cet algorithme nécessite des expressions régulières correctes et bien formatés, donc elles sont passées via l’invite de commande:
  $ python ./index.py -t “<exp>” # Exemple “a.(a+b)\*.b”
- Mode génération de sujets d’examens: A partir des automates créés précédemment, générer des sujets d’examens avec leurs corrections.
  $ python ./index.py -e
- Mode vérification de l’équivalence de deux automates: Ce mode étant ajouté vers la fin du développement, il est disponible en mode test seulement. Il doit obligatoirement avoir 2 fichiers texte dans le dossier Files pour l’exécuter, il calcule par la suite leurs automates minimaux et vérifiera l’équivalence
  $ python ./index .py -q
