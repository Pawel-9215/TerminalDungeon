#This module will be responsible for rendering stuff and gathering player input

import curses
from math import floor

class Renderque():
	#que is a list of all object that are to be rendered.
	#Each renderable object need to have draw() method
    que = []
    #screens is a list of current screens that need to be refreshed and updated
    screens = []
    #border = True
    
    def renderpass(self):
    	#this func update screens and draws all objects from que
        for screen in self.screens:
            screen.clear()
            screen.border()
        for obj in self.que:
            obj.draw()
        for screen in self.screens:
            screen.refresh()
            
    def addontop(self, obj):
        self.que.append(obj)
        
    def removeobj(self, obj):
        self.que.remove(obj)
        
    def setscreen(self, screen):
        self.screens.append(screen)
        
    def removescreen(self, screen):
        self.screen.remove(screen)
            