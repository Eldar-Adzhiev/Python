from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/first')
def first():
    return 'Hello!!!!!!!!!!!!!'


@app.route('/user_info', methods=['GET', 'POST'])
def user_info():

    if request.method == 'GET':
        name = 'Eldar'
        age = str(28)

        user_name = request.args.get('name')
        user_age = request.args.get('age')

        print("user_name=", user_name)

        user_list = [user_name, user_age]

        return jsonify(user_list)

    elif request.method == 'POST':

        salary = int(request.form.get('salary'))

        annualy = str(salary * 12)

        resp_str = 'Annualy salary = ' + annualy

        return resp_str