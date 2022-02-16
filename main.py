import sys

from config import *
from prefix import *
from player import *
from multiprocessing import Pool

PLAYER_COUNT = 2


def find_dominant_strategy():
    config_path = sys.argv[1]
    output_dest = sys.argv[2]

    config = Config(config_path, output_dest)

    for comp in config.get_compositions():
        print(f"Composition: {comp}. Generating optimal strategy...")

        # Symmetric setup of compositions
        players = []
        for i in range(PLAYER_COUNT):
            players.append(Player(i+1, comp))

        prefix = Prefix()
        result = prefix.run(players, True, True)
        config.write(result)

    config.save()


if __name__ == '__main__':
    find_dominant_strategy()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

