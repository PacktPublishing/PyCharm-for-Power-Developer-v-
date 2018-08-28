from flask import Flask, render_template, flash, request, redirect, url_for, Markup
from wtforms import Form, TextAreaField, StringField
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user
login_manager = LoginManager()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


class MenuOrder(Form):
    name = StringField('Name:')
    order = TextAreaField('Order:')


@app.route("/", methods=['GET', 'POST'])
def submit_order():
    form = MenuOrder(request.form)

    if request.method == 'POST':
        name = request.form['name']
        order = request.form['order']

        if request.form['submit'] == 'Submit Order':
            flash('Recieved an order for: ' + order)

        elif request.form['submit'] == 'FAQ':
            return render_template('FAQ.html')

        elif request.form['submit'] == 'Login':
            return render_template('login.html')

        else:
            flash('All the form fields are required. ')

    return render_template('hello_stylized.html', form=form)


######################################################################################
######################################################################################
######################################################################################

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model):
    __tablename__ = "Customer"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self , username, password):
        self.username = username
        self.password = password
    def __repr__(self):
        return '<User %r>' % self.username
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)


@app.route('/login', methods=['GET','POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        registered_user = User.query.filter_by(username=username, password=password).first()
        if registered_user is None:
            return render_template('Fail.html')

        login_user(registered_user)
        flash('Welcome back!')
        return redirect(request.args.get('next') or url_for('submit_order'))


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()