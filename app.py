from distutils.log import debug
from flask import Flask, render_template, request,jsonify
from helper import transform_features
import pandas as pd
import joblib

app = Flask(__name__)
app.debug = True
model = joblib.load('models/model.h5')
scaler = joblib.load('models/scaler.h5')



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def req(requests):
    x=['location', 'Bedrooms', 'Bathrooms', 'Area (m²)', 'Type', 'Payment Option', 'Compound', 'Delivery Term', 'Furnished', 'Delivery Date', 'meter_price', 'Parking', 'Landline', 'A/C', 'Gas', 'Security', 'Water', 'Elevator', 'Pool', 'Pets', 'Kitchen', 'Maids', 'Electricity', 'Garden', 'Balcony']
    x2={i:0.0 for i  in x}
    for k,v in requests.items():
        if k in['meter_price','Parking','Landline','A/C','Gas','Security','Water','Elevator','Pool','Pets','Kitchen','Maids''Electricity','Garden','Balcony','Bedrooms','Bathrooms','Area (m²)']:
            x2[k]=int(v)
        else:
            x2[k]=v
    return x2
    
@app.route('/predict', methods=['POST'])
def predict():
    df=transform_features(pd.DataFrame([req(request.form)]))
    client = scaler.transform(df)
    prediction = model.predict(client)[0]
    return {"price":prediction,
            "RMSA":"105105.02644692342"}

if __name__ == "__main__":  
    app.run(debug=True)
