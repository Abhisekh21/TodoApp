from fastapi import Body,FastAPI

app=FastAPI()
BOOKS=[{'tittle':'title one','author':'author one','category':'science'},
       {'tittle':'title two','author':'author two','category':'science'},
       {'tittle':'title three','author':'author three','category':'history'},
       {'tittle':'title four','author':'author four','category':'maths'},
       {'tittle':'title five','author':'author five','category':'maths'},
       {'tittle':'title six','author':'author six','category':'maths'}]

@app.get("/books")
def read_allbooks():
    return BOOKS

@app.get("/books/{book_author}")
def read_all_books(book_author: str):
    book_return=[]
    for book in BOOKS:
        if book.get('author').casefold()==book_author.casefold() :
            return book


@app.get("/books/")
def read_all_books(category: str):
    book_return=[]
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            book_return.append(book)
    return book_return


@app.get("/books/{book_author}/")
def read_all_books(book_author: str,category: str):
    book_return=[]
    for book in BOOKS:
        if book.get('author').casefold()==book_author.casefold() and book.get('category').casefold() == category.casefold():
            book_return.append(book)
    return book_return

@app.post("/books/create_book")
async def createbook(newbook=Body()):
    BOOKS.append(newbook)
    
@app.put("/books/update_book")
async def updatebook(updatebook=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('tittle').casefold() == updatebook.get('tittle').casefold():
            BOOKS[i]=updatebook
            
@app.delete("/books/delete_book/{book_title}")
async def updatebook(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('tittle').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break