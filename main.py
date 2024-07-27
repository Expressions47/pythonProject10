from flask import Flask, render_template, request

app = Flask(__name__)

pizzas = [
    {'name': 'Маргарита', 'description': 'Помідори, моцарела, базилік', 'price': 120},
    {'name': 'Салямі', 'description': 'Салямі, моцарела, томатний соус', 'price': 140},
    {'name': 'Чотири сири', 'description': 'Моцарела, горгонзола, пармезан, дорблю', 'price': 130}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)
