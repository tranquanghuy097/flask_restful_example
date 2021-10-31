from flask import Flask
from views.blueprint import api_bp

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(api_bp)

    from shared import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    return app