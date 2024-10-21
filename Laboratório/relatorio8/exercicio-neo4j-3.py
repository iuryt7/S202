from neo4j import GraphDatabase

class GameDatabase:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_player(self, name, player_id):
        with self.driver.session() as session:
            session.run(
                "CREATE (p:Player {name: $name, player_id: $player_id})",
                name=name, player_id=player_id
            )

    def update_player(self, player_id, name):
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {player_id: $player_id}) SET p.name = $name",
                player_id=player_id, name=name
            )

    def get_player(self, player_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Player {player_id: $player_id}) RETURN p.name AS name",
                player_id=player_id
            )
            return result.single()["name"]

    def delete_player(self, player_id):
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {player_id: $player_id}) DETACH DELETE p",
                player_id=player_id
            )

    def create_match(self, match_id, players, result):
        with self.driver.session() as session:
            session.run(
                "CREATE (m:Match {match_id: $match_id, result: $result})",
                match_id=match_id, result=result
            )
            for player_id in players:
                session.run(
                    """
                    MATCH (p:Player {player_id: $player_id}), (m:Match {match_id: $match_id})
                    CREATE (p)-[:PLAYED_IN]->(m)
                    """,
                    player_id=player_id, match_id=match_id
                )

    def get_player_matches(self, player_id):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (p:Player {player_id: $player_id})-[:PLAYED_IN]->(m:Match)
                RETURN m.match_id AS match_id, m.result AS result
                """,
                player_id=player_id
            )
            return [{"match_id": record["match_id"], "result": record["result"]} for record in result]

    def delete_match(self, match_id):
        with self.driver.session() as session:
            session.run(
                "MATCH (m:Match {match_id: $match_id}) DETACH DELETE m",
                match_id=match_id
            )

    def get_all_players(self):
        with self.driver.session() as session:
            result = session.run("MATCH (p:Player) RETURN p.player_id AS player_id, p.name AS name")
            return [{"player_id": record["player_id"], "name": record["name"]} for record in result]

if __name__ == "__main__":
    db = GameDatabase("bolt://34.237.2.20", "neo4j", "nameplates-helicopters-investments")
    db.create_player("Cavani", 1)
    db.create_player("German Cano", 2)
    db.create_match(1, [1, 2], "Fluminense venceu a Libertadores")
    print(db.get_player(1))
    print(db.get_player(1))
    print(db.get_player_matches(1))
    db.close()