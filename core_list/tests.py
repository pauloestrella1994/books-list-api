from django.test import TestCase
import requests


class TestAuthors:
    url_base = 'http://127.0.0.1:8000/books_list/'

    def test_get_books(self):
        books_get = requests.get(url=self.url_base)

        assert books_get.status_code == 200

    def test_get_book(self):
        book_get = requests.get(url=f'{self.url_base}1/')

        assert book_get.status_code == 200

    def test_post_book(self):
        book_post = {"name": "Python Fluente", "edition": 1,"publication_year": 2005}
        result = requests.post(url=self.url_base, data=book_post)

        assert result.status_code == 201
        assert result.json()['name'] == book_post['name']

    def test_put_book(self):
        book_put = {"name": "Python Fluente 2", "edition": 1,"publication_year": 2005}
        result = requests.put(url=f'{self.url_base}1/', data=book_put)
        
        assert result.status_code == 200
        assert result.json()['name'] == book_put['name']
    
    # def test_delete_book(self):
    #     result = requests.delete(url=f'{self.url_base}15/')

    #     assert result.status_code == 404 and len(result.text) == 0