import Exam as ex
import xml.etree.ElementTree as ET
from lxml import etree
import copy
import random

if __name__ == "__main__":


    dict = {}
    paragraphs = []

    exam = ex.Exam('inputs/input1.docx')


    random.shuffle(exam.questions)

    for q in exam.questions:
        
        exam.addParagraphs(q.paragraphs)
        exam.addParagraph(exam.blank)
        


    print(len(exam.questions))

    exam.writeDocx('asd.docx')