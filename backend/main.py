from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to StudyOS!"}

@app.get("/hello")
def hello():
    return {"message": "Hello Ryan!"}
@app.get("/health")
def health():
    return {"status": "healthy"}
