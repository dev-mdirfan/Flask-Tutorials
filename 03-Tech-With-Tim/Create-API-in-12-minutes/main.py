from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Home"

@app.route('/get-user/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@gmail.com"
    }
    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra
    return jsonify(user_data), 200 # 200 is the status code (OK or success)


@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify(data), 201 # 201 is the status code (created)


if __name__ == '__main__':
    app.run(debug=True)