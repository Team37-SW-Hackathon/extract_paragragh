from fastapi import FastAPI,File, UploadFile
from extract_eng import start_eng, test
from extract_kor import start_kor
from pydantic import BaseModel


class Url(BaseModel):
    url:str


app = FastAPI()

@app.get("/eng")
def get_pargraph():
    return start_eng()

@app.get("/")
def get_home():
    print(test())
    return test()

@app.get("/kor")
def get_pargraph():
    return start_kor()


@app.post("/extract")
def ext_paragraph(file: UploadFile):
    path=f"./data/{file.filename}"
    return start_eng(path)