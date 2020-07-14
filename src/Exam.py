import io
import zipfile as z
import Zipper as customZipper
import xml.etree.ElementTree as ET
from lxml import etree
import copy
import Question
import random
import Choice


class Exam:

    def __init__(self, inputFilePath):
        self._parser = etree.XMLParser(encoding='utf-8', remove_blank_text=True)
        self.zipper = customZipper.Zipper()
        self.blueprint = z.ZipFile(inputFilePath)
        self.prefix = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        self.paragraphs = []
        self.questions = []

        self.blank = etree.fromstring("""<w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:pPr><w:pStyle w:val="Normal"/><w:ind w:left="0" w:right="0" w:hanging="0"/><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="20"/><w:lang w:val="tr-TR"/></w:rPr></w:pPr><w:r><w:rPr><w:sz w:val="20"/><w:lang w:val="tr-TR"/></w:rPr></w:r></w:p>""")
        fileNameList = self.blueprint.namelist()

        # Traverse archived docx file and add all files
        # except document.xml to zipper
        for fName in fileNameList:
            with self.blueprint.open(fName) as f:
                if fName == 'word/document.xml':
                    self.docXMLRoot = etree.fromstring(f.read())
                else:
                    self.zipper.addFile(fName, f.read())

        self.body = self.docXMLRoot.find(self.prefix + "body")

        for paragraph in self.docXMLRoot.iter(self.prefix + "p"):
            clone = copy.deepcopy(paragraph)
            self.paragraphs.append(clone)
        
        # clear document
        for paragraph in self.docXMLRoot.iter(self.prefix + "p"):
            self.body.remove(paragraph)

        # get questions
        for i in range(len(self.paragraphs)):
            paragraphText = self.getParagraphText(self.paragraphs[i])

            if ("@" in paragraphText) and not("@&" in paragraphText):
                pars = [self.paragraphs[i]]
                j = 1

                while not ("$" in self.getParagraphText(self.paragraphs[i + j])):
                    pars.append(self.paragraphs[i + j])
                    j += 1
                if "$" in self.getParagraphText(self.paragraphs[i + j]):
                    pars.append(self.paragraphs[i + j])
                
                q = Question.Question(pars)
                self.questions.append(q)

                i = i + j
                
    #def shuffleQuestions(self):
    #    random.shuffle(self.questions)
    #    for q in self.questions:
    #        q.shuffleChoices()

    def clearRoot(self):
        for paragraph in self.docXMLRoot.iter(self.prefix + "p"):
            self.body.remove(paragraph)

    def writeQuestions(self):

        random.shuffle(self.questions)

        for i in range(len(self.questions)):

            questionPars, choices = self.questions[i].writeQuestion(i+1)

            for qP in questionPars:
                self.body.append(qP)
            for c in choices:
                for cP in c.pars:
                    self.body.append(cP)

            self.addBlankP()
        

    def getParagraphText(self, p):
        text = ""
        for t in p.iter(self.prefix + "t"):
            text += t.text

        return text

    def addBlankP(self):
        clone = copy.deepcopy(self.blank)
        self.body.append(clone)

    def writeDocx(self, filename):
        self.writeQuestions()
        zC = copy.deepcopy(self.zipper)
        zC.addFile('word/document.xml', etree.tostring(self.docXMLRoot))
        zC.writeToFile(filename)
        answerSheetFileName = filename.replace(".docx", "Cevaplar.txt")
        self.addAnswerSheet(answerSheetFileName)

    def addParagraphs(self, pars):
        for p in pars:
            clone = copy.deepcopy(p)
            self.body.append(clone)

    def addParagraph(self,p):
        clone = copy.deepcopy(p)
        self.body.append(clone)

    def addAnswerSheet(self, fileName):

        with open(fileName, 'a') as out:
            
            for i in range(len(self.questions)):

                for j in range(len(self.questions[i].choices)):
                    
                    if self.questions[i].choices[j].isTrue:
                        
                        out.write(str(i+1) + ") " + chr(65 + j) + '\n')


    def produceExamGroups(self, groupNumber):
        
        for i in range(groupNumber):
            self.writeDocx("Grup" + chr(65 + i) + ".docx")
            self.clearRoot()


                

