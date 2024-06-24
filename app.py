from fastapi import FastAPI
import uvicorn
from summarize import summarize

app = FastAPI()

@app.get('/')
def predict(text):
    return {
        'text':text,
        'summay':summarize(text)
    }

if __name__ == '__main__':
    uvicorn.run(app)