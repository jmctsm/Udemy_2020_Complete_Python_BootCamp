
# We'll use this later
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't do anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:
    def __init__(self):
        self.name = input("Please enter your name: ")
        seed_money = -1
        while True:
            try:
                seed_money = int(input("Please enter your starting money amount: "))
            except:
                print("Please enter a number")
                continue
            else:
                if seed_money > 0:
                    break
                else:
                    print("Please enter a number larger than 0")
                    continue

        self.money = seed_money
        # A new player has no cards or points
        self.all_cards = []
        self.card_value = []

    def add_cards(self, new_card):
        self.all_cards.append(new_card)
        self.card_value.append(values[new_card.rank])
        print(f"{self.name} has {len(self.all_cards)} cards.")

    def remove_all_cards(self):
        self.all_cards = []
        self.card_value = []

    def __str__(self):
        return f"{self.name} has ${str(self.money)}."

    def bet(self):
        bet_amount = 0
        while True:
            try:
                bet_amount = int(input("Please enter the amount to bet this hand: "))
            except:
                print("Please enter a number")
                continue
            else:
                if bet_amount > 0 and bet_amount <= self.money:
                    break
                else:
                    print("Please enter a number larger than 0")
                    continue
        self.bet_amount = bet_amount

    def lost(self):
        self.money = self.money - self.bet_amount


class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.all_cards = []


player_one = Player()
print(player_one)

new_deck = Deck()
new_deck.shuffle()

game_on = True

while game_on:
    player_one.bet()
    player_one.add_cards(new_deck.deal_one())
    if "Ace" in player_one.all_cards:
        print("Player has an ACE!!!")
    if sum(player_one.card_value) > 21:
        print(f"{player_one.name} has BUSTED!!!!")
        player_one.lost()
        game_on = False
        print(sum(player_one.card_value))
        break
    elif sum(player_one.card_value) == 21:
        print(f"{player_one.name} has 21!!!!")
        print(sum(player_one.card_value))
        break
    elif sum(player_one.card_value) < 21:
        print("Under 21")
        print(sum(player_one.card_value))
        break