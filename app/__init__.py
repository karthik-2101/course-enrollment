from flask import Flask
from config import Config
from app.database import db, ma
from app.routers import main_bp
# from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    # migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)  

    return app