from scr.game_state import GameState

json_data = '''
{
  "top": "g2",
  "deck": "g7 b6 y1 y0 r9",
  "current_player_index": 1,
  "players": [
    {
      "name": "Alex",
      "hand": "r3 y5 g4 g1",
      "is_human": true
    },
    {
      "name": "Bob",
      "hand": "y6 y2 r8",
      "is_human": false
    }
  ]
}
'''

def test_game_new():
    pass

def test_game_save():
    pass

def test_game_load():
    pass

def test_win_condition():
    tmp = '''
{
  "top": "g2",
  "deck": "g7 b6 y1 y0 r9",
  "current_player_index": 1,
  "players": [
    {
      "name": "Alex",
      "hand": "r3 y5 g4 g1",
      "is_human": true
    },
    {
      "name": "Bob",
      "hand": "",
      "is_human": false
    }
  ]
}
'''
    game = GameState.load(tmp)
    assert game.is_win_condition()

    game.iplayer = 0
    assert not game.is_win_condition()



