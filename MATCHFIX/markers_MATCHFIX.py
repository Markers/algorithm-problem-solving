
import sys

rl = lambda : sys.stdin.readline()


def main():
    for tc in xrange(int(rl())):
        players, games = map(int, rl().rstrip().split())
        wins = [0] * players
        match = [0] * games

        for player in xrange(players):
            wins[player] = raw_input()
            print wins[player]

        for game in xrange(games):
            match[game] = map(int, rl().rstrip().split())
        print match


if __name__ == "__main__":
    main()
