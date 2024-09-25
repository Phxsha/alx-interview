#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    grid: list of list of integers (0: water, 1: land)
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the up cell
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the down cell
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left cell
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right cell
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
