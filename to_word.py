import aspose.words as aw

PDF_FILE_PATH = "./data/kor1.pdf"

# load the PDF file
doc = aw.Document(PDF_FILE_PATH)

# convert PDF to Word DOCX format
doc.save("pdf-to-word.docx")
