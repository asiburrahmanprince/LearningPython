from pokemon_game.data_models.PokeType import PokeType
from pokemon_game.data_models.Pokemon import Pokemon


class FirePokemon(Pokemon):
    def __init__(self, name, pokedexId, level, living_points,
                 attacking_points, defense_points, attack):
        super().__init__(name, pokedexId, level, living_points, attacking_points, defense_points, attack)
        self.type: PokeType = PokeType(1)

    def lvlUp(self) -> Pokemon:
        pass
