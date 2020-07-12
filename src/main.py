import Exam as ex
import xml.etree.ElementTree as ET
from lxml import etree

if __name__ == "__main__":


    dict = {}
    fileNameList = []

    exam = ex.Exam('inputs/input1.docx')
    #xmlstr = ET.tostring(exam.docXMLRoot, encoding="unicode", method="xml")
    # print(xmlstr[0:10000])
    #for paragraph in exam.docXMLRoot.iter(exam.prefix + "p"):
    #    print(paragraph)
    #    pass

    for paragraph in exam.docXMLRoot.iter(exam.prefix + "p"):
        # print(paragraph)
        print(etree.tostring(paragraph))
        pass

    print(exam.docXMLRoot)
    #exam.zipper.writeToFile('eren.docx')