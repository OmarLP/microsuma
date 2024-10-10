from flask import Flask, request, render_template

app = Flask(__name__)

# Ruta para mostrar el formulario HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario y mostrar el resultado
@app.route('/sum', methods=['POST'])
def sum_numbers():
    try:
        # Obtener los números enviados por el formulario
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])

        # Sumar los números
        result = num1 + num2

        # Renderizar el resultado en la misma página
        return render_template('index.html', num1=num1, num2=num2, result=result)

    except ValueError:
        return render_template('index.html', error="Por favor ingresa números válidos.")

if __name__ == '__main__':
    app.run(debug=True)