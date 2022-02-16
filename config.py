import json
from character import Character
from composition import Composition
from itertools import combinations
from io import StringIO


class Config:
    def __init__(self, config_path, output_path, composition_size=2):
        self._characters = []
        self.load_file(config_path)
        self._composition_size = composition_size
        self._output = StringIO()

    def load_file(self, file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
            for character_data in data['characters']:
                self._characters.append(Character(character_data))

    def get_compositions(self):
        compositions = []
        for comp in list(combinations(self._characters, self._composition_size)):
            compositions.append(Composition(comp))
        return compositions

    def write(self, text):
        self._output.write(text)

    def save(self):
        self._output.seek(0)
        print(self._output.read())


