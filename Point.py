from functools import reduce

import numpy as np
from numpy.random import randint

from Settings import get_settings
from utils import sample_probability


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mutate(self):
        """
        Mutates this instance.
        :return: None.
        """
        if sample_probability(get_settings().get("point_move_mutation_rate")):
            self.x = randint(0, get_settings()["image_size"][0])
            self.y = randint(0, get_settings()["image_size"][1])
        if sample_probability(get_settings().get("point_move_mutation_rate")):
            self.x = max(0, min(get_settings()["image_size"][0], self.x + randint(-20, 20)))
            self.y = max(0, min(get_settings()["image_size"][1], self.y + randint(-20, 20)))
