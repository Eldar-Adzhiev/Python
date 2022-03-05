from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/first')
def first():
    return 'Hello!!!!!!!!!!!!!'