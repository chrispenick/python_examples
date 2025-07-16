from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Load the trained model
with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

# You may want to save the columns used for one-hot encoding during training
# For simplicity, let's assume you know the possible values for homeworld and unit_type
# Or you can load them from your training data if available

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>SWAPI Troop Movement Predictor</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Expecting: {"homeworld": "Naboo", "unit_type": "x-wing"}
    input_df = pd.DataFrame([{
        "homeworld": data.get("homeworld", ""),
        "unit_type": data.get("unit_type", "")
    }])
    # One-hot encode as in training
    input_encoded = pd.get_dummies(input_df)
    # Align columns with model (fill missing columns with 0)
    # You may want to save the columns from training as a list, e.g. model_columns
    # For demo, let's fit to model's expected columns if available
    try:
        model_columns = model.feature_names_in_
        input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)
    except AttributeError:
        # If feature_names_in_ is not available, just use input_encoded as is
        pass
    prediction = model.predict(input_encoded)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)