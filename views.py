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
    strn1 = Strain(strain_1, DETERMINANTS)
    strn2 = Strain(strain_2, DETERMINANTS)
    patho1 = strn1.pathogenicity
    patho2 = strn2.pathogenicity
    cross = CrossData(strn1, strn2, DETERMINANTS)
    data = cross.data
    rea11 = str(data["reassortants1"][0])
    rea12 = str(data["reassortants1"][1])
    rea13 = str(data["reassortants1"][2])
    rea21 = str(data["reassortants2"][0])
    rea22 = str(data["reassortants2"][1])
    rea23 = str(data["reassortants2"][2])
    rea31 = str(data["reassortants3"][0])
    rea32 = str(data["reassortants3"][1])
    rea33 = str(data["reassortants3"][2])
    rep11 = str(data["representation1"]["nulls"])
    rep12 = str(data["representation1"]["lows"])
    rep13 = str(data["representation1"]["highs"])
    rep21 = str(data["representation2"]["nulls"])
    rep22 = str(data["representation2"]["lows"])
    rep23 = str(data["representation2"]["highs"])

    return render_template('cross.html', result1=strain_1, result2=strain_2,
                            rea11=rea11, rea12=rea12, rea13=rea13,
                            rea21=rea21, rea22=rea22, rea23=rea23,
                            rea31=rea31, rea32=rea32, rea33=rea33,
                            rep11=rep11, rep12=rep12, rep13=rep13,
                            rep21=rep21, rep22=rep22, rep23=rep23,
                            rep31=rep31, rep32=rep32, rep33=rep33)


if __name__ == "__main__":
    app.run(debug=True)
