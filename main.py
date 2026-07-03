from flask import Flask

app = Flask(__name__)

@app.route("/")
def Pagina():
    return "<h1>Minha primeira página com o Flask</h1>"

@app.route("/secret")
def Secret():
    return "Essa página é secreta!"

if __name__ == "__main__":
    app.run(debug=True)