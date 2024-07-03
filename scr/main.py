from scr.game_interactions import GameInteractions
from scr.game_state import GameState

filename = 'save.json'
game_interactions = GameInteractions()
game = GameState()
if filename:
    with open(filename, 'r') as fin:
        text = fin.read()
        game.load(text)
else:
    players = game_interactions.request_players()
    game.new_game(players)

win_player = game.run()
game_interactions.congratulation(win_player)
