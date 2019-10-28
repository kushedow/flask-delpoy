from flask import *
app = Flask(__name__)
app.config['DEBUG'] = True
import data as cfg

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()