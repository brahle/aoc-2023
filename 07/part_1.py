
card_values = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}


class Hand():
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.card_dict = {
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            'T': 0,
            'J': 0,
            'Q': 0,
            'K': 0,
            'A': 0
        }
        for card in self.cards:
            self.card_dict[card] += 1
        self.card_values = [card_values[card] for card in self.cards]

    def is_five_of_a_kind(self):
        return len(set(self.cards)) == 1

    def is_four_of_a_kind(self):
        for card in self.cards:
            if self.card_dict[card] == 4:
                return True
        return False

    def is_full_house(self):
        has_three = False
        has_two = False
        for card in self.cards:
            if self.card_dict[card] == 3:
                has_three = True
            elif self.card_dict[card] == 2:
                has_two = True
        return has_three and has_two

    def is_three_of_a_kind(self):
        for card in self.cards:
            if self.card_dict[card] == 3:
                return not self.is_full_house()
        return False

    def is_two_pair(self):
        pairs = 0
        for card in set(self.cards):
            if self.card_dict[card] == 2:
                pairs += 1
        return pairs == 2

    def is_one_pair(self):
        for card in self.cards:
            if self.card_dict[card] == 2:
                return not self.is_two_pair() and not self.is_full_house()
        return False

    def is_high_card(self):
        for card in self.cards:
            if self.card_dict[card] > 1:
                return False
        return True

    def get_order(self):
        return (
            self.is_five_of_a_kind(),
            self.is_four_of_a_kind(),
            self.is_full_house(),
            self.is_three_of_a_kind(),
            self.is_two_pair(),
            self.is_one_pair(),
            self.is_high_card(),
        )


    def __lt__(self, other):
        my_order = self.get_order()
        other_order = other.get_order()
        if my_order != other_order:
            return my_order < other_order
        return self.card_values < other.card_values

    def __repr__(self) -> str:
        return f'Hand({self.cards}, {self.bid}, {self.get_order()})'


def main():
    hands = []

    with open('07/input.txt', 'r') as f:
        for line in f:
            cards, bid = line.split()
            hands.append(Hand(cards, int(bid)))

    hands.sort()
    result = 0
    for i, hand in enumerate(hands):
        print(i + 1, hand, hand.bid * (i + 1))
        result += hand.bid * (i + 1)

    print(result)


if __name__ == '__main__':
    main()
