#
#   Python DFA
#
import sys
from exe_modes import read_files, gen_auto, gen_thompson

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('\nVeuillez choisir le mode d\'execution:\n')
        print(
            '\npython ./MainEntry -g <n>  \nn = nombre de langages à générer (Par défaut 3)\n')
        print('\npython ./MainEntry -f \nPour utiliser les fichiers de /Files/\n')
        print('\npython ./MainEntry -t <exp> \n Pour générer un automate avec l\'expression régulière <exp>\n')
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

        # main()
        # gt = thompson('a.(a+b)*.b')
        # gt = thompson('a+b')
        # gt = thompson('a*.(a+b).b*')
        # gt_json = getgraph(gt)
        # write_to_json_file("Thompson.json", gt_json)
        # generate_automate()
