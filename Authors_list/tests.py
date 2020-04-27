from django.test import TestCase
import requests


class TestAuthors:
    url_base = 'http://127.0.0.1:8000/authors_list/'

    def test_get_authors(self):
        authors_get = requests.get(url=self.url_base)

        assert authors_get.status_code == 200

    def test_get_author(self):
        author_get = requests.get(url=f'{self.url_base}6/')

        assert author_get.status_code == 200

    def test_post_author(self):
        author_post = {"author_name": "Luciano Ramalho"}
        result = requests.post(url=self.url_base, data=author_post)

        assert result.status_code == 201
        assert result.json()['author_name'] == author_post['author_name']

    def test_put_author(self):
        author_put = {"author_name": "Luciano Ramalho 2"}
        result = requests.put(url=f'{self.url_base}6/', data=author_put)
        
        assert result.status_code == 200
        assert result.json()['author_name'] == author_put['author_name']
    
    def test_delete_author(self):
        result = requests.delete(url=f'{self.url_base}15/')

        assert result.status_code == 404 and len(result.text) == 0

    




