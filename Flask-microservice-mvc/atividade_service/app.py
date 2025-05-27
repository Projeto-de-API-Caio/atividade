from config import create_app, db
from controllers.atividade_controller import atividade_bp
from flask import Flask


app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app = create_app()
app.register_blueprint(atividade_bp, url_prefix='/atividades')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
