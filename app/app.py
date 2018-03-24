import flask
app = flask.Flask(__name__)

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyRegressor
from sklearn.datasets import make_regression


#----------- Model goes here ----------#
def the_model2(V):
    df = pd.read_csv('')
    features = ['X1', 'X2']
    target = []

    X = df[features]
    y = df[target]

    model = RandomForestClassifier(n_estimators=100).fit(X, y)
    
    return model

def transform_input(*items):
    X, y = make_regression(n_samples=1, n_features=2)
    return X

def the_mocked_model():
    
    X, y = make_regression(n_samples=500, n_features=2)
    model = DummyRegressor()
    model.fit(X, y)

    return model

PREDICTOR = the_mocked_model()

#-------- ROUTES GO HERE -----------#
@app.route('/')
def page():
   with open("templates/home.html", 'r') as viz_file:
       return viz_file.read()


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':
        #import ipdb;ipdb.set_trace()
        post_code = flask.request.form['post_code']
        n_rooms = flask.request.form['n_rooms']

        items = transform_input(post_code, n_rooms)
        predicted_price = PREDICTOR.predict(items)
        results = {'predicted_rental_income': list(predicted_price)[0] }
        return flask.jsonify(results)


if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = 4000

    app.run(HOST, PORT, debug=True)
