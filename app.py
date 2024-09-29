from flask import Flask, request, jsonify
from flask_restful import Api
from sql_alchemy import banco  
from resources.cliente import Cliente, Clientes
from flask_cors import CORS
from flasgger import Swagger
import requests

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

OPENCAGE_API_KEY = '0e51a6e45511417ca30a54aac169e293'

# Inicia o Swagger
swagger = Swagger(app)

# Inicia o banco de dados - chamado banco - com o flask app
banco.init_app(app)

api = Api(app)

# Cria as tabelas no banco de dados
with app.app_context():
    banco.create_all()

# Adiciona a resources para a API
api.add_resource(Clientes, '/clientes')
api.add_resource(Cliente, '/clientes/<string:cliente_id>')

@app.route('/api/getLocation', methods=['POST'])
def get_location():
    data = request.json
    address = data.get('address')
    
    if not address:
        return jsonify({"error": "No address provided"}), 400

    # Make a request to the OpenCage Geocoding API
    geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={OPENCAGE_API_KEY}"
    
    response = requests.get(geocode_url)
    
    if response.status_code == 200:
        geocode_data = response.json()
        if geocode_data['results']:
            location = geocode_data['results'][0]['geometry']
            return jsonify({
                "lat": location['lat'],
                "lng": location['lng']
            })
        else:
            return jsonify({"error": "Location not found"}), 404
    else:
        return jsonify({"error": "Failed to contact geocoding service"}), 500

if __name__ == '__main__':
    app.run(debug=True)

