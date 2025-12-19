# game that uses microbit grid for gaming
# stuff will fall from top and we have to avoid it

import microbit as mb

def setup_grid() -> list[list[int]]:
    grid = []
    for i in range(5):
        grid.append(5*[0])
    return grid

grid = setup_grid()

grid[0][2] = 9

print(grid)

while True:
    mb.display.set_pixel(0,0,1)