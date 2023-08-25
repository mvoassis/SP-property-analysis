from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

modelo = pickle.load(open('models/GB_model.pkl', 'rb'))

app = Flask(__name__)
CORS(app, origins=["http://localhost", "https://docs.ufpr.br"])


@app.route('/')
def home():
    return "Minha primeira API."

@app.route('/teste/<frase>')
def teste(frase):

    return "frase: {}".format(frase)

@app.route('/price/', methods=['POST'])
def price():
    data = request.get_json()
    # data = {'Metragem': 660,
    #         'latitude': -23.50447648908102,
    #         'longitude': -46.645119902668576,
    #         'Quartos': 4,
    #         'Banheiros': 7,
    #         'Vagas': 12,
    #         'V005': 6078.73,
    #         'V007': 6997.1,
    #         'V009': 2829.04,
    #         'V011': 4501.11}
    X = pd.DataFrame(
        columns=['Metragem', 'Quartos', 'Banheiros', 'Vagas', 'latitude', 'longitude', 'V005', 'V007', 'V009', 'V011'])
    X.loc[0] = data

    predict = modelo.predict(X)

    return f"Predicted Value: R$ {predict[0]:.2f}"


app.run(host='0.0.0.0', port=5000)
