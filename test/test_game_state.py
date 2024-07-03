from scr.card import Card
from scr.game_state import GameState, GameStage

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
      "hand": "y6 y1 r8",
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

def test_next_player():
    game = GameState.load(json_data)
    assert game.current_player().name == 'Bob'

    game.next_player()
    assert game.current_player().name == 'Alex'

    game.next_player()
    assert game.current_player().name == 'Bob'


def test_cannot_play():
    game = GameState.load(json_data)
    d1 = game.save()
    stage = game.try_play_card()
    d2 = game.save()
    assert d1 == d2
    assert stage == GameStage.DRAW_CARD

    stage = game.try_play_card(again=True)
    d2 = game.save()
    assert d1 == d2
    assert stage == GameStage.NEXT_TURN

def test_play_card_first():
    #       "hand": "y6 y1 r8",
    tmp = json_data
    game = GameState.load(json_data)
    game.top = Card('red', 6)
    d1 = game.save()

    stage = game.try_play_card()
    d2 = game.save()
    assert stage == GameStage.NEXT_TURN
    assert game.top == Card.load('y6')
    assert d2['players'][1]['hand'] == 'y1 r8'
    assert d1['deck'] == d2['deck']
    assert d1['current_player_index'] == d2['current_player_index']
    # ...






