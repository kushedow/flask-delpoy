from flask import *
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return undefined




if __name__ == '__main__':
    app.run()