from pokemon_game.data_models.AquaPokemon import AquaPokemon
from pokemon_game.data_models.Pokemon import Pokemon

squirtle = AquaPokemon('Squirtle', '002', 10, 50, 10, 20, [('tackle', 5)])
print(squirtle.name, squirtle.pokedexId)
print(squirtle.type.name)