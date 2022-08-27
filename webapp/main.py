from os.path import dirname, abspath, join
from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

generator = pipeline('text-generation', model='openai-gpt')
current_dir = dirname(abspath(__file__))
static_path = join(current_dir, "static")

app = FastAPI()
app.mount("/ui", StaticFiles(directory=static_path), name="ui")

class Body(BaseModel):
    text: str


@app.get('/')
def root():
    return FileResponse("static/index.html")


@app.post('/generate')
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]
