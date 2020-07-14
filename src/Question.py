import Choice
import random
import copy

class Question:

    def __init__(self, pars):
        self.paragraphs = pars
        self.prefix = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        self.questionPars = []
        self.choices = []


        for i in range(len(self.paragraphs)):
            paragraphText = self.getParagraphText(self.paragraphs[i])

            if "&" in paragraphText:
                choicePars = [self.paragraphs[i]]
                j = 1

                if i + j < len(self.paragraphs):
                    while not ("&" in self.getParagraphText(self.paragraphs[i + j])):
                        choicePars.append(self.paragraphs[i + j])
                        j += 1

                c = Choice.Choice(choicePars)
                self.choices.append(c)

                i = i + j

                
                    
            else:
                self.questionPars.append(self.paragraphs[i])

    
        self.choices[0].setIsTrue(True)

        # Delete $ at the end of last choice
        #for cParagraph 

    # TODO BURAYA BAK!!
    def giveQuestionNumber(self, number):
        p = self.questionPars

        # Question pars are deep copied because
        # we do not want to change actual paragraphs
        # for reusability
        cloneP = copy.deepcopy(p)

        for t in cloneP[0].iter(self.prefix + "t"):
            if "@" in t.text:
                t.text = t.text.replace("@", str(number) + ". ")

        return cloneP

    # This method gives a copy of modified
    # question paragraphs and choices
    def writeQuestion(self, number):

        # Choices are shuffled first
        self.shuffleChoices()

        cloneC = copy.deepcopy(self.choices)
        qP = self.giveQuestionNumber(number)

        # Enumerate choices
        for i in range(len(cloneC)):
            cParagraph = cloneC[i].pars[0]

            for t in cParagraph.iter(self.prefix + "t"):
                if "&" in t.text:
                    t.text = t.text.replace("&", chr(65 + i) + ")")
                if "$" in t.text:
                    t.text = t.text.replace("$", "")
        return qP, cloneC

    def shuffleChoices(self):
        random.shuffle(self.choices)    

    def getParagraphText(self, p):
        text = ""
        for t in p.iter(self.prefix + "t"):
            text += t.text

        return text

        

