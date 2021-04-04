"""Module contenant les modes d'exécution du projet

Ce module contient les fonctions qui seront exécutés selon le choix
de l'utilisateur.

"""
import json
import os
from os.path import isfile, join
from pathlib import Path
import codecs


from src.Graph import Graph

from src.Algorithms.acceptation import acceptation
from src.Algorithms.determinisation import determinisation
from src.Algorithms.acceptation import acceptation
from src.Algorithms.synchronisation import synchronisation, clean_graph
from src.Algorithms.minimisation import minimisation
from src.Algorithms.thompson import thompson
from src.Algorithms.equivalence import equivalence

from src.Automate_from_json import generate_automate
from src.Random_lang import generate_lang, valid_node
from src.graph_to_json import getgraph, write_to_json_file

global files_path
files_path = Path('.\\Files\\')


def read_files():
    """Traitement des fichiers du dossier 'Files'

    Cette fonction parcours tout les fichiers ayant l'extension
    '.txt', et une syntaxe correcte sous le format décrit ci-dessous
    pour les transformer en fichier JSON puis en automate avec graphviz

    Example:
        * La premier ligne contient les états finaux séparés par des espaces
        1 2 3
        * Le reste du fichier contient les transitions sous le format:
        <état de départ> <caractère à lire> <état d'arrivé>

    """
    input_files = (
        entry for entry in files_path.iterdir() if entry.is_file())
    # Parcours récursif de tout les fichiers dans le dossier Files
    # 1 fichier == 1 langage/graphe
    for filename in input_files:
        # ouvrir en mode lecture
        with codecs.open(os.path.join(os.getcwd(), filename), encoding='utf-8') as f:
            # parse le fichier et récupérer l'alphabet, les noeuds et états finaux
            graph = Graph(f)
            graph.parse()
            num_exo = filename.name.split('.')[0]
            name = filename.name.split('.')[0] + '.json'
            print(name)

            json_graph = getgraph(graph)
            write_to_json_file(name, json_graph)

            # Exécuter les algorithmes
            # synchronisation
            eps = synchronisation(graph)
            eps_json = getgraph(eps)
            write_to_json_file(num_exo+"-eps.json", eps_json)

            # determinisation
            det = determinisation(eps)
            det_json = getgraph(det)
            write_to_json_file(num_exo+"-det.json", det_json)

            # Minimisation
            gmin = minimisation(det)
            gmin_json = getgraph(gmin)
            write_to_json_file(num_exo+"-min.json", gmin_json)

            # acceptation
            # res = acceptation(graph, ['abab', 'bab', 'bca'])

    generate_automate()


def gen_auto(n):
    """Fonction de génération automatique d'automates

    La fonction génère des automates aléatoires en utilisant le module
    'Random_lang', et les stocke dans un fichier txt

    Args:
        n (int): Nombre d'automates à générer

    """
    i = 1
    while i < n+1:
        filename = "Ex1-" + str(i)
        with open(os.path.join(os.getcwd(), '.\\Files\\' + filename + ".txt"), 'w') as outfile:
            g = generate_lang()
            final = " ".join(g.finalStates) + "\n"
            outfile.write(final)
            for node in g.transitions:
                outfile.write(
                    " ".join([node.mFrom, node.mValue, node.mGoto]) + "\n")
            i = i + 1
            outfile.close()


def gen_thompson(exp):
    """Fonction de création d'automate depuis une expression régulière

    Args:
        exp (str): Expression régulière à transformer

    """
    gt = thompson(exp)
    gt_json = getgraph(gt)
    write_to_json_file("thompson.json", gt_json)

    sync_th = synchronisation(gt)
    sync_json = getgraph(sync_th)
    write_to_json_file("thompson-sync.json", sync_json)

    # determinisation
    det = determinisation(sync_th)
    det_json = getgraph(det)
    write_to_json_file("thompson-det.json", det_json)

    # Minimisation
    gmin = minimisation(det)
    gmin_json = getgraph(gmin)
    write_to_json_file("thompson-min.json", gmin_json)

    generate_automate()


def check_equivalence():
    input_files = (
        entry for entry in files_path.iterdir() if entry.is_file())
    # Parcours récursif de tout les fichiers dans le dossier Files
    # 1 fichier == 1 langage/graphe
    number_files = len(os.listdir(files_path))
    if number_files != 2:
        print('Veuillez mettre 2 automates dans le dossier /Files/.')
    else:
        graph1 = Graph()
        graph2 = Graph()
        num = 1
        for filename in input_files:
            # ouvrir en mode lecture
            with codecs.open(os.path.join(os.getcwd(), filename), encoding='utf-8') as f:
                # parse le fichier et récupérer l'alphabet, les noeuds et états finaux
                graph = Graph(f)
                graph.parse()
                num_exo = filename.name.split('.')[0]
                name = filename.name.split('.')[0] + '.json'
                print(name)

                json_graph = getgraph(graph)
                write_to_json_file(name, json_graph)

                # Exécuter les algorithmes
                # synchronisation
                eps = synchronisation(graph)
                eps_json = getgraph(eps)
                write_to_json_file(num_exo+"-eps.json", eps_json)

                # determinisation
                det = determinisation(eps)
                det_json = getgraph(det)
                write_to_json_file(num_exo+"-det.json", det_json)

                # Minimisation
                gmin = minimisation(det)
                gmin_json = getgraph(gmin)
                write_to_json_file(num_exo + "-min.json", gmin_json)
                if num == 1:
                    graph1 = gmin
                    num += 1
                else:
                    graph2 = gmin
        equivalence(graph1, graph2)

    generate_automate()
