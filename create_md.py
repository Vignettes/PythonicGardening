import mdutils
import shutil
from mdutils.mdutils import MdUtils
from mdutils import fileutils
import sys, tempfile, os
import subprocess
from config import *


def createFile():
    fileName = input("File Name? ") +".md"
    # fileTitle currently does not update the frontmatter in the MarkDown file
    fileTitle = input("File Title? ")
    #contentDir = "/Users/georgewolf/Documents/GeorgeOnTheWeb/content/notes/"
    #template = "/Users/georgewolf/Documents/PythonicGardening/template.md"
    shutil.copy(template, contentDir)
    os.rename(r"/Users/georgewolf/Documents/GeorgeOnTheWeb/content/notes/template.md", "/Users/georgewolf/Documents/GeorgeOnTheWeb/content/notes/"+fileName)
    os.chdir(contentDir)
    os.system("vi " + fileName)







