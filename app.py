from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - GabyDias"

if __name__ == '__main__':
    port = os.getenv('PORT', default='5000')
    app.run('0.0.0.0', port=port)