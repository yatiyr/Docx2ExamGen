import sys

import Exam as ex
import xml.etree.ElementTree as ET
from lxml import etree
import copy
import random
import tkinter as tk
from tkinter import filedialog


if __name__ == "__main__":


    dict = {}
    paragraphs = []


    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    control = []
    control = file_path.split('.')
    if control[1] != 'docx':
        print('You must choose a docx file to continue!')
        sys.exit()

    exam = ex.Exam(file_path)

    exam.produceExamGroups(5)

