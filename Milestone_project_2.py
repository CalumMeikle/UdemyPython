'''
Milestone project 2, a game of backgammon
'''

import random



class Deck:

    def __init__(self, cards):
        self.cards = cards

    def deck_contents(self):
        #return the elements of the deck
        return self.cards

    def my_rand(self):
        #Call a random card from the deck and then removing it from the deck
        card = random.choice(self.deck_contents())
        self.cards.remove(card)
        return card

    def __len__(self):
        return len(self.cards)



class Player:

    def __init__(self, name, first_card, second_card):
        self.name = name
        self.first_card = first_card
        self.second_card = second_card


    def hit(self, new_card):
        return dealing_with_an_ace(new_card)

    def stay(self, *args):
        return self.first_card, self.second_card, args

    def dealing_with_an_ace(self, new_card1=0, new_card2=0):
        try:
            sum_of_both = self.first_card + self.second_card + new_card + new_card2
            return f"The sum of your first two cards is {sum_of_both}", "Do you want to hit or stay? "
        except TypeError:
            first_list = [self.first_card, self.second_card] + list(new_card1, new_card2)
            first_list['Ace'] = 1
            second_list = [self.first_card, self.second_card] + list(new_card1, new_card2)
            second_list['Ace'] = 11
            return f"There is an Ace, your sum is either {sum(first_list)} or {sum(second_list)}", "Do you want to hit or stay? "





    #def dealing_with_ace(self):
        #if self.first_card == 'Ace':



    def __str__(self):
        return f"Welcome {self.name}.\nYour starting cards are ({self.first_card} {self.second_card})"



class Human(Player):
    pass

    #def sorting_through_starting_cards(self):
     #   if self.first_card == 'Ace' or self.second_card == 'Ace':






class Computer(Player):

    def __str__(self):
        return f"{self.name} can only show the {self.second_card}"



if __name__ == "__main__":
    #Setting up the game mode
    cards = Deck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'Ace'] * 4)

    #pick first card for human
    first_card_human = cards.my_rand()
    #cards.remove(first_card_human)

    first_card_computer = cards.my_rand()

    #pick ssecond card for human
    second_card_human = cards.my_rand()

    #pick second card for computer
    second_card_computer = cards.my_rand()

    assert len(cards) == 52;

    calum = Human('calum', first_card_human, second_card_human)
    hal9000 = Computer('hal9000', first_card_computer, second_card_computer)

    print(calum.dealing_with_an_ace()[0])
    hit_or_stay_human = str(input(calum.dealing_with_an_ace()[1])).lower()
    if hit_or_stay_human == 'hit':
        calum.hit(cards.my_rand())
    else:
        calum.stay()
    print(calum)


