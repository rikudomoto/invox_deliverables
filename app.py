from flask import Flask
from controller import auth

app = Flask(__name__)
app.register_blueprint(auth.app, url_prefix = '/api')

if __name__ == '__main__':
  app.run(debug = True)