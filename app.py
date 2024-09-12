from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/experiencia')
def experiencia_profissional():
    return render_template('experienciaProfissional.html')

@app.route('/sobre')
def sobre_mim():
    return render_template('sobreMim.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
