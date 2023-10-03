from flask import Flask, request, jsonify, abort
import tiktoken
import os

app = Flask(__name__)
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

SECRET = "Xujf9jgg1z"

@app.route('/count_tokens', methods=['POST'])
def count_tokens():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != SECRET:
        abort(401)  # Unauthorized
    data = request.json
    text = data.get('text', '')
    token_count = len(enc.encode(text))
    return jsonify({"token_count": token_count})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
