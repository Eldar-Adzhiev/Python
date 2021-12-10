from flask import Flask, request, jsonify

app = Flask(__name__)

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

        salary = int(request.json['salary'])
        name = request.json['name']
        age = request.json['age']

        annualy = str(salary * 12)

        resp_json = {'name': name,
                     'age': age,
                     'annualy': annualy
        }

        return jsonify(resp_json)