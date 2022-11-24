import functools

import processing
import main


structure_methods = [
    "preload",
    "setup",
    # "draw"
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
    processing.sketch.draw = main.draw
    processing.sketch.setup()
    

if hasattr(main, "preload"):
    processing.sketch.preload()
    processing.window.Promise.all(processing.preloaded_resources).then(
        run_sketch)

else:
    run_sketch()
