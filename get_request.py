from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_request():
    name = request.args.get('name', 'Guest')
    return jsonify(message=f"Hello, {name}! This is a GET request.")

if __name__ == '__main__':
    app.run(debug=True)
