from io import StringIO
from main import PLAYER_COUNT


class Prefix:
    def __init__(self):
        self._pd = StringIO()

    def run(self, players, is_smg, m_i_s):
        self._pd.write("//Writing prefix\n")

        # Header
        if is_smg:
            self._pd.write("smg\n")
        else:
            self._pd.write("mdp\n")

        if is_smg:

            # Write players
            for player in players:
                pa = StringIO()
                pa.write(f"player p{player.pid}\n\t")
                pa.write(" ".join(self.get_actions(player)) + "\n")
                pa.write("endplayer\n")
                pa.seek(0)
                self._pd.write(pa.read())
                pa.close()

        # write module
        self._pd.write(self.get_module(players, m_i_s))

        self._pd.seek(0)
        result = self._pd.read()
        self._pd.close()
        return result

    @staticmethod
    def get_module(players, m_i_s):
        module = StringIO()
        module.write("module game\n")
        # decision: 0 - NONE, 1 - p1c1 > p2c1, 2 - p1c1 > p2c2, 3 - p1c2 > p2c1, 4 - p1c2 > p2c2, 5 - p2c1 > p1c1,
        # 6 - p2c1 > p1c2, 7 - p2c2 > p1c1, 8 - p2c2 > p1c2, 9 - NEXT
        module.write("\tattack\t: [0..9];\n")

        # Player to act
        module.write("\tturn\t: [0..2];\n")

        # Health
        for player in players:
            for i, character in enumerate(player.composition):
                if m_i_s:
                    # pxcy
                    module.write(f"\tp{player.pid}c{i+1}\t: [health_floor..health_ceiling];\n")
                else:
                    module.write(f"\tp{player.pid}c{i+1}\t: [health_floor..health_ceiling] init {character.health};\n")

            # Stuns
            module.write(f"\tp{player.pid}_stun\t: [0..2];\n")

        # Flip coin & Next turn
        module.write(f"\t[flip_coin]\tturn = 0 -> 0.5 : (turn' = 1) + 0.5 : (turn' = 2);\n")
        module.write(f"\t[next_turn]\tattack = 9 & turn > 0 & (p1c1 > 0 | p1c2 > 0) & (p2c1 > 0 | p2c2 > 0) -> "
                     f"(attack' = 0) & (turn' = 3 - turn);\n")

        module.seek(0)
        result = module.read()
        module.close()
        return result

    def get_actions(self, player):
        if player.pid is 1:
            return self.get_actions_p1(player.composition)
        if player.pid is 2:
            return self.get_actions_p2(player.composition)

    @staticmethod
    def get_actions_p1(composition):
        actions = []
        for i, character in enumerate(composition):
            if i is 0:
                actions.append(f"[p1_turn_1], ")
                if character.name != "Archer":
                    actions.append("[p1_turn_2], ")
                actions.append("[p1_turn_3], ")
            if i is 1:
                if character.name != "Archer":
                    actions.append("[p1_turn_4], ")
                actions.append("[p1_turn_skip]")
        return actions

    @staticmethod
    def get_actions_p2(composition):
        actions = []
        for i, character in enumerate(composition):
            if i is 0:
                actions.append(f"[p2_turn_5], ")
                if character.name != "Archer":
                    actions.append("[p2_turn_6], ")
                actions.append("[p2_turn_7], ")
            if i is 1:
                if character.name != "Archer":
                    actions.append("[p2_turn_8], ")
                actions.append("[p2_turn_skip]")
        return actions








