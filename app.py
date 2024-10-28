from flask import Flask, request, render_template
from sympy import symbols, Eq, diophantine

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = int(request.form['c'])
    
    x, y = symbols('x y')
    equation = Eq(a * x + b * y, c)
    solutions = diophantine(equation)
    
    formatted_solutions = [f"{sol[0]} * {a} + {sol[1]} * {b} = {c}" for sol in solutions]
    
    return render_template('result.html', solutions=formatted_solutions)

if __name__ == '__main__':
    app.run(debug=True)