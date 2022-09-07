import joblib

def predict(data):
    
    model = joblib.load('model.h5')
    scaler = joblib.load('scaler.h5')

    x = ['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History_1.0','Gender_Male']


    result = model.predict(scaler.transform([data]))
    result[0]

    if result[0] == 0 :
        return "Sorry, your loan application has been rejected"
    else :
        return "Your loan application has been accepted"
    

#git add .
#git commit -m "finshed code"
#git push