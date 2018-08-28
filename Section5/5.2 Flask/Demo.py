from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, StringField


app = Flask(__name__)


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
            flash('Hello ' + name)
            flash('-----------')
            flash('Recieved an order for: ' + order)

        elif request.form['submit'] == 'FAQ':
            return faq()

        else:
            flash('All the form fields are required. ')

    return render_template('hello_stylized.html', form=form)
    # return render_template('hello.html', form=form)


@app.route("/FAQ", methods=['GET'])
def faq():
    return render_template('FAQ.html')
# ctrl shift R

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run()