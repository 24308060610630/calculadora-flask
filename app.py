from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    mensaje += "<h1>¡hola mundo!<h1>"
    
    mensaje += "<h2>para poder </h2>"
    mensaje += "<ol>"
    mensaje += "<li><h2> Suma http://127.0.0.1:5000/suma/10/20/</h2></li>"
    mensaje += "<li><h2> Resta http://127.0.0.1:5000/resta/10/20/</h2></li>"
    mensaje += "<li><h2> Division http://127.0.0.1:5000/division/10/20/</h2></li>"
    mensaje += "<li><h2>Multiplicar http://127.0.0.1:5000/multiplicar/10/20/</h2></li>"
    mensaje += "<li><h2>Maximo http://127.0.0.1:5000/maximo/10/20/</h2></li>"
    mensaje += "<li><h2>Minimo http://127.0.0.1:5000/minimo/10/20/</h2></li>"
    mensaje += "</ol>"
    return mensaje

@app.route('/suma/<v1><v2>')
def suma():
    s = str(float(v1) + float(v2))
    mensaje = f"<h1>la suma de {v1} + {v2} es {s} </h1>"
    return mensaje

if __name__ == "__main__":
    app.run(debug=True)
