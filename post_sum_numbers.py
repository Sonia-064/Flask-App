from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_sum_n', methods=['POST'])
def post_sum_n():
    data = request.get_json()
    numbers = data.get('numbers')

    if not numbers or not isinstance(numbers, list):
        return jsonify(message="Please provide a list of numbers"), 400

    result = sum(numbers)
    return jsonify(sum=result)

if __name__ == '__main__':
    app.run(debug=True)
