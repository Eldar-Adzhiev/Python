# API  котора вставляет данные в  DB
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)
conn = []
@app.route('/db_save', methods=['GET', 'POST'])
def db_save():

    user_name = request.args.get('name')
    city = request.args.get('city')

    if conn:
        print('CONN ===========')

        base_data = (user_name, city)
        p_query = """INSERT INTO public.Person (person_name, city_id) VALUES (%s, %s) """
        cursor.execute(p_query, base_data)

        conn.commit()

        return 'User saved'
    else:
        return 'User does not save'




# SELECT

@app.route('/user_cities', methods=['GET', 'POST'])
def user_cities():

    result = {}

    if conn:
        sl = cursor.execute("selest * from public.Person;")
        sll = cursor.fetcha()

        for i in sll:
            result[str(i[0])] = {'User': i[1], "City":i[2]}
            result['id'] = i[0]
            print(i[0], i[i])
        cursor.close

        return jsonify(result)
    else:
        return "Connection error"

    return jsonify(result)