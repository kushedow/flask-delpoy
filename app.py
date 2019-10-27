from flask import *
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()