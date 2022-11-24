from processing import *

notes = []

def preload():
    for octave in range(3, 6):
        for note in "cdefgab":
            note_file = "notes/" + note + str(octave) + ".mp3"
            notes.append(loadSound(note_file))


def setup():
    createCanvas(400, 400)
    print(len(notes))


def draw():
    background(0)
    for j in range(3):
        for i in range(7):
            stroke(99)
            fill(80)
            rect(i * 50, 100 + j * 50, 50, 50)


def keyPressed():
    if sketch.key.isdigit():
        note = notes[int(sketch.key) + 10]
        note.play()
        print(note.file)
    else:
        print(sketch.key)