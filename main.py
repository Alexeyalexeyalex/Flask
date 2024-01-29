from flask import Flask, request, make_response
from flask import render_template, session
# from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'e2b97356e6f9df296f4219739ff40b207b09210da919ea5f79102b2dd23a520a'

@app.route('/')
@app.route('/clothes/', methods=['GET', 'POST'])
def main_window():
    if request.method == 'POST':
        session.pop('userlogin', None)
        session.pop('useremail', None)
    
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


def cookies(user_name, user_email):
    response = make_response("My cookie")
    response.set_cookie('userlogin', user_name)
    response.set_cookie('useremail', user_email)
    return response

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':

        user_name = request.form.get('login')
        user_email = request.form.get('email')

        # cookies(user_name, user_email)
        session['userlogin'] = user_name
        session['useremail'] = user_email

        context = {
            'title': 'Приветствие',
            'login': session['userlogin'],
            'email': session['useremail']
        }


        return render_template('hello.html', **context)



if __name__ == '__main__':
    app.run()