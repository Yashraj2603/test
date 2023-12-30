from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post_data', methods=['POST'])
def post_data():
    try:
        data = request.get_json()
        print("Data:", data)

        if isinstance(data, int):
            response = {"result": data * data}
            return jsonify(response)
        else:
            error_response = {"error": "Input is not an integer"}
            return jsonify(error_response), 400

    except Exception as e:
        error_response = {"error": 'Internal Server Error'}
        return jsonify(error_response), 500

if __name__ == "__main__":
    app.run(debug=True)
