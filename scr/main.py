from scr.game_interactions import GameInteractions
from scr.game_state import GameState

filename = 'save.json'
game_interactions = GameInteractions()
if filename:
    with open(filename, 'r') as fin:
        text = fin.read()
        game = GameState.load(text)
else:
    players = game_interactions.request_players()
    game = GameState(players)

win_player = game.run(game_interactions)
game_interactions.congratulation(win_player)
