from flask import Flask, jsonify, request
from flask.helpers import make_response
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})
api = Api(app)

class PremiumPaymentGateway(Resource):
  def get(self):
    return jsonify(message="GET invoked", category="SUCCESS", status=200)

class ExpensivePaymentGateway(Resource):
  def get(self):
    return jsonify(message="GET invoked", category="SUCCESS", status=200)

class CheapPaymentGateway(Resource):
  def get(self):
    return jsonify(message="GET invoked", category="SUCCESS", status=200)


api.add_resource(PremiumPaymentGateway, '/premiumpayment')
api.add_resource(ExpensivePaymentGateway, '/expensivepayment')
api.add_resource(CheapPaymentGateway, '/cheappayment')


if(__name__ == '__main__'):
  app.run()
  pass
