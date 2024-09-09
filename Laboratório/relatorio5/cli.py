class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com o comando: ")
            if command == "sair":
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido.")


class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        _id = int(input("Qual o ID do livro: "))
        titulo = input("Qual o titulo do livro: ")
        autor = input("Qual o autor do livro: ")
        ano = int(input("Qual o ano do livro: "))
        preco = float(input("Qual o preco do livro: "))
        self.book_model.create_book(_id, titulo, autor, ano, preco)

    def read_book(self):
        _id = int(input("Entre com o ID do livro: "))
        book = self.book_model.read_book_by_id(_id)
        if book:
            print(f"Titulo: {book['titulo']}")
            print(f"Autor: {book['autor']}")
            print(f"Ano: {book['ano']}")
            print(f"Preco: {book['preco']}")
        else:
            print("Livro nao encontrado.")

    def update_book(self):
        _id = int(input("Qual o ID do livro: "))
        titulo = input("Qual o titulo do livro: ")
        autor = input("Qual o autor do livro: ")
        ano = int(input("Qual o ano do livro: "))
        preco = float(input("Qual o preco do livro: "))
        self.book_model.update_book(_id, titulo, autor, ano, preco)

    def delete_book(self):
        _id = int(input("Entre com o ID do livro: "))
        self.book_model.delete_book(_id)

    def run(self):
        print("Relatorio 5 - CRUDE")
        print("Comandos: create, read, update, delete, sair")
        super().run()
