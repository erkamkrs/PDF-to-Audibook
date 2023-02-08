import pyttsx3
import pdfplumber
import PyPDF2

# Change the path to the desired PDF file's absolute path
sample_file = '/Users/muhammedkiris/PycharmProjects/PDF-to-Audibook/samplefile.pdf'

# Creating a PDF File Object
pdfFileObj = open(sample_file, 'rb')

# Creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

#Get the number of pages
pages = len(pdfReader.pages)

with pdfplumber.open(sample_file) as pdf:
    for i in range(0, pages):
      page = pdf.pages[i]
      text = page.extract_text()
      print(text)
      speaker = pyttsx3.init()
      speaker.say(text)
      speaker.runAndWait()