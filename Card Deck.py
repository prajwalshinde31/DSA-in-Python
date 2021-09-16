from math import ceil
from random import randint

from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

# test cases will be represented as dictionary

test = dict(input={
    'cards': list(range(100000, 0, -1)),
    'query': 61
}, output=5)


def locate_card(cards, query):
    low = 0
    high = len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_num = cards[mid]

        print('lo:', low, ' high:', high, ' mid:', mid, ' mid_num:', mid_num)

        if mid_num == query:
            return mid
        elif mid_num < query:
            high = mid - 1
        elif mid_num > query:
            low = mid + 1

    return -1


def locate_card_linear(cards, query):

    position = 0
    while position <= len(cards):

        if cards[position] == query:
            return position

        position += 1

    return -1


evaluate_test_case(locate_card, test)

