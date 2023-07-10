import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

start_game = input("do you want to play a game of blackjack? 'y' or 'n' ")

def calc_total(list):
  total = 0

  for item in list:
    if item == 'J' or item == 'Q' or item == 'K':
      total += 11
    elif item == 'A':
      if total <= 10:
        total += 11
      else:
        total += 1
    else:
      total += item

  return total

def play_blackjack(value):
  if value == 'y':
    card1 = cards[random.randint(0, (len(cards) - 1))]
    card2 = cards[random.randint(0, (len(cards) - 1))]

    player_hand = [card1, card2]
    player_total = calc_total(player_hand)

    house1 = cards[random.randint(0, (len(cards) - 1))]
    house2 = cards[random.randint(0, (len(cards) - 1))]

    house_hand = [house1, house2]
    house_show = [house1]
    print("")
    print(f"your cards are {player_hand}")
    print(f"house = {house_show}")
    print("")
    action = input("would you like to hit, hold? ")

    def add_card(list, act, func):
      if act == 'hit':
        list.append(cards[random.randint(0, (len(cards) - 1))])
        new_total = func(list)

        if new_total >= 21:
          return new_total

        if new_total <= 21:
          print(f"your current total is {new_total}")
          new_action = input("would you like to hit, hold? ")

          return add_card(list, new_action, func)

      if act == 'hold':
        return func(list)

    player_sum = add_card(player_hand, action, calc_total)

    def play_house(list, func):
      sum = func(list)

      if sum >= 17:
        return sum

      if sum <= 16:
        list.append(cards[random.randint(0, (len(cards) - 1))])
        return play_house(list, func)

    house_total = play_house(house_hand, calc_total)
    print("")
    print(f"your total = {player_sum}")
    print(f"the house's total = {house_total}")

    if player_sum != None:
      if player_sum > 21:
        print('you lost!')
      elif player_sum == 21:
        print('you won!')
      elif player_sum >= house_total:
        print('you won!')
      elif player_sum <= 21 and house_total > 21:
        print('you won!')

    print("")
    play_again = input("play again? 'y' or 'n'? ")
    play_blackjack(play_again)

  if value == 'n':
    print('see you next time')

play_blackjack(start_game)