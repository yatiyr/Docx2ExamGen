import Exam as ex
import xml.etree.ElementTree as ET
from lxml import etree
import copy

if __name__ == "__main__":


    dict = {}
    paragraphs = []

    exam = ex.Exam('inputs/input1.docx')
 

    ps = [exam.paragraphs[0], exam.paragraphs[1], exam.paragraphs[2], exam.paragraphs[3], exam.paragraphs[4], exam.blank]

    exam.addParagraphs(ps)

    for q in exam.questions:
        
        exam.addParagraphs(q.paragraphs)

        exam.addParagraph(exam.blank)
        exam.addParagraph(exam.blank)


    print(len(exam.questions))

    exam.writeDocx('asd.docx')