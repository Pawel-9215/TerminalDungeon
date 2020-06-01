#This module will be responsible for rendering stuff and gathering player input

import curses
from math import floor

class Renderque():
	#Only one Scene can be rendered at a time.
    #Scene object already have all references of renderable objects within
    scene = None
    def __init__(self, scene=None):
        self.scene = scene
    
    def renderpass(self):
    	#this func update screens and draws all objects from que
        for screen in self.scene.windows:
            screen.clear()
            screen.border()
        for obj in self.scene.renderable_objects:
            obj.draw()
        for screen in self.scene.windows:
            screen.refresh()

class Updateque():
    #Same as render but is updating (for example positions) instead of rendering

    scene = None
    def __init__(self, scene=None):
        self.scene = scene

    def updatepass(self, key):

        for obj in self.scene.updatable_objects:
            obj.update(key)

            
            
class Keyboard():
    #this is keyboard controller
    #Idea is to send key presses to objects currenty focused objects
    #We can also edit key mapping here
    scene = None
    last_pressed = ""
    def __init__(self, scene=None):
        self.scene = scene
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
    windows = []
    renderable_objects = []
    updatable_objects = []
    input_window = None
    scene_manager = None
    keyboard_input = None

    def __init__(self, windows, input_window, scene_manager):
        self.windows = windows
        self.input_window = input_window
        self.scene_manager = scene_manager

class Scene_Manager():
    #this would be engine class
    all_scenes = []
    current_scene = None
    renderer = None
    updater = None
    input_controller = None
    fullscreen_window = None
    game_window = None
    ui_window = None
    extra_windows = []


    def __init__(self, renderer, updater):
        self.renderer = renderer
        self.updater = updater

    def change_scene(self, scene):
        self.current_scene = scene
        self.renderer.scene = scene
        self.updater.scene = scene
        self.input_controller.scene = scene
        self.renderer.renderpass()

    #you are working on scene manager system
    #update and render needs refactor as well as init screen in main module
    #think about architecture!
