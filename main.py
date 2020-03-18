from display import *
from draw import *
from parse import *
from matrix import *
import math

screen = new_screen()
color = [255,215,0]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )