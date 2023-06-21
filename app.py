from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paint', methods=['POST'])
def paint():
    x = request.form.get('x')
    y = request.form.get('y')
    color = request.form.get('color')
    # Aquí puedes agregar la lógica para pintar en la pantalla
    # Puedes guardar las coordenadas (x, y) y el color en una base de datos o en una lista

    return 'Pintado en coordenadas ({}, {}) con el color {}'.format(x, y, color)

if __name__ == '__main__':
    app.run()
