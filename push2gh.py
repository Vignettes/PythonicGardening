import mdutils
import shutil
from mdutils.mdutils import MdUtils
from mdutils import fileutils
import sys, tempfile, os
import subprocess



# User lands at a screen prompting creation of credentials file

# If the user already has the credentials file skips to main menu
## Main menu consists of the following options:

### Choose branch
#
### Choose folder to create doc 
#
### Create new file
# Ask user for value for file name
fileName = input("File Name?") +".md"
# Ask user for value for file title; consider asking to default to bind
fileTitle = str(input("File Title?"))
#
contentDir = r"/Users/georgewolf/Documents/GeorgeOnTheWeb/content/"
template = r"/Users/georgewolf/Documents/PythonicGardening/template.md"
# Define yaml frontmatter for title as header variable; consider adding other frontmatter options
#header = "---\n"+"title: {fileTitle}\n"+"---"
# Create new Markdown file using fileName and userTitle
def createFile(fileName, fileTitle):
    usrChoice = input("Enter 1 to create a new file from template: ")
    if usrChoice == "1":
        shutil.copy2(template, contentDir)
        subprocess.call(['vim', contentDir+fileName])
    else:
        exit
createFile(fileName, fileTitle)

#with tempfile.NamedTemporaryFile(suffix='task') as temp:
 #   subprocess.call(['vim', fileName])
    
    #shutil.copy2(temp.name, 'mytest.md')    
    #EDITOR = open(temp.name, 'r').read()   
    #mdFile.MarkDownFile.append_after_second_line(fileName, data)
#mdutils.fileutils.MarkDownFilE(fileName, data).append_end(EDITOR)


# Add the header to the new file
# mdFile.new_paragraph(header)
# # 
# mdFile.new_header(level=1, title='Overview')  # style is set 'atx' format by default.

# mdFile.new_paragraph("This is an example of markdown file created using mdutils python package. In this example you "
#                      "are going to see how to create a markdown file using this library. Moreover, you're "
#                      "finding the available features which makes easy the creation of this type of files while you "
#                      "are running Python code.")
# mdFile.new_paragraph("**IMPORTANT:** some features available on this library have no effect with the GitHub Markdown "
#                      "CSS. Some of them are: coloring text, centering text...")



#### Create using template or raw
# 
### Edit existing file
#
## Exit  




