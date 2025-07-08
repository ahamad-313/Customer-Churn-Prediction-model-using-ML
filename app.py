from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

# Load the trained model
model_path = 'model.pkl'  # Update this with the actual model filename
model = joblib.load(model_path)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form inputs
    features = [
        int(request.form['creditScore']),
        int(request.form['age']),
        int(request.form['tenure']),
        float(request.form['balance']),
        int(request.form['numOfProducts']),
        int(request.form['hasCrCard']),
        int(request.form['isActiveMember']),
        float(request.form['estimatedSalary']),
        int(request.form['exited']),
        1 if request.form['geography'] == 'Germany' else 0,  # Geography_Germany
        1 if request.form['gender'] == 'Male' else 0         # Gender_Male
    ]
    final_features = [np.array(features)]
    
    # Make prediction
    prediction = model.predict(final_features)
    output = 'Likely to Churn' if prediction[0] == 1 else 'Not Likely to Churn'

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
