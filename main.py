# uvicorn main:app --reload
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'home page'}}

@app.get('/blog')
def blog_list(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db loaded'}
    else:
        return {'data': f'{limit} blogs from db loaded'}

@app.get('/blog/{blog_id}')
def show_blog_by_id(blog_id: int):
    return {'data': blog_id}

@app.get('/blog/{blog_id}/comments')
def blog_comments(blog_id):
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Created a new blog with title {blog.title}"}

#for debug
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)