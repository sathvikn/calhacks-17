#app.py 
from flask import *
from proteinScraper import *

import pandas as pd 


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
