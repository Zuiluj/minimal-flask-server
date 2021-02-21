from flask import Flask
from flask import request, jsonify
app = Flask('simple_server')

data = [
    {
        "_id": 1,
        "title": "initial blog",
        "content": "my very first blog"
    },
    {
        "_id": 2,
        "title": "second blog",
        "content": "my second blog"
    }
]


@app.route('/blog', methods=['POST'])
def create_blog():
    return jsonify(request.json)


@app.route('/blog', methods=['GET'])
def get_all_blogs():
    return jsonify(data)


@app.route('/blog/<int:_id>', methods=['GET'])
def get_one_blog(_id):
    blog = [blog for blog in data if blog.get("_id") == _id]
    if not blog:
        return {
            'errors': 'not found'
        }
    return jsonify(blog)


@app.route('/blog/<int:_id>', methods=['PUT'])
def update_one_blog(_id):
    blog = [blog for blog in data if blog.get("_id") == _id]
    if not blog:
        return {
            'errors': 'not found'
        }
    return jsonify(request.json)


@app.route('/blog/<int:_id>', methods=['DELETE'])
def delete_a_blog(_id):
    blog = [blog for blog in data if blog.get("_id") == _id]
    if not blog:
        return {
            'errors': 'not found'
        }
    return jsonify(blog)