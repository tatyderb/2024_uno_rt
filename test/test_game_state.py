import random

from scr.deck import Deck
from scr.game_interactions import GameInteractions
from scr.player import Player
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
alex_dict = {
      "name": "Alex",
      "hand": "r3 y5 g4 g1",
      "is_human": True
}
bob_dict = {
      "name": "Bob",
      "hand": "y6 y1 r8",
      "is_human": False
}
alex = Player.load({
    "name": "Alex",
    "hand": "r3 y5 g4 g1",
    "is_human": True
})
bob = Player.load({
    "name": "Bob",
    "hand": "y6 y1 r8",
    "is_human": False
})


def test_game_init():
    deck = Deck.load('b0 b5 g1')
    g = GameState(players=[alex, bob], iplayer=1, deck=deck, top=Card('red', 5))
    assert g.players == [alex, bob]
    assert g.iplayer == 1
    assert g.deck == deck
    assert g.top == Card('red', 5)

def test_game_new():
    random.seed(7)
    alex_empty = Player(name='Alex', hand=None, is_human=True)
    bob_empty = Player(name='Bob', hand=None, is_human=False)
    alex_full = Player.load({
        "name": "Alex",
        "hand": "g0 b3 r6 r9 y2 r3 b8",
        "is_human": True
    })
    bob_full = Player.load({
        "name": "Bob",
        "hand": "r7 y7 g8 r4 r2 y8 g7",
        "is_human": False
    })
    g = GameState(players=[alex_empty, bob_empty])
    assert g.players[0] == alex_full
    assert g.players[1] == bob_full
    assert g.iplayer == 0
    assert len(g.deck) == 4*19 - 2*GameState.INITIAL_HAND_SIZE - 1
    assert repr(g.deck) == ('g2 b7 g9 y3 b1 g5 r0 r7 g4 b6 y3 y1 b4 y4 b2 r1 r4 y2 b9 g5 r1 g1 y9 g3 r8 '
        'b5 g4 g3 g1 g2 b0 y6 y6 y8 b7 g6 y5 y4 r9 r8 y0 r2 b4 b9 g6 b1 b6 b8 g9 y7 '
        'b2 r5 y1 g8 b5 r3 y5 g7 r5 r6 y9')
    assert g.top == Card('blue', 3)


def test_game_save():
    random.seed(7)
    alex_empty = Player(name='Alex', hand=None, is_human=True)
    bob_empty = Player(name='Bob', hand=None, is_human=False)
    g = GameState(players=[alex_empty, bob_empty])
    assert g.save() == {'current_player_index': 0,
         'deck': 'g2 b7 g9 y3 b1 g5 r0 r7 g4 b6 y3 y1 b4 y4 b2 r1 r4 y2 b9 g5 r1 g1 y9 ' + \
                 'g3 r8 b5 g4 g3 g1 g2 b0 y6 y6 y8 b7 g6 y5 y4 r9 r8 y0 r2 b4 b9 g6 b1 ' + \
                 'b6 b8 g9 y7 b2 r5 y1 g8 b5 r3 y5 g7 r5 r6 y9',
         'players': [{'hand': 'g0 b3 r6 r9 y2 r3 b8', 'is_human': True, 'name': 'Alex'},
                     {'hand': 'r7 y7 g8 r4 r2 y8 g7', 'is_human': False, 'name': 'Bob'}
                     ],
         'top': 'b3'
            }

def test_game_load():
    g = GameState.load(json_data)
    assert g.players == [alex, bob]
    assert g.iplayer == 1
    assert g.top == Card('green', 2)
    assert repr(g.deck) == "g7 b6 y1 y0 r9"
    # проверяем, что в колоде действительно карты, а не строкой хранится.
    assert g.deck.cards[0] == Card('green', 7)


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
      "hand": "r3",
      "is_human": false
    }
  ]
}
'''
    game = GameState.load(tmp)
    game.current_player().hand.cards = []
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

def test_draw_card():
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
    g = GameState.load(json_data)
    gi = GameInteractions()
    stage = g.draw_card(gi)
    assert repr(g.current_player().hand) == 'y6 y1 r8 r9'
    assert repr(g.deck) == "g7 b6 y1 y0"
    assert stage == GameStage.PLAY_CARD_AGAIN




