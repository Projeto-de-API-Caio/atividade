# 📘 API de Atividades

Este projeto consiste em uma **API RESTful** desenvolvida com **Flask** e **SQLAlchemy**, responsável por gerenciar atividades relacionadas a disciplinas. É parte de um **ecossistema de microsserviços**, no qual múltiplos serviços se comunicam via requisições HTTP, promovendo escalabilidade e separação de responsabilidades.

---

## 📌 Descrição da API

A API de Atividades expõe endpoints para:

* 📥 **Criar** novas atividades
* 📄 **Listar** todas as atividades existentes
* 🔍 (Suporte previsto) Obter, atualizar e remover atividades específicas

Cada atividade possui os seguintes campos:

* `id_atividade` (int) — Identificador único
* `id_disciplina` (int) — Chave estrangeira que representa a disciplina
* `enunciado` (str) — Texto da pergunta ou exercício
* `resposta` (str) — Resposta correta da atividade

---

## 🐳 Instruções de execução com Docker

### Pré-requisitos

* Docker instalado ([https://www.docker.com/](https://www.docker.com/))

### Passos para execução:

1. **Build da imagem:**

```bash
docker build -t flask-atividades .
```

2. **Execução do container:**

```bash
docker run -d -p 5002:5002 flask-atividades
```

3. A API estará disponível em:
   **[http://localhost:5002/atividades](http://localhost:5002/atividades)**

---

## 🧱 Arquitetura da Aplicação

A arquitetura segue o padrão **MVC simplificado**:

* **`app.py`**: ponto de entrada da aplicação. Inicializa o app e registra os blueprints.
* **`config.py`**: define as configurações da aplicação (banco de dados, debug, etc.).
* **`controllers/atividade_controller.py`**: gerencia as rotas e lógica de negócios da entidade Atividade (não enviado, mas presumido).
* **`SQLAlchemy`**: ORM para interagir com o banco de dados `SQLite`.

A aplicação é stateless e pode ser escalada horizontalmente, pois o estado (atividades) está persistido em banco de dados.

---

## 🧹 Ecossistema de Microsserviços

Este serviço faz parte de um ecossistema maior com os seguintes componentes:

| Serviço             | Porta  | Descrição                       |
| ------------------- | ------ | ------------------------------- |
| `API de Alunos`     | `8000` | Gerencia informações dos alunos |
| `API de Atividades` | `5002` | Gerencia enunciados e respostas |
| `API de Correção`   | `8001` | Corrige atividades submetidas   |

### Integração entre os serviços

* A **API de Atividades** é consumida por outras APIs, como a de correção e alunos.
* A comunicação é feita via HTTP com requisições `GET` e `POST`.
* Exemplo de fluxo:

  1. O aluno responde uma atividade via interface frontend.
  2. A interface envia a resposta para a `API de Correção`.
  3. A `API de Correção` consulta o enunciado e resposta corretos na `API de Atividades`.
  4. O resultado é computado e enviado de volta para a interface.

Este padrão desacoplado permite que cada serviço evolua de forma independente, facilite o versionamento e melhora a escalabilidade da aplicação como um todo.

---

## 💪 Testes

Os testes estão implementados em `testes.py` usando `unittest`:

* Teste de listagem de atividades (`GET /atividades`)
* Teste de criação de nova atividade (`POST /atividades`)

Para executar:

```bash
python testes.py
```

⚠️ Os testes esperam que a API esteja rodando na **porta 8000**. Ajuste se necessário.

---

## 🛆 Dependências

Listadas no `requirements.txt`:

* Flask
* Flask-SQLAlchemy
* flask-restx
* requests
* SQLAlchemy

---
