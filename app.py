from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/no-discordo')
def no_discordo():
    return render_template('no-discordo.html')


@app.route('/bob', methods=['GET', 'POST'])
def bob():
    if request.method == 'POST':
        return 'Bob is here'
    return render_template('bob.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

