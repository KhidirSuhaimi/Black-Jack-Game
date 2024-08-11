#blackjack game
import random
set_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

end_game = False
answer = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
if answer == 'y':
    end_game = False
else:
    end_game = True
cont = True

while not end_game:
    print("\n" *10)
    player_cards = []
    computer_cards = []
    player_total = 0
    computer_total = 0
    cont = True
    conti = True

    if not player_cards:
        for i in range(2):
            card = random.choice(set_cards)
            player_cards.append(card)
            player_total+=card

        for i in range(1):
            card =  random.choice(set_cards)
            computer_cards.append(card)
            computer_total += card
        print(f"Player has cards {player_cards}, Current Score: {player_total}")
        print((f"Computer has card {computer_cards}"))

    while cont:
        continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
        if continue_game == 'y':
            cont = True
        else:
            cont = False

        if player_total <21 and cont:
            card = random.choice(set_cards)
            player_cards.append(card)
            player_total += card
            print(f"Your cards {player_cards}, current score: {player_total}")
            print(f"Computer's first card: {computer_total}")
        if player_total >21 and cont:
            print(f"Your final hand: {player_cards}, final score: {player_total}")
            print(f"Computer's hand: {computer_cards}, final score: {computer_total}")
            print("You went over, You Lose!")
            cont = False
            conti = False

    if conti:
        card = random.choice(set_cards)
        computer_cards.append(card)
        computer_total += card
        while computer_total <17:
            card = random.choice(set_cards)
            computer_cards.append(card)
            computer_total += card
        if computer_total > player_total and computer_total <=21 :
            print(f"Your final hand: {player_cards}, final score: {player_total}")
            print(f"Computer's hand: {computer_cards}, final score: {computer_total}")
            print("You Lose!")
        elif player_total > computer_total:
            print(f"Your final hand: {player_cards}, final score: {player_total}")
            print(f"Computer's hand: {computer_cards}, final score: {computer_total}")
            print("You Win!")
        elif computer_total >  player_total and computer_total >21:
            print(f"Your final hand: {player_cards}, final score: {player_total}")
            print(f"Computer's hand: {computer_cards}, final score: {computer_total}")
            print("You Win!")
        else:
            print(f"Your final hand: {player_cards}, final score: {player_total}")
            print(f"Computer's hand: {computer_cards}, final score: {computer_total}")
            print("It's a Draw!")

    if not end_game:
        answer = input("Do you want to continue? Type 'y' or 'n': ")
        if answer == 'y':
            end_game = False
        else:
            end_game = True


