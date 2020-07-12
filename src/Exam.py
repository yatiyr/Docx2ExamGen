import io
import zipfile as z
import Zipper as customZipper
import xml.etree.ElementTree as ET
from lxml import etree


class Exam:

    ET.register_namespace('w14', 'http://schemas.microsoft.com/office/word/2010/wordml')
    ET.register_namespace('wp14', 'http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing')
    ET.register_namespace('mc', 'http://schemas.openxmlformats.org/markup-compatibility/2006')
    ET.register_namespace('wpg', 'http://schemas.microsoft.com/office/word/2010/wordprocessingGroup')
    ET.register_namespace('wps', 'http://schemas.microsoft.com/office/word/2010/wordprocessingShape')
    ET.register_namespace('wp', 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing')
    ET.register_namespace('w10', 'urn:schemas-microsoft-com:office:word')
    ET.register_namespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
    ET.register_namespace('v', 'urn:schemas-microsoft-com:vml')
    ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')
    ET.register_namespace('o', 'urn:schemas-microsoft-com:office:office')

    def __init__(self, inputFilePath):
        self._parser = etree.XMLParser(encoding='utf-8', remove_blank_text=True)
        self.zipper = customZipper.Zipper()
        self.blueprint = z.ZipFile(inputFilePath)
        self.prefix = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

        fileNameList = self.blueprint.namelist()

        # Traverse archived docx file and add all files
        # except document.xml to zipper
        for fName in fileNameList:
            with self.blueprint.open(fName) as f:
                if fName == 'word/document.xml':
                    # xmlstr = ET.tostring(self.docXMLRoot, encoding='utf-8', method="xml")
                    #elem = etree.XML(f.read(), parser=self._parser)
                    self.docXMLRoot = etree.fromstring(f.read())
                    #self.zipper.addFile(fName, etree.tostring(self.docXMLRoot))

                else:
                    self.zipper.addFile(fName, f.read())


                

