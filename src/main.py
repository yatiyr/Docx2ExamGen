import sys

import Exam as ex
import xml.etree.ElementTree as ET
from lxml import etree
import copy
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

if __name__ == "__main__":


    dict = {}
    paragraphs = []


    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if file_path == '':
        sys.exit()


    control = []
    control = file_path.split('.')
    if control[1] != 'docx':
        messagebox.showerror("Error", "You must choose a docx file to continue!")
        sys.exit()

    exam = ex.Exam(file_path)

    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    USER_INP = simpledialog.askinteger(title="Group",
                                      prompt="Oluşturmak istediğiniz grup sayisini giriniz: ")

    if USER_INP >10 or USER_INP <= 0:
        messagebox.showwarning("Warning", " Lütfen 1 ile 10 arasi bir sayi giriniz!")
        sys.exit()
    else:
        messagebox.showinfo("Basarili!", "Sinav gruplariniz basariyla olusturuldu.")



    exam.produceExamGroups(USER_INP)

