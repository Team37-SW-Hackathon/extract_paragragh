from fastapi import FastAPI,File, UploadFile
from typing import Optional
from extract_eng import start_eng, test
from extract_kor import start_kor
from pydantic import BaseModel


class Url(BaseModel):
    file: Optional[UploadFile]
    name:str
    startpg:int
    endpg:int


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
def ext_paragraph(url: Url):
    path=f"./data/{url.name}"
    print(url.name.filename)
    return start_eng(path)