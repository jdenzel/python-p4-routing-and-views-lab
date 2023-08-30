#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    count=''
    for number in range(0, parameter):
        count += f"{number}\n"
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        add = (num1 + num2)
        return str(add)
    elif operation == '-':
        subtract = num1-num2
        return str(subtract)
    elif operation == '*':
        multiply = num1*num2
        return str(multiply)
    elif operation == 'div':
        divide = num1/num2
        return str(divide)
    else:
        mod = num1%num2
        return str(mod)






        