
from flask import Flask,render_template,request,flash
import numpy as np
import pandas as pd
import pickle
import csv

app=Flask(__name__)

# load the ML model
pipe=pickle.load(open('model.pkl','rb'))


@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('index.html')


@app.route('/predict',methods=["post"])
def predict():
    area=int(request.form['area'])
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    balcony=int(request.form['balcony'])
    areatype=request.form['areatype']
    # predict price
    inputdata=pd.DataFrame([[areatype,area,bath,balcony,bhk]],columns=['area_type','total_sqft', 'bath','balcony','bhk'])
    prediction=pipe.predict(inputdata)
    prediction=int(round(prediction[0],2))
    
    return render_template('pass.html',n=prediction,area=area,bhk=bhk,bath=bath)
    
if __name__=="__main__":
    
    app.run(debug=True,host='0.0.0.0',port=8080)