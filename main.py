############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import sys
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(card_list):
    score = 0
    for card in card_list:
        if card == 11 and score + card > 21:
            score += 1
        else:
            score += card
    return score


def play_blackjack():
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if user_input.lower() == 'y':
        print(os.name)
        user_cards = list(random.choices(cards, k=2))
        computer_cards = [random.choice(cards)]
        hit = True
        first_draw = True
        while hit:
            user_current_score = calculate_score(user_cards)

            if first_draw and user_current_score == 21:
                print(f"Your cards: {user_cards}, current score: 0")
                print(f"Computer's first card: {computer_cards[0]}")
                print(f"Your final hand: {user_cards}, final score: 0")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_cards[0]}")
                print("Win with a Blackjack 😎")
                play_blackjack()
            elif user_current_score > 21:
                print(f"Your cards: {user_cards}, current score: {user_current_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                print(f"Your final hand: {user_cards}, final score: {user_current_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_cards[0]}")
                print("You went over. You lose 😭")
                play_blackjack()

            print(f"Your cards: {user_cards}, current score: {user_current_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card.lower() == 'y':
                first_draw = False
                user_cards.append(random.choice(cards))
            elif get_another_card.lower() == 'n':
                hit = False
                user_final_score = calculate_score(user_cards)
                print(f"Your final hand: {user_cards}, final score: {user_final_score}")
                while calculate_score(computer_cards) < 17:
                    computer_cards.append(random.choice(cards))
                computer_final_score = calculate_score(computer_cards)
                print(f"Computer's final hand: {computer_cards}, final score: {computer_final_score}")

                if user_final_score > computer_final_score:
                    print("You Win 😀")
                elif user_current_score == computer_final_score:
                    print("Draw 🙃")
                else:
                    print("You Lose 😤")
                play_blackjack()
    elif user_input.lower() == 'n':
        sys.exit(0)


play_blackjack()
