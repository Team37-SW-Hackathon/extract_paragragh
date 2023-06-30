import openai
from PyPDF2 import PdfReader
import json

PDF_FILE_PATH = "./data/eng.pdf"

with open('./secret.json') as f:
    secrets = json.loads(f.read())
DB_API_KEY = secrets["API_KEY"]




def extract_main(page):
  openai.api_key = DB_API_KEY

  text = f"""{page}"""
  instruction = f"""아래에서 영어 지문을 찾아줘.영어 지문은 3개 이상의 연속된 영어 문장으로 이루어져 있는 문단을 의미해. 영어지문은 한글을 포함하지 않아.선지는 1,2,3,4,5 번으로 이루어져 있고 지문 다음에 위치해, 선지는 지문이 아니야.아래에는 0~2개의 영어 지문이 존재할 수 있어.영어지문만 그대로 출력해. 영어지문이 없다면 아무것도 출력하지마.\n\n\n{text}"""
 
  model="gpt-3.5-turbo"
  messages=[{"role": "user", "content":instruction}]
    
  response = openai.ChatCompletion.create(
      model = model,
      messages = messages,
      temperature = 0.5,
      top_p = 0.3,
      max_tokens=512,
      presence_penalty=0,
      frequency_penalty=0,
  )
   
  output_text = response.choices[0].message["content"]
  print(output_text)
  return output_text



def start_eng(path):
  reader = PdfReader(path)
  pages = reader.pages
  cnt=0
  paragraphs = []
  for page in pages:
      cnt +=1
      if(cnt>=12 and cnt<14):
        sub = page.extract_text()
        paragraph = extract_main(sub)
        
        paragraph = paragraph.split('\n\n')
        for i in range(len([paragraph])):
          paragraph[i] = paragraph[i].replace('\n','')
          paragraphs.append(paragraph[i])
        print("\n\n\n------------------------------------------------------")

  return {'paragraphs':paragraphs}



    
def test():
   return {"name" : "asdf"}