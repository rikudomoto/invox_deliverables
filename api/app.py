from flask import Flask
from common.database import init_db
from flask_restful import Api
from backend.invox import InvoxAPI

def create_app():
  app = Flask(__name__)
  app.config.from_object('config.Config')

  init_db(app)

  api = Api(app)
  api.add_resource(InvoxAPI, '/invox')

  return app

app = create_app()

