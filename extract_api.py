from fastapi import FastAPI
from extract_eng import start_eng, test
from extract_kor import start_kor



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