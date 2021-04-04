"""Point d'entré du programme

Ce point d'entré permet d'exécuter le projet selon un des modes d'execution possibles

Example: 
    $ python ./index -g <n> 
    $ python ./index -f
    python ./index -t <exp>

Todo:
    * Ajouter d'autres modes d'execution
"""
import sys
from src.exe_modes import read_files, gen_auto, gen_thompson, check_equivalence
from src.latex_gen import gen_exam

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('\nVeuillez choisir le mode d\'execution:\n')
        print('\npython ./index -f \nPour utiliser les fichiers de /Files/\n')
        print(
            '\npython ./index -g <n>  \nn = nombre de langages à générer (Par défaut 3)\n')
        print('\npython ./index -t <exp> \nPour générer un automate avec l\'expression régulière <exp>\n')
        print('\npython ./index -e\nPour générer un sujet d\'examen à partir des fichiers de Results\n')
        print('\npython ./index -q\nPour vérifier l\'équivalence de deux automate dans le dossier /Files/')
    else:
        if sys.argv[1] == '-g':
            if len(sys.argv) < 3:
                gen_auto(3)
            else:
                gen_auto(int(sys.argv[2]))
            read_files()
        elif sys.argv[1] == '-f':
            read_files()
        elif sys.argv[1] == '-t':
            if len(sys.argv) < 3:
                print('Donnez une expression régulière.')
            else:
                gt = gen_thompson('a.(a+b)*.b')
                # gt = thompson('a+b')
                # gt = thompson('a*.(a+b).b*')
                # gen_thompson(sys.argv[2])
        elif sys.argv[1] == '-e':
            gen_exam()
        elif sys.argv[1] == '-q':
            check_equivalence()
