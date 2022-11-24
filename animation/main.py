from processing import *


def setup():
    createCanvas(windowWidth, windowHeight)
    
    fill("cyan")
    noCursor()
    noStroke()
    

def draw():
    background(32)
    distance = dist(sketch.width / 2, sketch.height / 2, sketch.mouseX, sketch.mouseY)
    size = map(abs(distance), 0, sketch.width / 2, 40, 10)
    circle(sketch.mouseX, sketch.height / 2, size)
    circle(sketch.width / 2, sketch.mouseY, size)
    