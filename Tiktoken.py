from flask import Flask, request, jsonify, abort
from tiktoken import Tokenizer

app = Flask(__name__)
tokenizer = Tokenizer()

SECRET = "Xujf9jgg1z"

@app.route('/count_tokens', methods=['POST'])
def count_tokens():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != SECRET:
        abort(401)  # Unauthorized

    data = request.json
    text = data.get('text', '')
    
    token_count = tokenizer.count_tokens(text)
    return jsonify({"token_count": token_count})

if __name__ == '__main__':
    app.run(debug=True)
