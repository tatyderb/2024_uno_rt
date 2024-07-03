import json
from enum import Enum

from scr.card import Card
from scr.deck import Deck
from scr.game_interactions import GameInteractions
from scr.player import Player

class GameStage(Enum):
    PLAY_CARD = 1           # DRAW_CARD, NEXT_TURN
    DRAW_CARD = 2           # PLAY_CARD_AGAIN
    PLAY_CARD_AGAIN = 3     # NEXT_TURN
    NEXT_TURN = 4           # PLAY_CARD
    END_GAME = 5            # все, игра закончена


class GameState:
    def __init__(self, players=list[Player], iplayer: int = 0, deck: Deck = None, top: Card = None):
        self.players = players
        self.iplayer = iplayer
        if deck is None:
            deck = Deck(Card.all_cards())
            deck.shuffle()

        self.deck = deck
        if top is None:
            top = self.deck.draw_card()
        self.top = top

    def current_player(self) -> Player:
        return self.players[self.iplayer]

    def save(self) -> dict:
        return {
            'players': [p.save() for p in self.players],
            'current_player_index': self.iplayer,
            'deck': self.deck.save(),
            'top': self.top.save()
        }

    @classmethod
    def load(cls, text):
        data = json.loads(text)
        return cls(players=[Player.load(pd) for pd in data['players']],
                   iplayer=data['current_player_index'],
                   deck=Deck.load(data['deck']),
                   top=Card.load(data['top']))

    @classmethod
    def new_game(cls, players: list[Player]):
        return cls(players)

    def run(self, game_interactions: GameInteractions) -> Player:
        """Игра до победы, возвращает игрока-победителя. До этой функции должны быть вызваны или load, или new_game"""
        stage = GameStage.PLAY_CARD
        while stage != GameStage.END_GAME:
            match stage:
                case GameStage.PLAY_CARD:
                    stage = self.try_play_card()
                case GameStage.DRAW_CARD:
                    stage = self.draw_card(game_interactions)
                case GameStage.PLAY_CARD_AGAIN:
                    stage = self.try_play_card(again=True)
                case GameStage.NEXT_TURN:
                    if self.is_win_condition():
                        stage = GameStage.END_GAME
                    else:
                        self.next_player()
                        stage = GameStage.PLAY_CARD
        return self.current_player()


    def try_play_card(self, again: bool = False) -> GameStage:
        """Текущий игрок пытается играть карту с руки. again=True - после того, как уже брал карту из колоды."""
        pass

    def draw_card(self, game_interactions: GameInteractions) -> GameStage:
        """Текущий игрок берет карту из колоды."""
        pass

    def next_player(self):
        """Ход переходит к следующему игроку."""
        pass

    def is_win_condition(self):
        p = self.current_player()
        return p.hand.is_empty()




