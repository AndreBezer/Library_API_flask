```markdown
# API Flask para Gerenciamento de Livros

API simples para CRUD de livros usando Flask e SQLAlchemy

## 🔧 Pré-requisitos
- Python 3.8+
- Pip instalado

## 🛠️ Instalação
```bash
git clone https://github.com/seu-usuario/flask-library-api.git
cd flask-library-api
pip install -r requirements.txt
```

## 🚀 Uso
Inicie o servidor:
```bash
python app.py
```
Acesse: `http://localhost:5000`

## 📍 Endpoints

### Adicionar livro
`POST /api/book/add`
```json
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis"
}
```

### Listar livros
`GET /api/book`

### Buscar livro
`GET /api/book/<id>`

### Atualizar livro
`PUT /api/book/update/<id>`
```json
{
  "titulo": "Novo Título",
  "status": "Lido"
}
```

### Deletar livro
`DELETE /api/book/delete/<id>`

## ⚠️ Importante
- Sempre use `Content-Type: application/json`
- Banco de dados não é versionado

## 📁 Estrutura
```
app.py
requirements.txt
instance/
  library.db
```
