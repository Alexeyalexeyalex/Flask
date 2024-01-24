from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/clothes/')
def main_window():
    context = {
        'title': 'Главная'
    }
    return render_template('main.html', **context)

@app.route('/footwear/')
def footwear():
    context = {
        'title': 'Обувь'
    }
    return render_template('footwear.html', **context)

@app.route('/jacket/')
def jacket():
    context = {
        'title': 'Куртки'
    }
    return render_template('jacket.html', **context)

if __name__ == '__main__':
    app.run()