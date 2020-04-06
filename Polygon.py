from numpy.random import randint

from Point import Point
from Settings import get_settings
from utils import sample_probability


class Polygon:
    """
    Class representing a polygon in a drawing.
    """

    def __init__(self, points, fill):
        """
        Initializes an instance.
        :param points: the points of the polygons
        :param fill: the fill color in rgba.
        """
        self.points = points
        self.fill = fill

    def draw(self, image_draw):
        """
        Draws this polygon on the surface.
        :param image_draw: the image to draw on.
        :return: None
        """
        image_draw.polygon([(p.x, p.y) for p in self.points], self.fill)

    def mutate_color_red(self):
        self.fill = (randint(0, 255), self.fill[1], self.fill[2], self.fill[3])

    def mutate_color_green(self):
        self.fill = (self.fill[0], randint(0, 255), self.fill[2], self.fill[3])

    def mutate_color_blue(self):
        self.fill = (self.fill[0], self.fill[1], randint(0, 255), self.fill[3])

    def mutate_alpha(self):
        self.fill = (self.fill[0], self.fill[1], self.fill[2], randint(30, 60))

    def add_point(self):
        if len(self.points) < get_settings().get("max_polygon_points"):
            self.points.append(
                Point(randint(0, get_settings()["image_size"][0]), randint(0, get_settings()["image_size"][1])))

    def remove_point(self):
        if len(self.points) > 3:
            self.points.pop()

    def mutate(self):
        """
        Mutates this instance in-place.
        :return: None.
        """
        if sample_probability(get_settings().get("polygon_add_point_mutation_rate")):
            self.add_point()
        if sample_probability(get_settings().get("polygon_remove_point_mutation_rate")):
            self.remove_point()
        if sample_probability(get_settings().get("polygon_color_mutation_rate")):
            self.mutate_color_red()
        if sample_probability(get_settings().get("polygon_color_mutation_rate")):
            self.mutate_color_green()
        if sample_probability(get_settings().get("polygon_color_mutation_rate")):
            self.mutate_color_blue()
        if sample_probability(get_settings().get("polygon_color_mutation_rate")):
            self.mutate_alpha()
        for point in self.points:
            point.mutate()

    def copy(self):
        return Polygon([Point(p.x, p.y) for p in self.points], self.fill)

    @staticmethod
    def create_random():
        """
        Creates a random polygon.
        :return: None.
        """
        point_amount = randint(0, get_settings()["max_polygon_points"])
        points = []
        fill = (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

        for i in range(point_amount):
            points.append(
                Point(randint(0, get_settings()["image_size"][0]), randint(0, get_settings()["image_size"][1])))
        return Polygon(points, fill)
