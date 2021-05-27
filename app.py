from flask import Flask, request, jsonify

from models.model import autocomplete, search

app = Flask(__name__)

@app.route('/api/branches/autocomplete')
def autocomplete_api():
    """Autocomplete API to fetch possible matches on branch name.

    Args:
        q: The branch to be retrieved.
        limit: The limit of results.
        offset: The offset of results.

    Returns: JSON serialized response.

    Raises:
        Message: Internal Server Error
    """
    q = request.args.get("q")
    limit = request.args.get("limit")
    offset = request.args.get("offset")
    response = autocomplete(q,limit,offset)
    return jsonify(response)

@app.route('/api/branches')    
def search_api():
    """Search API to search a word/term across the databse.

    Args:
        q: The term or word to be searched.
        limit: The limit of query results.
        offset: The offset of query results.

    Returns: JSON serialized response.

    Raises:
        Message: Internal Server Error
    """
    q = request.args.get("q")
    limit = request.args.get("limit")
    offset = request.args.get("offset")
    response = search(q,limit,offset)
    return jsonify(response)

@app.route('/')
def index():
    return "<h1>Indian Banks API !!</h1>"

@app.errorhandler(404)
def not_found(e):
    response = {"Message":"Malformed Url"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)