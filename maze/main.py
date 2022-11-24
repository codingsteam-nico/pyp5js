from processing import *

import random
import time

directions = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
opposite = {"up": "down", "left": "right", "down": "up", "right": "left"}


cell_size = 40
grid = []

stack = []
current = 6, 6
first = True

def setup():
    global columns, rows, maze

    size = min(windowWidth, windowHeight)
    createCanvas(size, size)
    # frameRate(10)

    columns = floor(size / cell_size)
    rows = floor(size / cell_size)
    maze = [
        [dict.fromkeys(directions, False) for _ in range(rows)] for _ in range(columns)
    ]


def draw():
    global first, current
    background(32)
    
    if stack or first:
        if first:
            first = False
        x, y = current

        unvisited = {}
        for direction, movement in directions.items():
            m_x, m_y = movement
            n_x, n_y = x + m_x, y + m_y

            if 0 <= n_x < columns and 0 <= n_y < columns and not any(maze[n_y][n_x].values()):
                unvisited[direction] = n_x, n_y
                
        if unvisited:
            stack.append(current)
            direction = random.choice(list(unvisited))
            next_cell = unvisited[direction]
            n_x, n_y = next_cell
            maze[y][x][direction] = True
            maze[n_y][n_x][opposite[direction]] = True
            current = next_cell
        else:
            current = stack.pop()

        
    for j, row in enumerate(maze):
        for i, cell in enumerate(row):
            position = i, j
            s = cell_size
            x = i * s;
            y = j * s;
            if position in stack:
                noStroke()
                fill(hue_to_rgb(stack.index(position) * 2 % 360))
                rect(x, y, s, s)
            if stack and position == current:
                noStroke()
                fill("gold")
                rect(x, y, s, s)
            if any(cell.values()):
                stroke("white")
                if not cell["up"]:
                    line(x, y, x + s, y)
                if not cell["down"]:
                    line(x, y + s, x + s, y + s)
                if not cell["left"]:
                    line(x, y, x, y + s)
                if not cell["right"]:
                    line(x + s, y, x + s, y + s)


def hue_to_rgb(hue):
    i = int(hue / 360 * (255*6))
    if i < 255*1:
        return i, 0, 255
    elif i < 255*2:
        i %= 255
        return 255, 0, 255-i
    elif i < 255*3:
        i %= 255
        return 255, i, 0
    elif i < 255*4:
        i %= 255
        return 255-i, 255, 0
    elif i < 255*5:
        i %= 255
        return 0, 255, i
    else:
        i %= 255
        return 0, 255 - i, 255
