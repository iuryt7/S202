class TeacherCRUD:
    def __init__(self, database):
        self.database = database

    def create(self, name, ano_nasc, cpf):
        query = f"CREATE (t:Teacher {{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}})"
        self.database.run_query(query)

    def read(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) RETURN t"
        return self.database.run_query(query)

    def delete(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) DELETE t"
        self.database.run_query(query)

    def update(self, name, newCpf):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) SET t.cpf = '{newCpf}'"
        self.database.run_query(query)
