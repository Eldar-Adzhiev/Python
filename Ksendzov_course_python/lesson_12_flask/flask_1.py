# Terminal
# pip3 install virtualenv - Установка витуального окружения
# virtualenv venv - Создание папки окружегия
# source venv/scripts/activate  - Активация окружения
# pip3 freeze -l - Посмотреть установленные библиотеки
# pip list
# pip3 install Flask - Установить библиотеку Flask
# export FLASK_APP=filename.py
# flask run --host='0.0.0.0' --port="5003"

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/first')
def first():
    return 'Hello!!!!!!'