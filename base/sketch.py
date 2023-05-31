import functools

import processing
import main


structure_methods = [
    "preload",
    "setup",
    "draw"
]

event_handlers = [
    "windowResized",
    "mouseMoved",
    "mouseDragged",
    "mousePressed",
    "mouseReleased",
    "mouseClicked",
    "doubleClicked",
    "mouseWheel",
    "keyPressed",
    "keyReleased",
    "keyTyped"
]

for bindable in structure_methods + event_handlers:
    try:
        def binding():
            bind = getattr(main, bindable)
            if bindable in event_handlers:

                @functools.wraps(bind)
                def bind_wrapper(event):
                    bind()
                setattr(processing.sketch, bindable, bind_wrapper)

            else:
                setattr(processing.sketch, bindable, bind)

        binding()

    except AttributeError:
        pass


def run_sketch(*args):
    if hasattr(main, "draw"):
        processing.sketch.draw = main.draw
    if hasattr(main, "setup"):
        processing.sketch.setup()


def do_preload():
    processing.sketch.preload()
    processing.window.Promise.all(processing.preloaded_resources).then(
        run_sketch)


def main():
    if hasattr(main, "preload"):
        do_preload()
    else:
        run_sketch()


main()
