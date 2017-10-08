#app.py 
from flask import *
from flask_wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from proteinScraper import *
from models import *
import pandas as pd 


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'enable-form';


det1 = Determinant(1, "PB2", 627, high='K', low='E')
det2 = Determinant(1, "PB2", 701, high='N', low='D')
det3 = Determinant(2, "PB1-F2", 66, high='S', low='N')
det4 = Determinant(6, "NA", 274, high='Y', low='H')
det5 = Determinant(8, "NS1", 92, high='E', low='D')

DETERMINANTS = [det1, det2, det3, det4, det5] # Order matters


@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html')


@app.route('/inputStrains', methods = ['GET'])
def input_strains():
    return render_template('inputStrains.html')


@app.route('/cross', methods = ['GET', 'POST'])
def cross():
    strain_1 = request.form['strain-1']
    strain_2 = request.form['strain-2']
#    strn1 = Strain(strain_1, DETERMINANTS)
#    strn2 = Strain(strain_2, DETERMINANTS)
#    patho1 = strn1.pathogenicity
#    patho2 = strn2.pathogenicity
#    cross = CrossData(strn1, strn2, DETERMINANTS)
#    data = cross.data
#    return render_template('cross.html', result1=strain_1, result2=strain_2,
                            patho1=patho1, patho2=patho2, data=data)
    return render_template('cross.html', result1=strain_1, result2=strain_2)


if __name__ == "__main__":
    app.run(debug=True)
