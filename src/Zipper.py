import zipfile as z
import io

class Zipper:

    def __init__(self):
        self.zipInMemory = io.BytesIO()

    def addFile(self, fileName, fileContents):
        zf = z.ZipFile(self.zipInMemory, "a", z.ZIP_DEFLATED, False)

        zf.writestr(fileName, fileContents)

        for zFile in zf.filelist:
            zFile.create_system = 0
        
        return self

    def read(self):

        self.zipInMemory.seek(0)
        return self.zipInMemory.read()

    def writeToFile(self, fileName):

        f = open(fileName, "wb")
        f.write(self.read())
        f.close()
