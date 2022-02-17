from io import StringIO
from player import Player


class FreeStrategy:
    def __init__(self):
        pass

    def run(self, player: Player, opponent: Player):
        strategy = StringIO()
        strategy.write("//Writing FreeStrategy\n")

        action_num = 5
        if player.pid is 1:
            action_num = 1

        stun_string = f"(p{player.pid}_stun' = 0);"
        print(f"Starting loop, should be {len(player.composition)} elements")
        for i, character in enumerate(player.composition):
            print("Player: ", i, character.name)
            prefix_string = f"\tattack = 0 & turn = {player.pid} & p{player.pid}c{i+1}"
            prefix_string += f" > 0 & p{player.pid}_stun != {i+1} & "

            # If the 2nd character is an Archer?

            if i == 1 and character.name == "Archer":
                print("Entered")
                label = f"\t[p{player.pid}_turn_{action_num}]"
                prefix_string += f"\t(p{3-player.pid}c1 > 0 | p{3-player.pid}c2 > 0) -> (attack' = {action_num}) & "

                # Write
                strategy.write(label + prefix_string + stun_string + "\n")
                action_num += 2

            # If it isnt an archer
            else:
                for j, _character in enumerate(opponent.composition):
                    label = f"\t[p{player.pid}_turn_{action_num}]"
                    _string = label + prefix_string
                    _string += f"p{3-player.pid}c{j+1} > 0 -> (attack' = {action_num}) & "
                    strategy.write(_string + stun_string + "\n")
                    action_num += 1
        skip_action = f"\t[p{player.pid}_turn_skip]\tattack = 0 & turn = {player.pid} & ( (p{player.pid}_stun = 1 "
        skip_action += f"& p{player.pid}c2 < 1) | (p{player.pid}_stun = 2 & p{player.pid}c1 < 1) ) -> (attack' = 9) & "
        strategy.write(skip_action + stun_string + "\n")

        strategy.seek(0)
        result = strategy.read()
        strategy.close()
        return result
