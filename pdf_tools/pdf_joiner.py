from PyPDF2 import PdfMerger
import os; os.chdir(r'C:\Users\user\Downloads')

pdfs = ["file_1.pdf", "file_2.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("joined.pdf")
merger.close()
