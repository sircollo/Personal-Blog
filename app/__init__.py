from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(confi_name):
  app = Flask(__name__)

  app.config.from_object(config_options[confi_name])
  
  
  bootstrap.init_app(app)
  
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)
  
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  
  return app
