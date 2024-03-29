import os
from flask import Flask, render_template
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
app = None

def create_app():
	app = Flask(__name__,template_folder = "templates",static_url_path = '/static',static_folder = 'static')
	app.secret_key="key"
	if os.getenv('ENV',"development") == "production":
		raise Exception("Currently no production config is setup. ")
	else:
		print("Starting local development")
		app.config.from_object(LocalDevelopmentConfig)
	db.init_app(app)
	app.app_context().push()
	return app

app=create_app()

from application.controllers import *
if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		debug=True,
		port=8080
		)