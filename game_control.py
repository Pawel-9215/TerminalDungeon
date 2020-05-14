#This module will be responsible for rendering stuff and gathering player input

import curses
from math import floor

class Renderque():
    que = []
    screens = []
    #border = True
    
    def renderpass(self):
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
            