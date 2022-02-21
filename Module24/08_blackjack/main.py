# TODO здесь писать код
import random


class BlackJack:

    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen',
                     'King', 'Ace'] * 4
        self.score = 0
        self.computer_score = 0

    def start(self):
        random.shuffle(self.deck)
        self.choice()

        print('До новых встреч!')

    def print_card(self, current_card, score, bot):
        if not bot:
            print('Вам попалась карта {}. У вас {} '
                  'очков.'.format(current_card, score))
        else:
            print('Компьютеру попалась карта {}. У него {} '
                  'очков'.format(current_card, score))

    def random_card(self, score, bot):
        current_card = self.deck.pop()
        if type(current_card) is int:
            score += current_card
        elif current_card == 'Ace':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current_card, score, bot)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.computer_score, True)
        while True:
            if score > 21:
                break
            choice = int(input('Будете брать карту (1 - Да; 2 - Нет)\n'))
            if choice == 1:
                score = self.random_card(score, False)
                if bot_score <= 20:
                    bot_score = self.random_card(bot_score, True)
            elif choice == 2:
                if score > bot_score and bot_score <= 20:
                    while bot_score <= 20:
                        bot_score = self.random_card(bot_score, True)
                break
        if score > 21:
            print('У вас слишком много очков, вы сгорели.')
            return
        elif bot_score == score:
            print('Ничья')
            return
        elif score > bot_score:
            print('Вы выиграли.')
            return
        elif bot_score > score:
            print('Компьютер победил.')


game = BlackJack()
game.start()
