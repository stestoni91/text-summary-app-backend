from fastapi import FastAPI
import uvicorn
from summarize import summarize

app = FastAPI()

@app.post('/')
def predict(text):
    return {
        'text':text,
        'summary':summarize(text)
    }

if __name__ == '__main__':
    uvicorn.run(app)