
#Build an "__API__" to take data from the user and pass this data to the model for prediction and finally display the predicted value
from flask import Flask,render_template,request,flash
import numpy as np
import pandas as pd
import pickle
import csv

# create app in flash
app=Flask(__name__)

# load the ML model
pipe=pickle.load(open('model.pkl','rb'))


@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('index.html')


# when user click on submit button after fill the form then submit button hit the url=http://127.0.0.1:11111/predict
@app.route('/predict',methods=["post"])
def predict():
    # data come from HTML form
    area=int(request.form['area'])
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    balcony=int(request.form['balcony'])
    areatype=request.form['areatype']
    # predict price
    inputdata=pd.DataFrame([[areatype,area,bath,balcony,bhk]],columns=['area_type','total_sqft', 'bath','balcony','bhk'])
    prediction=pipe.predict(inputdata)
    prediction=int(round(prediction[0],2))
    
    # render the predicted price on pass.html file
    return render_template('pass.html',n=prediction,area=area,bhk=bhk,bath=bath)
    
# finally run this app on port=8080
if __name__=="__main__":
    debug=True
    app.run(host='0.0.0.0',port=8080)