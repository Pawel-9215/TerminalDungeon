"""This module will be responsible for rendering stuff and gathering player input"""

# import curses
# from math import floor
import ui
import pickle


class Renderque:
    """This class is responsible for drawing objects in current scene
    """

    # Only one Scene can be rendered at a time.
    # Scene object already have all references of rendered objects within

    def __init__(self, engine: object):
        self.engine = engine

    def renderpass(self):
        """This method gathers updates all windows in use by current scene
        """
        scene = self.engine.current_scene
        # this func update screens and draws all objects from que
        for screen in scene.windows:
            screen.clear()
            screen.border()
            screen.refresh()

        for obj in scene.renderable_objects:
            obj.draw()

        for screen in scene.windows:
            screen.refresh()

    def clearscene(self):
        """This methods clears all windows used by current scene
        """
        scene = self.engine.current_scene
        if scene is not None:
            for screen in scene.windows:
                screen.clear()


class Updateque:
    """This class is responsible for updating all objects in current scene
    """

    # Same as render but is updating (for example positions) instead of rendering

    def __init__(self, engine: object):
        self.engine = engine

    def updatepass(self, key):
        """this methods runs update method in all updatable objects of a scene

        Args:
            key ([string]): [this is key returned by Keyboard class]
        """
        scene = self.engine.current_scene
        for obj in scene.updatable_objects:
            obj.update(key)

        for obj in scene.secondary_update:
            obj.update(key)


class Keyboard:
    """ # this is keyboard controller
        # Idea is to send key presses to objects currenty focused objects
        # We can also edit key mapping here
    """
    last_pressed = ""

    def __init__(self, engine: object):
        self.engine = engine

    def key_listen(self):
        """wait for key press and return what was pressed
        """
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
        elif symbol == "q":
            quit()
        else:
            self.last_pressed = symbol


class Characters:
    def __init__(self):
        self.characters = None
        self.load_characters()

    def load_characters(self):
        try:
            characters = pickle.load(open("resources/char", "rb"))
        except:
            characters = {"No characters": {"name": "No characters"}}

        self.characters = characters


class Scene:
    """Base Scene class. Most stuff in game is going to be some sort of scene
    """

    def __init__(self, windows, name: str, engine: object):
        self.windows = windows
        self.input_window = windows[-1]
        self.engine = engine
        self.win_y, self.win_x = self.windows[0].getmaxyx()
        self.renderable_objects = []
        self.updatable_objects = []
        self.name = name  # debug only?
        self.scene_label = ui.Label(windows[0], name, 0, 0)
        self.renderable_objects.append(self.scene_label)
        self.focused_item = 0
        self.menu_buttons = []
        self.secondary_update = []

    def button_toggle(self, key: object):

        if key == "down":
            if self.focused_item + 1 > len(self.menu_buttons) - 1:
                self.focused_item = 0
            else:
                self.focused_item += 1

        if key == "up":
            if self.focused_item - 1 < 0:
                self.focused_item = len(self.menu_buttons) - 1
            else:
                self.focused_item -= 1

        if key == " ":
            self.menu_buttons[self.focused_item].on_pressed()

        for key in self.menu_buttons:
            key.is_focused = False
        self.menu_buttons[self.focused_item].is_focused = True
