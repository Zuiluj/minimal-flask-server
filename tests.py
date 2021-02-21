import json
import unittest

from server import app
from server import data
server_data = data


class MyServerTests(unittest.TestCase):
    """ A list of my own unit tests for my blog server """

    @classmethod
    def setUpClass(cls):
        """ Runs first when class test starts.
            Set up every necessary procedure here
        """
        print('\n------------TEST SUITE START-------------\n')

    @classmethod
    def tearDownClass(cls):
        """ Runs after the class test ends
            This is for cleaning up
        """
        print('\n------------TEST SUITE ENDS-------------\n')

    def setUp(self):
        # flask-specific acquiring of test client
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_create_blog(self):
        body = {"_id": 3,
                "title": "my new blog",
                "content": "a new blog I created"}
        res = self.client.post("/blog", json=body)
        self.assertEqual(res.json, body)

    def test_get_all_blogs(self):
        res = self.client.get("/blog")
        self.assertEqual(res.json, server_data)

    def test_get_blog(self):
        blog_id = 1
        res = self.client.get(f"blog/{blog_id}")
        expected = [blog for blog in server_data if blog.get("_id") == blog_id]
        self.assertEqual(res.json, expected)

    def test_update_blog(self):
        blog_id = 1
        body = {"_id": 1,
                "title": "updated blog",
                "content": "I updated my very first blog"}
        res = self.client.put(f"/blog/{blog_id}", json=body)
        self.assertEqual(res.json, body)


    def test_delete_blog(self):
        blog_id = 1
        res = self.client.delete(f"/blog/{blog_id}")
        expected = [blog for blog in server_data if blog.get("_id") == blog_id]
        self.assertEqual(res.json, expected)

    def test_get_blog_wrong_id(self):
        blog_id = 0
        res = self.client.get(f"blog/{blog_id}")
        expected = {"errors": "not found"}
        self.assertEqual(res.json, expected)

    def test_update_blog_wrong_id(self):
        blog_id = 0
        body = {"_id": 1,
                "title": "updated blog",
                "content": "I updated my very first blog"}
        res = self.client.put(f"blog/{blog_id}", json=body)
        expected = {"errors": "not found"}
        self.assertEqual(res.json, expected)

    def test_delete_blog_wrong_id(self):
        blog_id = 0
        res = self.client.delete(f"/blog/{blog_id}")
        expected = {"errors": "not found"}
        self.assertEqual(res.json, expected)