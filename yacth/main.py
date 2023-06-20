import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

def count_dice(dice, value):
    return dice.count(value)

def score_dice(dice):
    score = 0
    for i in range(1, 7):
        count = count_dice(dice, i)
        if count >= 3:
            score += i * 3
        if count == 4:
            score += i * 2
        if count == 5:
            score += 50
    return score

def print_dice(dice):
    print("Dice:", dice)

def print_score(score):
    print("Score:", score)

def play_game():
    print("Welcome to Yacht!")

    dice = roll_dice()
    print_dice(dice)

    score = score_dice(dice)
    print_score(score)

play_game()
