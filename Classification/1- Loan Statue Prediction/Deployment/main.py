from flask import Flask, render_template,send_from_directory,request
from AICode import predict
import joblib
 
app = Flask(__name__,static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/images/<path:path>')
def send_ddd(path):
    return send_from_directory('images', path)


@app.route('/vendor/<path:path>')
def send_ssds(path):
    return send_from_directory('vendor', path)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/data',methods = ['GET', 'POST'])
def helloff():
    if request.method == 'GET':
        return "opps"
      
    if request.method == 'POST':
       
        data = request.form # a multidict containing POST data
       
        d1 = dict(data) 
        if d1['Credit_History'] == "on" :
            d1['Credit_History'] = 0 
        else :
            d1['Credit_History'] = 1 


        if d1['Gender'] == "Male" :
            d1['Gender'] = 1 
        else :
            d1['Gender'] = 0



        l_data = list(d1.values())
        x = predict(l_data)
        return render_template('prediction.html',text=x)



# ImmutableMultiDict([('IncomeofApplicant', '222'), ('IncomeofCo-Applicant', '22225'), ('LoanAmount', '525252'), ('Loan_Amount_Term', '88'), ('Credit_History', 'on'), ('Gender', 'Male')])

#export FLASK_APP=app.py
#export FLASK_ENV=development
#flask run