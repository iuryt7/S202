from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

class AutopecaCRUD:
    def __init__(self, conn):
        self.conn = conn

    def criar_autopeca(self):
        nome = input("Digite o nome da autopeça: ")
        tipo = input("Digite o tipo da autopeça: ")
        valor = float(input("Digite o valor da autopeça: "))
        query = """
        CREATE (peca:Autopeca {nome: $nome, tipo: $tipo, valor: $valor})
        """
        self.conn.query(query, {"nome": nome, "tipo": tipo, "valor": valor})
        print(f"Autopeça '{nome}' criada com sucesso!")

    def ler_autopecas(self):
        query = "MATCH (peca:Autopeca) RETURN peca"
        resultado = self.conn.query(query)
        if resultado:
            for record in resultado:
                peca = record['peca']
                print(f"Nome: {peca['nome']}, Tipo: {peca['tipo']}, Valor: R${peca['valor']}")
        else:
            print("Nenhuma autopeça encontrada.")

    def atualizar_autopeca(self):
        nome_antigo = input("Digite o nome da autopeça a ser atualizada: ")
        nome_novo = input("Digite o novo nome da autopeça: ")
        tipo = input("Digite o novo tipo da autopeça: ")
        valor = float(input("Digite o novo valor da autopeça: "))
        query = """
        MATCH (peca:Autopeca {nome: $nome_antigo})
        SET peca.nome = $nome_novo, peca.tipo = $tipo, peca.valor = $valor
        """
        self.conn.query(query, {"nome_antigo": nome_antigo, "nome_novo": nome_novo, "tipo": tipo, "valor": valor})
        print(f"Autopeça '{nome_antigo}' atualizada para '{nome_novo}'.")

    def deletar_autopeca(self):
        nome = input("Digite o nome da autopeça a ser deletada: ")
        query = "MATCH (peca:Autopeca {nome: $nome}) DETACH DELETE peca"
        self.conn.query(query, {"nome": nome})
        print(f"Autopeça '{nome}' deletada com sucesso!")

class FuncionarioCRUD:
    def __init__(self, conn):
        self.conn = conn

    def criar_funcionario(self):
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        query = """
        CREATE (func:Funcionario {nome: $nome, cargo: $cargo})
        """
        self.conn.query(query, {"nome": nome, "cargo": cargo})
        print(f"Funcionário '{nome}' criado com sucesso!")

    def ler_funcionarios(self):
        query = "MATCH (func:Funcionario) RETURN func"
        resultado = self.conn.query(query)
        if resultado:
            for record in resultado:
                func = record['func']
                print(f"Nome: {func['nome']}, Cargo: {func['cargo']}")
        else:
            print("Nenhum funcionário encontrado.")

    def atualizar_funcionario(self):
        nome_antigo = input("Digite o nome do funcionário a ser atualizado: ")
        nome_novo = input("Digite o novo nome do funcionário: ")
        cargo = input("Digite o novo cargo do funcionário: ")
        query = """
        MATCH (func:Funcionario {nome: $nome_antigo})
        SET func.nome = $nome_novo, func.cargo = $cargo
        """
        self.conn.query(query, {"nome_antigo": nome_antigo, "nome_novo": nome_novo, "cargo": cargo})
        print(f"Funcionário '{nome_antigo}' atualizado para '{nome_novo}'.")

    def deletar_funcionario(self):
        nome = input("Digite o nome do funcionário a ser deletado: ")
        query = "MATCH (func:Funcionario {nome: $nome}) DETACH DELETE func"
        self.conn.query(query, {"nome": nome})
        print(f"Funcionário '{nome}' deletado com sucesso!")

class ClienteCRUD:
    def __init__(self, conn):
        self.conn = conn

    def criar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        query = """
        CREATE (cli:Cliente {nome: $nome, endereco: $endereco})
        """
        self.conn.query(query, {"nome": nome, "endereco": endereco})
        print(f"Cliente '{nome}' criado com sucesso!")

    def ler_clientes(self):
        query = "MATCH (cli:Cliente) RETURN cli"
        resultado = self.conn.query(query)
        if resultado:
            for record in resultado:
                cli = record['cli']
                print(f"Nome: {cli['nome']}, Endereço: {cli['endereco']}")
        else:
            print("Nenhum cliente encontrado.")

    def atualizar_cliente(self):
        nome_antigo = input("Digite o nome do cliente a ser atualizado: ")
        nome_novo = input("Digite o novo nome do cliente: ")
        endereco = input("Digite o novo endereço do cliente: ")
        query = """
        MATCH (cli:Cliente {nome: $nome_antigo})
        SET cli.nome = $nome_novo, cli.endereco = $endereco
        """
        self.conn.query(query, {"nome_antigo": nome_antigo, "nome_novo": nome_novo, "endereco": endereco})
        print(f"Cliente '{nome_antigo}' atualizado para '{nome_novo}'.")

    def deletar_cliente(self):
        nome = input("Digite o nome do cliente a ser deletado: ")
        query = "MATCH (cli:Cliente {nome: $nome}) DETACH DELETE cli"
        self.conn.query(query, {"nome": nome})
        print(f"Cliente '{nome}' deletado com sucesso!")

class VendaCRUD:
    def __init__(self, conn):
        self.conn = conn

    def realizar_venda(self):
        nome_funcionario = input("Digite o nome do funcionário (vendedor): ")
        nome_cliente = input("Digite o nome do cliente (comprador): ")
        nome_peca = input("Digite o nome da autopeça vendida: ")

        query = """
        MATCH (func:Funcionario {nome: $nome_funcionario}),
              (cli:Cliente {nome: $nome_cliente}),
              (peca:Autopeca {nome: $nome_peca})
        CREATE (func)-[:VENDEU]->(peca),
               (cli)-[:COMPROU]->(peca)
        """
        self.conn.query(query, {"nome_funcionario": nome_funcionario, "nome_cliente": nome_cliente, "nome_peca": nome_peca})
        print(f"Venda realizada: '{nome_funcionario}' vendeu a peça '{nome_peca}' para '{nome_cliente}'.")

    def ler_vendas(self):
        query = """
        MATCH (func:Funcionario)-[:VENDEU]->(peca:Autopeca)<-[:COMPROU]-(cli:Cliente)
        RETURN func.nome AS vendedor, cli.nome AS comprador, peca.nome AS peca
        """
        resultado = self.conn.query(query)
        if resultado:
            for record in resultado:
                print(f"Vendedor: {record['vendedor']} | Comprador: {record['comprador']} | Peça: {record['peca']}")
        else:
            print("Nenhuma venda realizada.")

def menu():
    conn = Neo4jConnection(uri="bolt://54.197.199.174", user="neo4j", password="shovel-bats-sense")

    autopeca_crud = AutopecaCRUD(conn)
    funcionario_crud = FuncionarioCRUD(conn)
    cliente_crud = ClienteCRUD(conn)
    venda_crud = VendaCRUD(conn)

    while True:
        print("\nEscolha uma opção:")
        print("1. Criar Autopeça")
        print("2. Ler Autopeças")
        print("3. Atualizar Autopeça")
        print("4. Deletar Autopeça")
        print("5. Criar Funcionário")
        print("6. Ler Funcionários")
        print("7. Atualizar Funcionário")
        print("8. Deletar Funcionário")
        print("9. Criar Cliente")
        print("10. Ler Clientes")
        print("11. Atualizar Cliente")
        print("12. Deletar Cliente")
        print("13. Realizar Venda")
        print("14. Ler Vendas")
        print("15. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            autopeca_crud.criar_autopeca()
        elif opcao == "2":
            autopeca_crud.ler_autopecas()
        elif opcao == "3":
            autopeca_crud.atualizar_autopeca()
        elif opcao == "4":
            autopeca_crud.deletar_autopeca()
        elif opcao == "5":
            funcionario_crud.criar_funcionario()
        elif opcao == "6":
            funcionario_crud.ler_funcionarios()
        elif opcao == "7":
            funcionario_crud.atualizar_funcionario()
        elif opcao == "8":
            funcionario_crud.deletar_funcionario()
        elif opcao == "9":
            cliente_crud.criar_cliente()
        elif opcao == "10":
            cliente_crud.ler_clientes()
        elif opcao == "11":
            cliente_crud.atualizar_cliente()
        elif opcao == "12":
            cliente_crud.deletar_cliente()
        elif opcao == "13":
            venda_crud.realizar_venda()
        elif opcao == "14":
            venda_crud.ler_vendas()
        elif opcao == "15":
            break
        else:
            print("Opção inválida!")

    conn.close()

if __name__ == "__main__":
    menu()
