from scr.card import Card
from scr.player import Player


class GameInteractions:

    @staticmethod
    def print_draw_card(player: Player):
        print(f'{player.name} draw card')
        GameInteractions.print_player_info(player)

    @staticmethod
    def print_player_info(player: Player):
        print(player)

    @staticmethod
    def print_table_info(top: Card):
        print(f'Top: {top}')

    @staticmethod
    def request_players():
        n = int(input('Введите количество игроков: '))
        players = []
        for i in range(n):
            name = input(f'Введите имя игрока {i+1}: ')
            is_human = input('Это человек (y) или бот (n)? ') in 'yYдДуУ'
            players.append(Player(name=name, is_human=is_human))
        return players

    @staticmethod
    def congratulation(win_player: Player):
        print(f'Поздравляем! Победил игрок {win_player.name}')

