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
    INITIAL_HAND_SIZE = 7
    def __init__(self, players: list[Player], iplayer: int = 0, deck: Deck = None, top: Card = None):
        self.players = players
        self.iplayer = iplayer
        if deck is None:
            deck = Deck(Card.all_cards())
            deck.shuffle()

        self.deck = deck
        if top is None:
            top = self.deck.draw_card()
        self.top = top

        # если у всех игроков нет карт, это новая игра, раздадим по 7 карт всем
        if self.current_player().hand.is_empty():
            for p in self.players:
                for _ in range(self.INITIAL_HAND_SIZE):
                    p.hand.add_card(self.deck.draw_card())


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
        game = cls(players)


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
        p: Player = self.current_player()
        card = p.choose_card(self.top, [])
        if card is None:
            return GameStage.NEXT_TURN if again else GameStage.DRAW_CARD
        p.hand.remove_card(card)
        self.top = card
        return GameStage.NEXT_TURN


    def draw_card(self, game_interactions: GameInteractions) -> GameStage:
        """Текущий игрок берет карту из колоды."""
        card = self.deck.draw_card()
        p = self.current_player()
        p.hand.add_card(card)
        game_interactions.print_draw_card(p)
        return GameStage.PLAY_CARD_AGAIN

    def next_player(self):
        """Ход переходит к следующему игроку."""
        # 0 1 2 0 1 2 0 1 2  i % 3
        # 0 1 2 3 4 5 6 7 8  i
        n = len(self.players)
        self.iplayer = (self.iplayer + 1) % n

    def is_win_condition(self):
        """Проверка, что игрок победил (у него не осталось карт)."""
        p = self.current_player()
        return p.hand.is_empty()





