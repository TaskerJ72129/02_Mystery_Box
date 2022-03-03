import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    prize = ""
    round_winnings = 0

    for thing in range(0, 3):

        # randint finds numbers between givin enpoints, including both endpoints
        prize_num = random.randint(1,100)
        # prize += " "
        if 0 < prize_num <= 5:
            # one in ten chance of getting gold
            # prize += "gold"
            round_winnings += 5
        elif 5 < prize_num <= 25:
            # get silver if it's a 2 or 3
            # prize += "silver"
            round_winnings += 2
        elif 25 < prize_num <= 65:
            # copper if its 4, 5, 6, 7 
            # prize += "copper"
            round_winnings += 1
        '''else prize_num == 4:
            prize += "lead"'''

    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Pay Out: ${}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead".format(winnings - cost))
else:
    print("Sorry, you lost ${}".format(cost - winnings))