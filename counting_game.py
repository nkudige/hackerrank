# https://www.hackerrank.com/challenges/counter-game

powers = [2**i for i in xrange(65)]

def play_game(n, player):
#    print n
    if n == 1:
        return "Louise" if player == "Richard" else "Richard"
    global powers
    
    next_player = "Louise" if player == "Richard" else "Richard"

    if n in powers:
        return play_game(n >> 1, next_player)
    else:
        for i in xrange(65):
            if n < powers[i]:
                return play_game(n ^ powers[i-1], next_player)

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    print play_game(N, "Louise")
