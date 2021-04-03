"""Module pour la génération de sujet d'examens de THL avec Latex
Todo:
"""
from pylatex import *
from pylatex.utils import bold
import os
from pathlib import Path

global doc
global geometry_options
global image_filename
global path
path = Path('.\\Results\\')


def generate_header():
    global doc
    # Add document header
    header = PageStyle("header")
    # Create left header
    with header.create(Head("L")):
        header.append("Universite Cergy Pontoise")
        header.append(LineBreak())
        header.append("irenee.briquel@gmail.com")
    # Create center header
    with header.create(Head("C")):
        header.append("Annee 2021")
    # Create right header
    with header.create(Head("R")):
        header.append("Automates et langages reguliers")
        header.append(LineBreak())
        header.append("L2")
    # # Create left footer
    # with header.create(Foot("L")):
    #     header.append("Left Footer")
    # # Create center footer
    # with header.create(Foot("C")):
    #     header.append("Center Footer")
    # # Create right footer
    # with header.create(Foot("R")):
    #     header.append("Right Footer")

    doc.preamble.append(header)
    doc.change_document_style("header")

    # Add Heading
    with doc.create(MiniPage(align='c')):
        doc.append(
            LargeText(bold("Examen de deuxieme session - Langages et automates")))
        doc.append(LineBreak())
        doc.append(MediumText(bold("Mardi 16 avril 2021")))


# def generate_exercise():
#     with doc.create(Section('The simple stuff')):


def generate_exercice(exo, images):
    global doc, image_filename
    corrections = ['det.png', 'min.png', 'eps.png']

    image_filename = os.path.join(os.getcwd(), '.\\Results\\' + exo + '.png ')
    image_det = os.path.join(os.getcwd(), '.\\Results\\' + exo + '-det.png ')
    image_min = os.path.join(os.getcwd(), '.\\Results\\' + exo + '-min.png ')

    with doc.create(Section('Exercice 1')):
        with doc.create(Subsection("Soit l'automate suivant:")):
            with doc.create(Figure(position='h!')) as automate:
                automate.add_image(image_filename, width='120px')
        with doc.create(Itemize()) as itemize:
            # Question 1
            itemize.add_item("Trouver l'automate deterministe.")
            with doc.create(Figure(position='h!')) as automate:
                automate.add_image(image_min, width='120px')
            # Question 2
            itemize.add_item("Trouver l'automate minimal.")
            with doc.create(Figure(position='h!')) as automate:
                automate.add_image(image_det, width='120px')
            # Question 3


def gen_exam():
    global doc, image_filename, geometry_options
    images = (
        entry for entry in path.iterdir() if entry.is_file())

    geometry_options = {"margin": "0.7in"}
    doc = Document(geometry_options=geometry_options)
    generate_header()

    for image in images:
        num = image.name.split('.')
        if len(num) > 1 and num[1] == 'png':
            exo = num[0].split('-')
            if (len(exo) == 2):
                exo = "-".join(exo)
                generate_exercice(exo, images)
                doc.generate_pdf(filepath='./Exam_PDF/exam' +
                                 exo[4], clean_tex=False)
    # doc = Document('basic')
    # doc.generate_pdf(filepath='./Exam_PDF/header', clean_tex=False)
    #     latex_document = './Files/l2automates.exam2018.s2.tex'
    #     with open(latex_document) as file:
    #         tex = file.read()
    #     doc.append(NoEscape(tex))
    #     doc.generate_pdf(filepath='./Exam_PDF/abab', clean_tex=False)

    # # geometry_options = {"tmargin": "0cm", "lmargin": "0cm"}
    # # doc = Document(geometry_options=geometry_options)

    # # doc.generate_pdf(filepath='./Exam_PDF/abab', clean_tex=False)
