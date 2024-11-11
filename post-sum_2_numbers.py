from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_sum_2', methods=['POST'])
def post_sum_2():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify(message="Please provide both num1 and num2"), 400

    result = num1 + num2
    return jsonify(sum=result)

if __name__ == '__main__':
    app.run(debug=True)
