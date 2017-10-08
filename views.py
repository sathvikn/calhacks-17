#app.py 
from flask import *
from flask_wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from proteinScraper import *
import pandas as pd 


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'enable-form';

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/inputStrains', methods = ['GET'])
def input_strains():
    return render_template('inputStrains.html')

@app.route('/seqDetail', methods = ['GET', 'POST'])
def seq_detail():
    print("called")
    strain = request.form['strain']
    return render_template('seqDetail.html', results = strain)

@app.route('/crossed', methods = ['GET', 'POST'])
def cross():
    strain_1 = request.form['strain-1']
    strain_2 = request.form['strain-2']
    return render_template('crossed.html', result1 = strain_1, result2 = strain_2)

if __name__ == "__main__":
    app.run(debug=True)
