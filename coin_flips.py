# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    one_flip = []
    coin_flips()
    # 1 flip there will be be two possibilities
    

# print(coinFlips(1)) 
# => [h, t]
# print(coinFlips(2)) 
# => ["HH", "HT", "TH", "TT"]
# print(coinFlips(4))
# => ['HHHH', 'HHTT', 'TTHH', 'TTTT', 'HTHT', 'THTH']
# => ['HHHHH', 'TTTTT', 'HTHTH', 'THTHT']
# takes an integer n
# we have to tell it what is heads and what is tails