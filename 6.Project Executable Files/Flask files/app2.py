from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle


model=pickle.load(open(r'C:\Users\jashwanth\Documents\Fetal_AI\Fetal_AI\fetal_health1.pkl','rb'))
app=Flask('__name__')
@app.route("/")
def home():
    return render_template("index.html")

# ROUTING 
@app.route('/predict',methods=["GET","POST"])
def predict():
     render_template('predict.html')


@app.route("/output",methods=["GET","POST"])
def home():
    prolongued_decelerations = float(request.form['prolongued_decelerations'])
    abnormal_short_term_variability= float(request.form['abnormal_short_term_variability'])
    percentage_of_time_with_abnormal_long_term_variability = float(request.form['percentage_of_time_with_abnormal_long_term_variability'])
    histrogram_variance = float(request.form['histrogram_variance'])
    histrogram_median =float(request.form['histrogram_median'])
    mean_value_of_long_term_variability = float(request.form['mean_value_of_long_term_variability'])
    histrogram_mode = float(request.form['histrogram_mode']) 
    accelerations = float(request.form['accelerations']) 
    x = [[prolongued_decelerations,abnormal_short_term_variability,percentage_of_time_with_abnormal_long_term_variability,]]


    output = model.predict(x)
    out=['NORMAL','PATHOLOGIACL','SUSPECT']
    if int(output[0])==0:
        output='NORMAL'
    elif int(output[0])==1:
        output='PATHOLOGICAL'
    else:
        output='SUSPECT' 

    return render_template('output.html',output=output)  


#MAIN FUNCTION :
if   __name__==  "_main_":
       app.run(debug=True)