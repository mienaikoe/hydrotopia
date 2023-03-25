from models.model import Model
import numpy as np


def triangle_vertices_from_indices(vertices, indices):
    triangle_vertices = [vertices[ind] for triangle in indices for ind in triangle]
    return np.array(triangle_vertices, dtype="f4")


cube_corners = [
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
]
cube_indices = [
    (0, 2, 3),
    (0, 1, 2),
    (1, 7, 2),
    (1, 6, 7),
    (6, 5, 4),
    (4, 7, 6),
    (3, 4, 5),
    (3, 5, 0),
    (3, 7, 4),
    (3, 2, 7),
    (0, 6, 1),
    (0, 5, 6),
]
cube_vertices = triangle_vertices_from_indices(cube_corners, cube_indices)
texture_corners = [(0, 0), (1, 0), (1, 1), (0, 1)]
texture_indices = [
    (0, 2, 3),
    (0, 1, 2),
    (0, 2, 3),
    (0, 1, 2),
    (0, 1, 2),
    (2, 3, 0),
    (2, 3, 0),
    (2, 0, 1),
    (0, 2, 3),
    (0, 1, 2),
    (3, 1, 2),
    (3, 0, 1),
]
texture_vertices = triangle_vertices_from_indices(texture_corners, texture_indices)


class Cube(Model):
    def get_vertex_data(self):
        return np.hstack([texture_vertices, cube_vertices])
