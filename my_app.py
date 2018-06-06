from pyfladesk import init_gui
from flask import render_template, Flask, request
from flask_wtf import FlaskForm
from wtforms import BooleanField
import json


class LoginForm(FlaskForm):
    checkbox1 = BooleanField('checkbox1')
    checkbox2 = BooleanField('checkbox2')


class Config(object):
    SECRET_KEY = 'asd12u39whkdjshfoiauwy3hrqkwefndslzngag1q'


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', data=[1,0,1,0,1,0])
    else:
        print(request.get_json())
        return render_template('index2.html', data=request.get_json()['data'])


if __name__ == '__main__':
    init_gui(app)
    
