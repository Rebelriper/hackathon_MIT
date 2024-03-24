from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

# Load the model from the pickle file
with open('crop_recommendation_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the dataset
df = pd.read_csv('merged')

# Drop rows with NaN values in the crop column
df = df.dropna(subset=['Crop'])

# Assuming X contains soil NPK values and y contains crop names
X = df[['N', 'P', 'K']]
y = df['Crop']

# Train a KNN model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X, y)

# Define the API endpoint for crop recommendation
@app.route('/recommend_crop', methods=['POST'])
def recommend_crop():
    # Get the NPK values from the request
    npk_values = request.json.get('npk_values')

    # If there is a NaN value, return an error message
    if any(pd.isnull(npk_values)):
        return jsonify({'error': 'No crop recommendations available for this input'})

    # Make the prediction using the loaded model
    prediction = model.predict([npk_values])[0]

    # If the prediction is 0, return a different message
    if prediction == '0':
        return jsonify({'message': 'No crop recommendations available for this input'})

    return jsonify({'predicted_crop': prediction})

if __name__ == '__main__':
    app.run(debug=True)
