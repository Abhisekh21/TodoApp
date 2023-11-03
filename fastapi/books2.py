from fastapi import  FastAPI
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI()

class book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    
    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class BookRequest(BaseModel):
    id: Optional[int]=Field(title="id is not required")
    title: str=Field(min_length=5)
    author: str=Field(min_length=5)
    description: str=Field(min_length=5,max_length=100)
    rating: int=Field(gt=-1,lt=6)
    
    class Config:
        json_schema_extra={
            'example':{
                "title":"A new book",
                "auhtor":"codingwithroby",
                "description":"A new description of book",
                "rating":4
            }
        }
    
    
books=[
    book(1,"computer science pro","codewithroby","A very nice book!",5),
    book(2,"Be fast with Fastapi","codewithroby","A great book!",5),
    book(3,"master endpoints","codewithroby","A awesome book",5),
    book(4,"HP1","Author 1","Book Description",3),
    book(5,"HP2","Author 2","Book Description",2),
    book(6,"HP3","Author 3","Book Description",1)
]

@app.get("/books")
async def read_all_books():
    return books

@app.get('/books/{book_id}')
async def find_boook_id(book_id: int):
    for book in books:
        if book.id==book_id:
            return book

@app.get("/books/rating/{rating}")
async def find_by_rating(rating: int):
    for book in books:
        if book.rating==rating:
            return book

@app.post("books/upadate_book")
async def upadet_book(book: BookRequest):
    for i in range(len(books)):
        if books[i].id==book.id:
            books[i]=book

@app.post("/create_books")
async def createbooks(book_request: BookRequest):
    newbook=book(**book_request.model_dump())
    books.append(find_book_id(newbook))

def find_book_id(book: book):
    if len(books)>0:
        book.id=books[-1].id+1
    else:
        book.id=1
    return book


