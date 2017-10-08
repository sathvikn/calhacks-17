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

class StrainForm(Form):
    strain = StringField('strain', validators=[DataRequired()])

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/inputStrains', methods = ['GET'])
def input_strains():
    first_strain = StrainForm()
    second_strain = StrainForm()
    if first_strain.validate_on_submit():
        results = first_strain.strain.data
        return render_template('seqDetail.html', results=results)

    return render_template('inputStrains.html', strain_1 = first_strain, strain_2 = second_strain)

@app.route('/seqDetail', methods = ['GET', 'POST'])
def seq_detail():
    strain_name = request.form['strain']
    return render_template('seqDetail.html', results=strain_name)


if __name__ == "__main__":
    app.run(debug=True)
