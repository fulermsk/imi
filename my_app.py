from pyfladesk import init_gui
from flask import render_template, Flask
from flask_wtf import FlaskForm
from wtforms import BooleanField


class LoginForm(FlaskForm):
    checkbox1 = BooleanField('checkbox1')
    checkbox2 = BooleanField('checkbox2')


class Config(object):
    SECRET_KEY = 'asd12u39whkdjshfoiauwy3hrqkwefndslzngag1q'


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    init_gui(app)
