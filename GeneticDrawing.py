import numpy as np
from PIL import ImageDraw, Image
from numpy.random import randint

from Settings import get_settings
from utils import sample_probability
from Polygon import Polygon


class GeneticDrawing:
    """
    This class represents a genetic drawing that is made up of polygons.
    """
    def __init__(self):
        self.polygons = []
        pass

    def draw(self, image_draw):
        """
        Draws this instance on the image.
        :param image_draw: the image draw object to draw to.
        :return: None
        """
        for poly in self.polygons:
            poly.draw(image_draw)

    def produce_image(self):
        """
        This function produces an image made based on this drawing.
        :return:
        """
        img = Image.new('RGB', get_settings()["image_size"])
        draw = ImageDraw.Draw(img, 'RGBA')
        self.draw(draw)
        return img

    def add_polygon(self):
        if len(self.polygons) < get_settings()["max_polygons"]:
            self.polygons.append(Polygon.create_random())

    def remove_polygon(self):
        if len(self.polygons) > 1:
            self.polygons.pop()

    def move_polygon_order(self):
        """
        Moves an internal polygon in the order of drawing. (changes its' z-index)
        :return:
        """
        index = randint(0, len(self.polygons))
        p = self.polygons[index]
        self.polygons.remove(p)
        self.polygons.insert(randint(0, len(self.polygons) + 1), p)

    def mutate(self):
        """
        Mutates this instance.
        :return: the offspring created by the mutation opeartion.
        """
        offspring = GeneticDrawing()
        for i in range(len(self.polygons)):
            offspring.polygons.append(self.polygons[i].copy())
            offspring.polygons[-1].mutate()
        if sample_probability(get_settings().get("drawing_add_polygon_mutation_rate")):
            offspring.add_polygon()
        if sample_probability(get_settings().get("drawing_remove_polygon_mutation_rate")):
            offspring.remove_polygon()
        if sample_probability(get_settings().get("drawing_move_polygon_mutation_rate")):
            offspring.move_polygon_order()
        return offspring

    @staticmethod
    def create_random(polygon_amount):
        """
        Generates a random drawing
        :param polygon_amount: the amount of polygons to include.
        :return: a drawing.
        """
        dna = GeneticDrawing()
        for i in range(polygon_amount):
            dna.polygons.append(Polygon.create_random())
        return dna
