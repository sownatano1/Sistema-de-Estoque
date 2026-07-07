from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def Dashboard():
    return render_template('index.html')

@app.route("/produtos")
def Produtos():
    return render_template('produtos.html')

if __name__ == "__main__":
    app.run(debug=True)