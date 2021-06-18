from logging import exception
from flask import Flask, render_template, request, jsonify
from functools import reduce
import math 

app = Flask(__name__)

@app.route('/get_max_num', methods=['POST', 'GET'])
def get_max_num():
    try:
        if (request.method == 'POST'):
            lst = request.json['lst']
            return jsonify (reduce(lambda a, b: a if a > b else b, lst))
        else:
            return jsonify("Only 'POST' method is allowed for this request")
    except Exception as e :
        return jsonify (e)

@app.route('/get_prime_num', methods = ['GET', 'POST'])
def get_prime_num():
    try:
        if (request.method == 'GET'):
            num = request.json['num']
            for i in range (2,num):
                if num%i==0:
                    return jsonify (f"Nope, '{num}' is not a prime number")
                    break
                else:
                    return jsonify (f"yup, '{num}' is a prime number")
        else:
            return jsonify ("Only 'GET' method is allowed for this request")
    except ValueError :
        return jsonify ('Program only accepts the numerical values')
    except exception as e :
        return jsonify (e)

@app.route('/find_vol', methods = ['GET', 'POST'])
def get_vol():
    try:
        if (request.method == 'GET'):
            dia = request.json['dia']
            radius = dia/2
            voluume = (4/3)*(math.pi)*radius
            return jsonify (f'Volume is {round(voluume,2)}')     
        else:
            return jsonify ("Only 'GET' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/reverse_str', methods = ['GET', 'POST'])
def reverse_str():
    try:
        if (request.method == 'POST'):
            string = request.json['string']
            return jsonify(string[::-1])
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/filter_float', methods = ['GET', 'POST'])
def filter_float():
    try:
        if (request.method == 'POST'):
            lst = request.json['lst']
            return jsonify(list(filter(lambda a:a if type(a)==float else 0 , lst)))
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/find_tri_area', methods = ['GET', 'POST'])
def calculate_area():
    try:
        if (request.method == 'POST'):
            a = float(request.json['a'])
            b = float(request.json['b'])
            c = float(request.json['c'])
            s = (a+b+c)/2
            return jsonify((s*(s-a)*(s-b)*(s-c)) ** 0.5)
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/filter_long_words', methods = ['GET', 'POST'])
def filter_long_words():
    try:
        if (request.method == 'POST'):
            lst = request.json['lst']
            max_len = request.json['max_len']
            return jsonify([i for i in lst if  len(i) > max_len])
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/word_to_int', methods = ['GET', 'POST'])
def word_to_int():
    try:
        if (request.method == 'POST'):
            lst = request.json['lst']
            return jsonify([len(word) for word in lst])
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/str_to_words', methods = ['GET', 'POST'])
def str_to_words():
    try:
        if (request.method == 'POST'):
            string = request.json['string']
            return jsonify(string.split())
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/get_upper', methods = ['GET', 'POST'])
def get_upper():
    try:
        if (request.method == 'POST'):
            string = request.json['string']
            return jsonify(string.upper())
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/get_vowels', methods = ['GET', 'POST'])
def get_vowels():
    try:
        if (request.method == 'POST'):
            letters_of_alphabet = request.json['letters_of_alphabet']
            return jsonify(list(map(lambda letter : True if letter.upper() in ['A', 'E', 'I', 'O', 'U'] else False , letters_of_alphabet)))
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)

@app.route('/euclidean_distance', methods = ['GET', 'POST'])
def get_distance():
    try:
        if (request.method == 'POST'):
            x_axis = request.json['x_points']
            y_axis = request.json['y_points']
            return jsonify(math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(x_axis, y_axis))))
        else:
            return jsonify ("Only 'POST' method is allowed for this request")
    except exception as e :
        return jsonify (e)


if __name__ == "__main__" :
    app.run()