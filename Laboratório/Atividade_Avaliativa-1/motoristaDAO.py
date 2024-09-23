class MotoristaCLI:
    def __init__(self):
        self.comandos = {}

    def adicionar_comando(self, nome, funcao):
        self.comandos[nome] = funcao

    def run(self):
        while True:
            comando = input("Digite um comando: ")
            if comando == "sair":
                print("Adeus!")
                break
            elif comando in self.comandos:
                self.comandos[comando]()
            else:
                print("Comando inválido. Tente novamente.")


class MotoristaDAO(MotoristaCLI):
    def __init__(self, motorista_modelo):
        super().__init__()
        self.motorista_modelo = motorista_modelo
        self.adicionar_comando("criar", self.criar_motorista)
        self.adicionar_comando("ler", self.ler_motorista)
        self.adicionar_comando("atualizar", self.atualizar_motorista)
        self.adicionar_comando("deletar", self.deletar_motorista)

    def criar_corrida(self):
        # Coleta informações da corrida
        nota_corrida = int(input("Nota da corrida: "))
        distancia_corrida = float(input("Distância da corrida (em km): "))
        valor_corrida = float(input("Valor da corrida (em R$): "))
        nome_passageiro = input("Nome do passageiro: ")
        documento_passageiro = input("Documento do passageiro: ")

        corrida = {
            'nota': nota_corrida,
            'distancia': distancia_corrida,
            'valor': valor_corrida,
            'passageiro': {
                'nome': nome_passageiro,
                'documento': documento_passageiro
            }
        }

        return corrida

    def criar_motorista(self):
        motorista_id = int(input("ID do motorista: "))
        nome = input("Nome do motorista: ")
        nota = int(input("Nota do motorista: "))

        corridas = []
        while True:
            adicionar_corrida = input("Você quer adicionar corridas? (s/n): ")
            if adicionar_corrida.lower() == 'n':
                break
            corrida = self.criar_corrida()
            corridas.append(corrida)

        self.motorista_modelo.create_motorista(motorista_id, nome, corridas, nota)

    def ler_motorista(self):
        motorista_id = int(input("Digite o ID do motorista: "))
        motorista = self.motorista_modelo.read_motorista(motorista_id)
        if motorista:
            print(f"Nome do Motorista: {motorista['nome']}")
            print(f"Nota do Motorista: {motorista['nota']}")
            print("Corridas:")
            for corrida in motorista['corridas']:
                print(f"  Nota da Corrida: {corrida['nota']}")
                print(f"  Distância da Corrida: {corrida['distancia']} km")
                print(f"  Valor da Corrida: R$ {corrida['valor']}")
                print(f"  Nome do Passageiro: {corrida['passageiro']['nome']}")
                print(f"  Documento do Passageiro: {corrida['passageiro']['documento']}")
                print("------")
        else:
            print("Motorista não encontrado.")

    def atualizar_motorista(self):
        # Agora essa função coleta os dados do motorista a partir do input do usuário
        motorista_id = int(input("Digite o ID do motorista a ser atualizado: "))
        nome = input("Digite o novo nome do motorista: ")
        nota = int(input("Digite a nova nota do motorista: "))

        corridas = []
        while True:
            adicionar_corrida = input("Você quer adicionar novas corridas? (s/n): ")
            if adicionar_corrida.lower() == 'n':
                break
            corrida = self.criar_corrida()
            corridas.append(corrida)

        self.motorista_modelo.update_motorista(motorista_id, nome, corridas, nota)

    def deletar_motorista(self):
        motorista_id = int(input("Digite o ID do motorista: "))
        self.motorista_modelo.delete_motorista(motorista_id)

    def run(self):
        print("Bem-vindo ao CLI de Motoristas!")
        print("Comandos disponíveis: criar, ler, atualizar, deletar, sair")
        super().run()