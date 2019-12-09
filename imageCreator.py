import docx
from docx.shared import Mm

pageWidth = 210
pageHeight = 297
marginSize = 12.7

doc = docx.Document()
section = doc.sections[0]
section.page_height = Mm(pageHeight)
section.page_width = Mm(pageWidth)
section.left_margin = Mm(marginSize)
section.right_margin = Mm(marginSize)
section.top_margin = Mm(marginSize)
section.bottom_margin = Mm(marginSize)

imageFile = input("Enter file name : ")

images = []
images.append(imageFile)
images.append(imageFile)
images.append(imageFile)

width = ((pageWidth - (marginSize * 2)) / 2) - 10
height = ((pageHeight - (marginSize * 2)) / 3) - 5

for image in images:
    doc.add_picture(image,Mm(width),Mm(height))


doc.save("images.docx")