import io
import zipfile as z
import Zipper as customZipper

class Exam:

    def __init__(self, inputFilePath):
        self.zipper = customZipper.Zipper()
        self.blueprint = z.ZipFile(inputFilePath)
        self.documentXml = ""

        fileNameList = self.blueprint.namelist()

        # Traverse archived docx file and add all files
        # except document.xml to zipper
        for fName in fileNameList:
            with self.blueprint.open(fName) as f:
                if fName == 'word/document.xml':
                    self.documentXml = f.read()
                else:
                    self.zipper.addFile(fName, f.read())

                

