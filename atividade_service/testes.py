import requests
import unittest


class TestStringMethods(unittest.TestCase): 
    
    def test_001_get_alunos(self):
        
        r = requests.get('http://localhost:8000/atividades/')
        self.assertEqual(r.status_code, 200)
        atividade = r.json()
        self.assertIsInstance(atividade, list)
        print("1 OK")

    def test_002(self):
       # cria aluno novo com dados válidos
        atv_data = {
                     "id_disciplina": "1",
                     "enunciado":"Quanto é 2+2",
                     "resposta":"4",
                     }
        r = requests.post('http://localhost:8000/atividades/', json=atv_data)
        self.assertEqual(r.status_code, 200)
        atividade = r.json()
        id_atividade = r.json()['id_atividade']
        self.assertEqual(atividade['id_atividade'], id_atividade)
        
        print("2 OK")

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)



if __name__ == '__main__':
    unittest.main()