import json
from datetime import datetime

class Database:
    def __init__(self):
        self.data = {
            "pokemon": [
                {"id": 1, "name": "Bulbasaur", "type": "Grass/Poison"},
                {"id": 2, "name": "Ivysaur", "type": "Grass/Poison"},
                {"id": 3, "name": "Venusaur", "type": "Grass/Poison"},
            ]
        }

    def get_all_pokemon(self):
        return self.data["pokemon"]

    def get_pokemon_by_id(self, pokemon_id):
        for pokemon in self.data["pokemon"]:
            if pokemon["id"] == pokemon_id:
                return pokemon
        return None

    def get_pokemon_by_name(self, name):
        for pokemon in self.data["pokemon"]:
            if pokemon["name"].lower() == name.lower():
                return pokemon
        return None

    def get_pokemon_by_type(self, pokemon_type):
        return [pokemon for pokemon in self.data["pokemon"] if pokemon_type.lower() in pokemon["type"].lower()]

    def add_pokemon(self, pokemon):
        self.data["pokemon"].append(pokemon)
        return pokemon


class Pokedex:
    def __init__(self, database):
        self.database = database

    def log_action(self, action, details):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details
        }
        self.writeAJson(log_entry)

    def writeAJson(self, log_entry):
        with open("log.json", "a") as logfile:
            logfile.write(json.dumps(log_entry) + "\n")

    def show_all_pokemon(self):
        result = self.database.get_all_pokemon()
        self.log_action("show_all_pokemon", {"result_count": len(result)})
        return result

    def find_pokemon_by_id(self, pokemon_id):
        result = self.database.get_pokemon_by_id(pokemon_id)
        self.log_action("find_pokemon_by_id", {"pokemon_id": pokemon_id, "found": result is not None})
        return result

    def find_pokemon_by_name(self, name):
        result = self.database.get_pokemon_by_name(name)
        self.log_action("find_pokemon_by_name", {"name": name, "found": result is not None})
        return result

    def find_pokemon_by_type(self, pokemon_type):
        result = self.database.get_pokemon_by_type(pokemon_type)
        self.log_action("find_pokemon_by_type", {"type": pokemon_type, "result_count": len(result)})
        return result

    def add_new_pokemon(self, pokemon):
        result = self.database.add_pokemon(pokemon)
        self.log_action("add_new_pokemon", {"pokemon": pokemon})
        return result

database = Database()
pokedex = Pokedex(database)

pokedex.add_new_pokemon({"id": 4, "name": "Charmander", "type": "Fire"})

print(pokedex.show_all_pokemon())

print(pokedex.find_pokemon_by_id(1))

print(pokedex.find_pokemon_by_name("Ivysaur"))

print(pokedex.find_pokemon_by_type("Fire"))
