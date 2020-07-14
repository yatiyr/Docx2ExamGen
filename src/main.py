import Exam as ex
import xml.etree.ElementTree as ET
from lxml import etree
import copy
import random

if __name__ == "__main__":


    dict = {}
    paragraphs = []

    exam = ex.Exam('inputs/input1.docx')

    exam.produceExamGroups(5)
    print("deneme commiti")
