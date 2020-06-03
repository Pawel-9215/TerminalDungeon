# This module will be responsible for rendering stuff and gathering player input

import curses
from math import floor
import ui
import engine


class Renderque():
    # Only one Scene can be rendered at a time.
    # Scene object already have all references of renderable objects within

    def __init__(self, engine: engine.Engine):
        self.scene = engine.current_scene

    def renderpass(self):
        # this func update screens and draws all objects from que
        for screen in self.scene.windows:
            screen.clear()
            screen.border()
            screen.refresh()
        #print(self.scene.renderable_objects)
        for obj in self.scene.renderable_objects:
            obj.draw()
            pass
        for screen in self.scene.windows:
            screen.refresh()

    def clearscene(self):
        if self.scene != None:
            for screen in self.scene.windows:
                screen.clear()


class Updateque():
    # Same as render but is updating (for example positions) instead of rendering


    def __init__(self, engine: engine.Engine):
        self.scene = engine.current_scene

    def updatepass(self, key):
        for obj in self.scene.updatable_objects:
            obj.update(key)


class Keyboard():
    # this is keyboard controller
    # Idea is to send key presses to objects currenty focused objects
    # We can also edit key mapping here
    last_pressed = ""

    def __init__(self, engine: engine.Engine):
        self.scene = engine.current_scene

    def key_listen(self):
        key_pressed = self.scene.input_window.getch()
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
        self.name = name
        self.scene_label = ui.Label(windows[0], name, 0, 0)
        self.renderable_objects.append(self.scene_label)





