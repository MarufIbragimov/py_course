"""
Реализовать CRUD для списка книг
* get all
* get by id
* create
* update
* delete

{
"title": "Book1",
"description": "Very old book",
"author": "Vasya Federov"
}

"""

import json
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()

books = [
    {
        'id': 1,
        'title': 'Harry Potter and the Chamber of Secrets',
        'description': """Harry returns to Hogwarts to face a terrifying monster 
            unleashed from the mysterious Chamber of Secrets, threatening the lives 
            of the students and revealing dark secrets about the school's past""",
        'author': 'J.K. Rowling'
    },
    {
        'id': 2,
        'title': 'The Amulet of Samarkand',
        'description': """a young magician's apprentice summons a powerful, witty djinn 
            to steal a legendary artifact, plunging them both into a world of magical 
            intrigue and political conspiracy""",
        'author': 'Jonathan Stroud'
    }
]


@app.get('/')
def ping():
    return {'message': 'Server is up and running'}


@app.get('/books', summary='Get the list of all books', tags=['books'])
def get_all_books():
    return Response(
        json.dumps(books),
        status_code=200,
        media_type='application/json'
    )


@app.get("/books/{book_id}", summary="Get book by ID", tags=["books"])
def books_by_id(book_id: int):
    for book_dict in books:
        if book_dict['id'] == book_id:
            return Response(
                json.dumps(book_dict),
                status_code=200,
                media_type='application/json'
            )
    return Response(
        json.dumps({'error': 'book not found'}),
        status_code=404,
        media_type='application/json'
    )


class Book(BaseModel):
    title: str
    description: str
    author: str


@app.post('/books', summary='Add new book', tags=['books'])
def add_book(book: Book):
    book_dict = book.model_dump()
    book_dict['id'] = len(books) + 1

    books.append(book_dict)

    return Response(
        json.dumps({'message': 'successfully added new book'}),
        status_code=201,
        media_type='application/json'
    )


@app.put('/books/{book_id}', summary='Update book by ID', tags=['books'])
def update_task(book_id: int, book: Book):
    for book_dict in books:
        if book_dict['id'] == book_id:
            book_dict['title'] = book.title
            book_dict['description'] = book.description
            book_dict['author'] = book.author

            return Response(
                json.dumps({'message': 'successfully updated book info'}),
                status_code=200,
                media_type='application/json'
            )
    return Response(
        json.dumps({'error': 'book with this ID is not found'}),
        status_code=404,
        media_type='application/json'
    )


@app.delete('/books/{book_id}', summary='Delete book by ID', tags=['books'])
def delete_book(book_id: int):
    for book_dict in books:
        if book_dict['id'] == book_id:
            books.pop(books.index(book_dict))
            return Response(
                json.dumps({'message': 'successfully deleted book'}),
                status_code=200,
                media_type='application/json'
            )
        
    return Response(
        json.dumps({'error': 'book with this ID is not found'}),
        status_code=404,
        media_type='application/json'
    )