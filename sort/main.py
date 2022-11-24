from processing import *

import random


numbers = [random.randint(1, 20) for _ in range(40)]

def setup():
    global sorter
    createCanvas(800, 400)

    noStroke()
    fill("orange")
    
    sorter = bubble_sort(numbers)


def draw():
    background(32)
    
    try:
        current = next(sorter)
    except:
        current = None
    
    for i, number in enumerate(numbers):
        x = 800 / len(numbers) * i
        if current and current == i:
            fill("cyan")
        else:
            fill("orange")
        rect(x, 400, 800 / len(numbers) - 2, -number * 20)


def bubble_sort(data):
    num_of_numbers = len(data)
    num_of_pairs = num_of_numbers - 1

    for j in range(num_of_numbers):
        for i in range(num_of_pairs - j):
            a = data[i]
            b = data[i+1]
            if a > b:
                data[i+1] = a
                data[i] = b
            yield i+1