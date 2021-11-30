from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import time

app = Flask(__name__)

clf=pickle.load(open('mine.sav','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/detect',methods=['POST','GET'])

def predict():
    
    int_features=request.form["u_data"]
    testing = int_features 
    arr = [float(x) for x in testing.split('\t')]
    
    prediction=clf.predict([arr])
    if prediction == 1:
      predd = clf.predict_proba([arr])[:,1]
      print(predd*100)
    else:
      predd = clf.predict_proba([arr])[:,0]

    time.sleep(3)
    
   
    if prediction == 1:
        return render_template('index.html',pred='Mine',probp = predd*100)
    if prediction == 0:
        return render_template('index.html',red='Rock',probn = predd*100)



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port="33")

