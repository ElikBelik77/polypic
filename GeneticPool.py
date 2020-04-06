from PIL import ImageStat, ImageChops
from GeneticDrawing import GeneticDrawing
from utils import image_diff


class SingleChildGeneticLearner:
    """
    Class responsible for pooling and choosing best fit drawing.
    """

    def __init__(self, target_image):
        """
        Initializes this instance
        :param target_image: the image to replicate.
        """
        self.parent = GeneticDrawing.create_random(polygon_amount=1)
        self.image_size = target_image.size
        self.target_image = target_image

    def run_generation(self):
        """
        Runs a single generation.
        :return: the current best fit drawing, the fitness, the image, and whether or not the current best fit is a new best fit.
        """
        parent_img = self.parent.produce_image()
        parent_fitness = image_diff(parent_img, self.target_image)
        child = self.parent.mutate()
        child_img = child.produce_image()
        child_fitness = image_diff(child_img, self.target_image)
        if child_fitness < parent_fitness:
            self.parent = child
            return child, child_fitness, child_img, True
        return self.parent, parent_fitness, parent_img, False
