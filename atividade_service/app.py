from config import create_app, db
from controllers.atividade_controller import atividade_bp
from flask import Flask

app = create_app()

app.register_blueprint(atividade_bp, url_prefix='/atividades')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
