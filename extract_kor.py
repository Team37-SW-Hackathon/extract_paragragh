import openai
from PyPDF2 import PdfReader
import json
import re

PDF_FILE_PATH = "./data/kor1.pdf"   #문학


with open('./secret.json') as f:
    secrets = json.loads(f.read())
DB_API_KEY = secrets["API_KEY"]

def extract_main(page):
   return



def start_kor():
  reader = PdfReader(PDF_FILE_PATH)
  pages = reader.pages
  cnt=0
  paragraphs = []
  for page in pages:
      cnt +=1
      if(cnt>0):
        sub = page.extract_text()
        sub = sub.replace('\n','')
        print(sub)
        #paragraph = extract_main(sub)
        #paragraphs.append(paragraph)
        print("\n\n\n------------------------------------------------------")

  return {'paragraphs':paragraphs}
