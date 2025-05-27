from config import db

class Atividade(db.Model):
    __tablename__='atividade'
    id_atividade = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(200), nullable=False)
    respostas = db.Column(db.String(100), nullable=False)

    def __init__(self, id_disciplina, enunciado, respostas):
        self.id_disciplina = id_disciplina
        self.enunciado = enunciado
        self.respostas = respostas

    def to_dict(self):
        return {
            'id_atividade': self.id_atividade,
            'id_disciplina': self.id_disciplina,
            'enunciado': self.enunciado,
            'respostas': self.respostas,
                }
        



class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    atividades = Atividade.query.all()
    return [a.to_dict() for a in atividades]

def obter_atividade(id_atividade):
    atividade = Atividade.query.filter_by(id_atividade=id_atividade).first()
    if not atividade:
        raise AtividadeNotFound
    return atividade.to_dict()

def criarAtividade(dados):
    
    try:
        id_disciplina = dados['id_disciplina']
        enunciado = dados['enunciado']
        resposta = dados['resposta']
        
        atividade = Atividade(id_disciplina, enunciado, resposta)
        
        if atividade:
            
            print(atividade)
            
            db.session.add(atividade)
            db.session.commit()

            return atividade.to_dict(), 200
        
        
    except KeyError as e:
        return {"erro": "Atividade não criada"}, 400
        
