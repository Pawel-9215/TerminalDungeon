# This module will be responsible for rendering stuff and gathering player input

import curses
from math import floor
import ui



class Renderque():
    # Only one Scene can be rendered at a time.
    # Scene object already have all references of renderable objects within

    def __init__(self, engine: object):
        self.engine = engine

    def renderpass(self):
        scene = self.engine.current_scene
        # this func update screens and draws all objects from que
        for screen in scene.windows:
            screen.clear()
            screen.border()
            screen.refresh()
        #print(self.scene.renderable_objects)

        for obj in scene.renderable_objects:
            obj.draw()
            pass
        for screen in scene.windows:
            screen.refresh()

    def clearscene(self):
        scene = self.engine.current_scene
        if scene != None:
            for screen in scene.windows:
                screen.clear()


class Updateque():
    # Same as render but is updating (for example positions) instead of rendering


    def __init__(self, engine: object):
        self.engine = engine

    def updatepass(self, key):
        scene = self.engine.current_scene
        for obj in scene.updatable_objects:
            obj.update(key)


class Keyboard():
    # this is keyboard controller
    # Idea is to send key presses to objects currenty focused objects
    # We can also edit key mapping here
    last_pressed = ""

    def __init__(self, engine: object):
        self.engine = engine

    def key_listen(self):
        scene = self.engine.current_scene
        key_pressed = scene.input_window.getch()
        symbol = chr(key_pressed)
        if symbol == "w":
            self.last_pressed = "up"
        elif symbol == "s":
            self.last_pressed = "down"
        elif symbol == "a":
            self.last_pressed = "left"
        elif symbol == "d":
            self.last_pressed = "right"
        else:
            self.last_pressed = symbol


class Scene():

    def __init__(self, windows, name: str, engine: object):
        self.windows = windows
        self.input_window = windows[-1]
        self.engine = engine
        self.win_y, self.win_x = self.windows[0].getmaxyx()
        self.renderable_objects = []
        self.updatable_objects = []
        self.name = name #debug only
        self.scene_label = ui.Label(windows[0], name, 0, 0)
        self.renderable_objects.append(self.scene_label)

        






