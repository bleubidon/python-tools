from pdf2image import convert_from_path
import os; os.chdir(r'C:\Users\user\Downloads')

input_pdf = 'file.pdf'
images = convert_from_path(input_pdf)

for i in range(len(images)):
    images[i].save(input_pdf.split('.pdf')[0] + '_page' + str(i) + '.jpg', 'JPEG')