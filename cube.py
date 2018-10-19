""" Consider the set of points in the unit cube that are closer to the 
middle than to any of the cube vertices.
What is the volume of this set?

Ans: 1/2"""

import math

def distance(p1, p2):
    """Returns distance between two points (tuples) in space."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

vertices = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]
mid_cube = (0.5, 0.5, 0.5)
grid_size = 50
points = [(x / grid_size, y / grid_size, z / grid_size) for x in range(grid_size+1) for y in range(grid_size+1) for z in range(grid_size+1)]
# print(points)

nbr_of_points = (grid_size + 1)**3
points_in_set = 0
for point in points:
    closer_to_vertex = 0
    for vertex in vertices:
        if distance(vertex, point) < distance(mid_cube, point):
            closer_to_vertex = 1
    if closer_to_vertex == 0:
        points_in_set += 1

print("Volume of set of points closer to mid of cube than to any vertex:", points_in_set / nbr_of_points)
            