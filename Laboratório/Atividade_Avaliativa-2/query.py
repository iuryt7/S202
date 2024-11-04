from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return [record for record in result]

# Questão 1
def questao1_a(database):
    query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
    return database.run_query(query)

def questao1_b(database):
    query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
    return database.run_query(query)

def questao1_c(database):
    query = "MATCH (c:City) RETURN c.name"
    return database.run_query(query)

def questao1_d(database):
    query = """
    MATCH (s:School)
    WHERE s.number >= 150 AND s.number <= 550
    RETURN s.name, s.endereco, s.number
    """
    return database.run_query(query)

# Questão 2
def questao2_a(database):
    query = "MATCH (t:Teacher) RETURN min(t.ano_nasc) AS mais_jovem, max(t.ano_nasc) AS mais_velho"
    return database.run_query(query)

def questao2_b(database):
    query = "MATCH (c:City) RETURN avg(c.population) AS media_habitantes"
    return database.run_query(query)

def questao2_c(database):
    query = """
    MATCH (c:City {cep: '37540-000'})
    RETURN replace(c.name, 'a', 'A') AS nome_alterado
    """
    return database.run_query(query)

def questao2_d(database):
    query = """
    MATCH (t:Teacher)
    RETURN substring(t.name, 3, 1) AS letra_a_partir_terceira
    """
    return database.run_query(query)
