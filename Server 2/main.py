import pickle
from flask import Flask
from flask import request,jsonify
app=Flask(__name__)

#Loading Model
with open('plant_detect.pkl','rb') as f:
    model=pickle.load(f)



@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    prediction=model.predict(data)
    return jsonify({'prediction':prediction.tolist()})

@app.route('/')
def welcome():
    return "Successful"


if __name__=='__main__':
    app.run(debug=True)
