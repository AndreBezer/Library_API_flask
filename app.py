from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'

db = SQLAlchemy(app)


# Configuração do banco de dados
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(30), nullable=True, unique=True)
    autor = db.Column(db.String(30), nullable=True)
    status = db.Column(db.String(8), nullable=True)

#╔══════════════════════════════════════════╗
#║         ROTA PARA ADICIONAR LIVRO        ║
#╚══════════════════════════════════════════╝
@app.route('/api/book/add', methods=['POST'])
def add_book():
    data = request.json

    if 'titulo' in data and 'autor' in data:
        book = Book(titulo=data['titulo'], autor=data['autor'], status=data.get('status', 'Não Lido'))

        db.session.add(book)
        db.session.commit()

        return jsonify({'message' : 'Book added succesfully'})
    return jsonify({'message' : 'Invalid product data'}), 400

#╔═════════════════════════════════════════════════╗
#║         ROTA PARA EXCLUIR UM LIVRO SALVO        ║
#╚═════════════════════════════════════════════════╝
@app.route('/api/book/delete/<int:book_id>', methods=['DELETE'])
def del_book(book_id):
    book = Book.query.get(book_id)

    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message" : "book removed succesfully"})
    
    return jsonify({'message' : 'Book not founded'}), 404

#╔════════════════════════════════════════════╗
#║         ROTA PARA VER O LIVRO SALVO        ║
#╚════════════════════════════════════════════╝
@app.route('/api/book/<int:book_id>', methods=['GET'])
def recuperar_detalhe_individual(book_id):

    # Recuparar informação com base no id
    book = Book.query.get(book_id)
    if book:
        return jsonify({
            'Id' : book.id,
            'Titulo' : book.titulo,
            'Autor' : book.autor,
            'Status' : book.status
        })
    return jsonify({'message' : "Book not found"}), 404

#╔═══════════════════════════════════════════════╗
#║         ROTA PARA VER OS LIVROS SALVOS        ║
#╚═══════════════════════════════════════════════╝
@app.route("/api/book", methods=['GET'])
def recuperar_detalhe_coletivo():
    book = Book.query.all()
    book_list = []

    for item in book:
        book_data = {
            "id": item.id,
            "titulo": item.titulo,
            "autor": item.autor,
            "status": item.status
        }
        book_list.append(book_data)
    return jsonify(book_list)

#╔═══════════════════════════════════════════════╗
#║         ROTA PARA ATUALIZAR OS LIVROS         ║
#╚═══════════════════════════════════════════════╝
@app.route('/api/book/update/<int:book_id>', methods=["PUT"])
def atualizar_livro(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({'message' : 'Book not found'}), 404
    
    data = request.json
    if 'titulo' in data:
        book.titulo = data['titulo']
    
    if 'autor' in data:
        book.autor = data['autor']

    if 'status' in data:
        book.status = data['status']

    db.session.commit()
    return jsonify({'message' : 'Book updated succesfully'})


# Definir a rota raiz ( Pagina inicial )
@app.route('/')
def home():
    return 'ola'

if __name__ == '__main__':
    app.run(debug=True)