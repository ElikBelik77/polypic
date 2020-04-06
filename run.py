from PIL import Image
import argparse
from GeneticPool import SingleChildGeneticLearner
import Settings

settings = Settings.get_settings().set({
    "polygon_remove_point_mutation_rate": 1 / 150,
    "polygon_add_point_mutation_rate": 1 / 150,
    "polygon_color_mutation_rate": 1 / 70,
    "drawing_remove_polygon_mutation_rate": 1 / 150,
    "drawing_add_polygon_mutation_rate": 1 / 10,
    "drawing_move_polygon_mutation_rate": 1 / 70,
    "point_move_mutation_rate": 1 / 70,
    "max_polygons": 50,
    "max_polygon_points": 10,
    "out": "",
    "verbose": "",
    "target": "",
})
arguments_translation = {
    "prpmr": "polygon_remove_point_mutation_rate",
    "papmr": "polygon_add_point_mutation_rate",
    "pcmr": "polygon_color_mutation_rate",
    "drpmr": "drawing_remove_polygon_mutation_rate",
    "dapmr": "drawing_add_polygon_mutation_rate",
    "dmpmr": "drawing_move_polygon_mutation_rate",
    "pmr": "point_move_mutation_rate",
    "max_polygons": "max_polygons",
    "max_polygon_points": "max_polygon_points",
    "out": "out",
    "verbose": "verbose",
    "target": "target",
}
parser = argparse.ArgumentParser(
    description='Genetic algorithm that uses hill climbing to display a source image with polygons.')
parser.add_argument("--prpmr", type=float, nargs='?',
                    help='The probability of a polygon mutating and removing a point.', default=1 / 150)
parser.add_argument("--papmr", type=float, nargs='?',
                    help='The probability of a polygon mutating and adding a point.', default=1 / 150)
parser.add_argument("--pcmr", type=float, nargs='?',
                    help="The probability of a polygon mutating and changing it's color.", default=1 / 70)
parser.add_argument('--dapmr', type=float, nargs='?',
                    help='The probability of a drawing mutating and adding another polygon.', default=1 / 150)
parser.add_argument('--drpmr', type=float, nargs='?',
                    help='The probability of a drawing mutating and removing a polygon.', default=1 / 70)
parser.add_argument('--dmpmr', type=float, nargs='?',
                    help='The probability of a drawing mutating and moving a polygon in the drawing order.',
                    default=1 / 10)
parser.add_argument('--pmr', type=float, nargs='?',
                    help='The probability of a point mutation and moving in the 2d-plane.', default=1 / 70)
parser.add_argument('--max_polygons', type=int, nargs='?',
                    help='The maximum amount of polygons in a drawing.', default=50)
parser.add_argument('--max_polygon_points', type=int, nargs='?',
                    help='The maximum amount of points per polygon.', default=10)
parser.add_argument('-out', type=str, nargs='?',
                    help='The directory to output data to.', required=True)
parser.add_argument('-target', type=str, nargs='?',
                    help='The target image to replicate.', required=True)
parser.add_argument('--verbose', type=str, nargs='?',
                    help='Determines if the application runs in verbose mode.', default=False)

arguments = parser.parse_args()

for key, value in vars(arguments).items():
    if value is not None:
        Settings.get_settings().set({arguments_translation[key]: value})

target_image = Image.open(arguments.target)
Settings.get_settings().set({"image_size": target_image.size})

r = SingleChildGeneticLearner(target_image)

i = 0
have_new_offspring = False
while True:
    offspring, fitness, output, changed = r.run_generation()
    have_new_offspring = have_new_offspring or changed
    if i % 100 == 0:
        if Settings.get_settings()["verbose"]:
            print("generation ", i, "fitness", fitness)
        if have_new_offspring:
            output.save(Settings.get_settings()["out"] + str(i) + ".png")
            have_new_offspring = False
    i += 1
