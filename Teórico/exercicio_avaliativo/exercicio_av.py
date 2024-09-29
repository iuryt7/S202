"""
Códigos do neo4j

CREATE(:Pessoa:Familia{nome:'Guilherme', idade:'29', sexo:'masculino'})

CREATE(:Pessoa:Familia{nome:'Rhuan', idade:'29', sexo:'masculino'})

CREATE(:Pessoa:Familia{nome:'Rhanna', idade:'29', sexo:'feminino'})

CREATE(:Pessoa:Familia{nome:'Maria Carolina', idade:'21', sexo:'feminino'})

CREATE(:Pessoa:Familia{nome:'Aparecida', idade:'70', sexo:'feminino'})

CREATE(:Pessoa:Familia{nome:'Devanir', idade:'73', sexo:'masculino'})

CREATE(:Pessoa:Familia{nome:'Ana Maria', idade:'73', sexo:'feminino'})

CREATE(:Pessoa:Familia{nome:'Juvenil', idade:'70', sexo:'masculino'})

CREATE(:Pessoa:Familia{nome:'Flavio', idade:'53', sexo:'masculino'})

CREATE(:Pessoa:Familia{nome:'Hingligy', idade:'50', sexo:'feminino'})

CREATE(:Pessoa:Familia{nome:'Iury', idade:'23', sexo:'masculino'})

MATCH(p:Pessoa{nome:'Devanir'}),(d:Pessoa{nome:'Aparecida'})
CREATE (p)-[:E_CASAL{relacao:'casados'}]->(d);

MATCH(p:Pessoa{nome:'Juvenil'}),(d:Pessoa{nome:'Ana Maria'})
CREATE (p)-[:E_CASAL{relacao:'casados'}]->(d);

MATCH(p:Pessoa{nome:'Hingligy'}),(d:Pessoa{nome:'Flavio'})
CREATE (p)-[:E_CASAL{relacao:'casados'}]->(d);

MATCH(p:Pessoa{nome:'Guilherme'}),(d:Pessoa{nome:'Rhanna'})
CREATE (p)-[:E_CASAL{relacao:'casados'}]->(d);

MATCH(p:Pessoa{nome:'Iury'}),(d:Pessoa{nome:'Maria Carolina'})
CREATE (p)-[:E_CASAL{relacao:'namorados'}]->(d);

MATCH(p:Pessoa{nome:'Rhuan'}),(d:Pessoa{nome:'Rhanna'})
CREATE (p)-[:PRIMO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhuan'}),(d:Pessoa{nome:'Iury'})
CREATE (p)-[:PRIMO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhuan'}),(d:Pessoa{nome:'Hingligy'})
CREATE (p)-[:SOBRINHO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhuan'}),(d:Pessoa{nome:'Flavio'})
CREATE (p)-[:SOBRINHO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhuan'}),(d:Pessoa{nome:'Aparecida'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhuan'}),(d:Pessoa{nome:'Devanir'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhanna'}),(d:Pessoa{nome:'Ana Maria'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhanna'}),(d:Pessoa{nome:'Juvenil'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhanna'}),(d:Pessoa{nome:'Aparecida'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhanna'}),(d:Pessoa{nome:'Devanir'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Iury'}),(d:Pessoa{nome:'Ana Maria'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Iury'}),(d:Pessoa{nome:'Juvenil'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Iury'}),(d:Pessoa{nome:'Aparecida'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Iury'}),(d:Pessoa{nome:'Devanir'})
CREATE (p)-[:NETO_DE]->(d);

MATCH(p:Pessoa{nome:'Flavio'}),(d:Pessoa{nome:'Devanir'})
CREATE (p)-[:FILHO_DE]->(d);

MATCH(p:Pessoa{nome:'Flavio'}),(d:Pessoa{nome:'Aparecida'})
CREATE (p)-[:FILHO_DE]->(d);

MATCH(p:Pessoa{nome:'Iury'}),(d:Pessoa{nome:'Rhanna'})
CREATE (p)-[:IRMAO_DE]->(d);

MATCH(p:Pessoa{nome:'Hingligy'}),(d:Pessoa{nome:'Ana Maria'})
CREATE (p)-[:FILHO_DE]->(d);

MATCH(p:Pessoa{nome:'Hingligy'}),(d:Pessoa{nome:'Juvenil'})
CREATE (p)-[:FILHO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhanna'}),(d:Pessoa{nome:'Flavio'})
CREATE (p)-[:FILHO_DE]->(d);

MATCH(p:Pessoa{nome:'Rhanna'}),(d:Pessoa{nome:'Hingligy'})
CREATE (p)-[:FILHO_DE]->(d);

MATCH(p:Pessoa{nome:'Iury'}),(d:Pessoa{nome:'Flavio'})
CREATE (p)-[:FILHO_DE]->(d);

MATCH(p:Pessoa{nome:'Iury'}),(d:Pessoa{nome:'Hingligy'})
CREATE (p)-[:FILHO_DE]->(d);


"""

from neo4j import GraphDatabase

# Função para criar o cliente de consulta ao grafo
class GraphClient:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # Função para encontrar pessoas do sexo feminino
    def quem_e_feminino(self):
        query = "MATCH (p:Pessoa {sexo: 'feminino'}) RETURN p.nome AS nome"
        with self.driver.session() as session:
            result = session.run(query)
            feminino = [record["nome"] for record in result]
            return feminino

    # Função para encontrar primos
    def quem_e_primo(self):
        query = "MATCH (p1:Pessoa)-[:PRIMO_DE]->(p2:Pessoa) RETURN p1.nome AS primo1, p2.nome AS primo2"
        with self.driver.session() as session:
            result = session.run(query)
            primos = [{"primo1": record["primo1"], "primo2": record["primo2"]} for record in result]
            return primos

    # Função para encontrar casais
    def quem_e_casal(self):
        query = """
        MATCH (p1:Pessoa)-[r:E_CASAL]->(p2:Pessoa)
        RETURN p1.nome AS pessoa1, p2.nome AS pessoa2, r.relacao AS relacao
        """
        with self.driver.session() as session:
            result = session.run(query)
            casais = [{"pessoa1": record["pessoa1"], "pessoa2": record["pessoa2"], "relacao": record["relacao"]} for record in result]
            return casais

    # Função para encontrar irmãos
    def quem_e_irmao(self):
        query = "MATCH (p1:Pessoa)-[:IRMAO_DE]->(p2:Pessoa) RETURN p1.nome AS pessoa1, p2.nome AS pessoa2"
        with self.driver.session() as session:
            result = session.run(query)
            irmaos = [{"irmao1": record["pessoa1"], "irmao2": record["pessoa2"]} for record in result]
            return irmaos

    # Função para encontrar sobrinhos
    def quem_e_sobrinho(self):
        query = "MATCH (p1:Pessoa)-[:SOBRINHO_DE]->(p2:Pessoa) RETURN p1.nome AS sobrinho, p2.nome AS tio"
        with self.driver.session() as session:
            result = session.run(query)
            sobrinhos = [{"sobrinho": record["sobrinho"], "tio": record["tio"]} for record in result]
            return sobrinhos

    # Função para encontrar quem é pai de quem
    def quem_e_pai(self):
        query = "MATCH (p1:Pessoa)-[:FILHO_DE]->(p2:Pessoa) RETURN p1.nome AS filho, p2.nome AS pai"
        with self.driver.session() as session:
            result = session.run(query)
            pais_filhos = [{"pai": record["pai"], "filho": record["filho"]} for record in result]
            return pais_filhos

    # Função para encontrar quem é avô de quem
    def quem_e_avo(self):
        query = """
        MATCH (avo:Pessoa)-[:NETO_DE]->(filho:Pessoa)
        RETURN avo.nome AS neto, filho.nome AS avo
        """
        with self.driver.session() as session:
            result = session.run(query)
            avos_netos = [{"avo": record["avo"], "neto": record["neto"]} for record in result]
            return avos_netos

if __name__ == "__main__":

    uri = "bolt://44.203.29.218:7687"
    user = "neo4j"
    password = "valve-lesson-commissions"

    # Criar o cliente de grafo
    client = GraphClient(uri, user, password)

    # Consultar e imprimir as pessoas do sexo feminino
    feminino = client.quem_e_feminino()
    print(f"Pessoas do sexo feminino na família: {feminino}")
    print("")

    # Consultar e imprimir quem são os primos
    primos = client.quem_e_primo()
    for relacao in primos:
        print(f"{relacao['primo1']} é primo de {relacao['primo2']}")

    print("")

    # Consultar e imprimir quem é pai de quem
    pais_filhos = client.quem_e_pai()
    for relacao in pais_filhos:
        print(f"{relacao['pai']} é pai de {relacao['filho']}")

    print("")

    # Consultar e imprimir quem é avô de quem
    avos_netos = client.quem_e_avo()
    for relacao in avos_netos:
        print(f"{relacao['avo']} é avô de {relacao['neto']}")

    print("")

    # Consultar e imprimir quem são os irmãos
    irmaos = client.quem_e_irmao()
    for relacao in irmaos:
        print(f"{relacao['irmao1']} é irmão de {relacao['irmao2']}")

    print("")

    # Consultar e imprimir quem são os casais
    casais = client.quem_e_casal()
    for relacao in casais:
        print(f"{relacao['pessoa1']} e {relacao['pessoa2']} são um casal, relação: {relacao['relacao']}")

    print("")

    # Consultar e imprimir quem são os sobrinhos
    sobrinhos = client.quem_e_sobrinho()
    for relacao in sobrinhos:
        print(f"{relacao['sobrinho']} é sobrinho(a) de {relacao['tio']}")

    # Fechar a conexão
    client.close()
