from typing import List
from io import StringIO

from player import Player


class Suffix:
    def __init__(self):
        self._fd = StringIO()

    def run(self, players: List[Player], m_i_s: bool):
        self._fd.write("//Writing Suffix\n")
        p1 = players[0]
        p2 = players[1]
        for i, p1c in enumerate(p1.composition):
            for j, p2c in enumerate(p2.composition):
                actor = f"p{p1.pid}c{i+1}"
                target = f"p{p2.pid}c{j+1}"

                action_label = f"\t[{actor}_{target}]\t"
                attack_state = "?"
                action_string = action_label + f"attack = {attack_state}"
                self._fd.write(action_string + "\n")

        self._fd.write('label \"p1_wins\" = (p1c1 > 0 | p1c2 > 0) & p2c1 < 1 & p2c2 < 1;\n')
        self._fd.write('label \"p2_wins\" = (p2c1 > 0 | p2c2 > 0) & p1c1 < 1 & p1c2 < 1;\n')
        self._fd.write("formula health_ceiling \t= max(Knight_health, Archer_health, Wizard_health);\n")
        self._fd.write("formula health_floor \t= 1 - max(Knight_damage, Archer_damage, Wizard_damage);\n")

        self._fd.seek(0)
        result = self._fd.read()
        self._fd.close()
        return result


