# type: ignore

import functools

from browser import window


def create(sketch):
    noop = lambda: None
    create.setup = noop
    create.draw = noop

sketch = window.p5.new(create)

for attr in dir(sketch):
    globals()[attr] = getattr(sketch, attr)


def loader_promise(loader):
    @functools.wraps(loader)
    def create_loader(path):
        resource = None

        def promise(resolve, reject):
            nonlocal resource
            resource = loader(path, resolve, reject)
        preloaded_resources.append(window.Promise.new(promise))
        return resource
    return create_loader


preloaded_resources = []
loadImage = loader_promise(sketch.loadImage)
loadSound = loader_promise(sketch.loadSound)
loadFont = loader_promise(sketch.loadFont)
