import pytest
from app import app, db, Book

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

def test_create_book(client):
    response = client.post('/books', json={
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'publication_year': 2021
    })
    assert response.status_code == 201
    assert response.json['title'] == 'Test Book'

def test_get_books(client):
    client.post('/books', json={
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'publication_year': 2021
    })
    response = client.get('/books')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_update_book(client):
    client.post('/books', json={
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'publication_year': 2021
    })
    response = client.put('/books/1', json={
        'title': 'Updated Test Book'
    })
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Test Book'

def test_delete_book(client):
    client.post('/books', json={
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'publication_year': 2021
    })
    response = client.delete('/books/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Book deleted'
