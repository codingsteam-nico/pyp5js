from processing import *
import random


positions = []
velocities = []
accelerations = []

gravity = createVector()
center = createVector()
mouse = createVector()

dampening = 0.2
sound = None


def preload():
    global sound
    sound = loadSound("impactWood_light_000.ogg")


def setup():
    sound.setVolume(0.2)
    createCanvas(windowWidth, windowHeight)

    gravity.set(0, 0.3)
    center.set(windowWidth / 2, windowHeight / 2)
    mouse.set(center)

    strokeWeight(4)
    stroke(255, 125, 0)
    fill(255, 125, 0, 100)
    
    for index in range(20):
        position = createVector(
            random.randint(15, windowWidth - 15),
            random.randint(15, windowHeight - 15)
        )
        velocity = createVector(
            random.randint(-4, 4),
            random.randint(-4, 4)
        )
        acceleration = createVector(0, 0)
        
        positions.append(position)
        velocities.append(velocity)
        accelerations.append(acceleration)


def draw():
    global gravity
    background(32)
    line(center.x, center.y, mouse.x, mouse.y)

    distance = window.p5.Vector.sub(mouse, center)
    direction = distance.heading()
    
    # gravity.setHeading(direction)
    gravity = window.p5.Vector.fromAngle(direction)
    gravity.setMag(distance.mag() / 500)

    for index in range(20):
        position = positions[index]
        velocity = velocities[index]
        acceleration = accelerations[index]

        acceleration.add(gravity)
        velocity.add(gravity)
        position.add(velocity)

        if position.x < 15 or position.x > sketch.width - 15:
            position.x = constrain(position.x, 15, sketch.width - 15)
            velocity.x = velocity.x * (-1 + dampening * random.uniform(0.90, 1))
            acceleration.x = acceleration.x * (-1 + dampening * random.uniform(0.95, 1))
            # sound.play()
            
        if position.y < 15 or position.y > sketch.height - 15:
            position.y = constrain(position.y, 15, sketch.height - 15)
            velocity.y = velocity.y * (-1 + dampening * random.uniform(0.95, 1))
            acceleration.y = acceleration.y * (-1 + dampening * random.uniform(0.95, 1))
            # sound.play()
        
        circle(position.x, position.y, 15)



def mouseMoved():
    mouse.set(sketch.mouseX, sketch.mouseY)

def mousePressed():
    # print(sound)
    # sound.stopAll()
    if sketch.isLooping:
        noLoop()
    else:
        loop()