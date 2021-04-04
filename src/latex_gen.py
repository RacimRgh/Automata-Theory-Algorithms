"""Module pour la génération de sujet d'examens de THL avec Latex
Todo:
"""
from pylatex import *
from pylatex.utils import bold
import os
from pathlib import Path

global doc, doc_correction
global geometry_options
global image_filename
global path
path = Path('.\\Results\\')


def generate_header():
    """
    """
    global doc, doc_correction
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

    doc_correction.preamble.append(header)
    doc_correction.change_document_style("header")

    # Add Heading
    with doc.create(MiniPage(align='c')):
        doc.append(
            LargeText(bold("Examen de deuxieme session - Langages et automates")))
        doc.append(LineBreak())
        doc.append(MediumText(bold("Mardi 16 avril 2021")))

    # Add Heading
    with doc_correction.create(MiniPage(align='c')):
        doc_correction.append(
            LargeText(bold("Correctoin de l'examen de deuxieme session - Langages et automates")))
        doc_correction.append(LineBreak())
        doc_correction.append(MediumText(bold("Mardi 16 avril 2021")))


def generate_exercice(exo, images):
    global doc, image_filename

    # automate original
    image_filename = os.path.join(os.getcwd(), '.\\Results\\' + exo + '.png ')

    """
        Génération du contenu de l'examen
    """
    with doc.create(Section('Exercice 1')):
        with doc.create(Subsection("Soit l'automate suivant:")):
            with doc.create(Figure(position='h!')) as automate:
                automate.add_image(image_filename, width='120px')
        with doc.create(Itemize()) as itemize:
            # Question 1
            itemize.add_item("Trouver l'automate deterministe.")
            # Question 2
            itemize.add_item("Trouver l'automate minimal.")
            # Question 3
            itemize.add_item(
                "Trouver l'automate de thompson de l'expression: a(a+b)*b")


def generate_correction(exo, images):
    global doc_correction, image_filename

    # automate original
    image_filename = os.path.join(os.getcwd(), '.\\Results\\' + exo + '.png ')
    # automate déterministe
    image_det = os.path.join(os.getcwd(), '.\\Results\\' + exo + '-det.png ')
    # automate minimal
    image_min = os.path.join(os.getcwd(), '.\\Results\\' + exo + '-min.png ')
    # automate sans eps-transitions
    image_eps = os.path.join(os.getcwd(), '.\\Results\\' + exo + '-eps.png ')
    # automate de thompson
    image_thompson = os.path.join(
        os.getcwd(), '.\\Results\\' + exo + '-thompson.png ')
    """
        Génération de la correction
    """
    with doc_correction.create(Section('Exercice 1')):
        with doc_correction.create(Subsection("Soit l'automate suivant:")):
            with doc_correction.create(Figure(position='h')) as automate_corr:
                automate_corr.add_image(image_filename, width='120px')
        with doc_correction.create(Itemize()) as itemize_corr:
            # Question 1
            itemize_corr.add_item("Trouver l'automate deterministe.")
            with doc_correction.create(Figure(position='h')) as automate_corr:
                automate_corr.add_image(image_det, width='120px')
            # Question 2
            itemize_corr.add_item("Trouver l'automate minimal.")
            with doc_correction.create(Figure(position='h')) as automate_corr:
                automate_corr.add_image(image_min, width='120px')
            # Question 3
            itemize_corr.add_item(
                "Trouver l'automate de thompson de l'expression: a(a+b)*b")
            with doc_correction.create(Figure(position='h')) as automate_corr:
                automate_corr.add_image(image_thompson, width='120px')


def gen_exam():
    global doc, doc_correction, image_filename, geometry_options
    images = (
        entry for entry in path.iterdir() if entry.is_file())

    geometry_options = {"margin": "0.7in"}
    doc = Document(geometry_options=geometry_options)
    doc_correction = Document(geometry_options=geometry_options)
    generate_header()

    for image in images:
        num = image.name.split('.')
        if len(num) > 1 and num[1] == 'png':
            exo = num[0].split('-')
            if (len(exo) == 2):
                exo = "-".join(exo)
                generate_exercice(exo, images)
                generate_correction(exo, images)
                doc.generate_pdf(filepath='./Exam_PDF/exam' +
                                 exo[4], clean_tex=False)
                doc_correction.generate_pdf(filepath='./Exam_PDF/exam_correction' +
                                            exo[4], clean_tex=False)


########################################################################################
"""
    Compilation d'un document latex avec python
"""
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
########################################################################################
