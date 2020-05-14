#This is main application body
import curses
import splash_screen
import ui
import game_control
from curses import wrapper
from math import floor


def main(wholescr):
    curses.curs_set(0)
    wholescr_y, wholescr_x = wholescr.getmaxyx()
    wholescr.addstr(int(wholescr_y/2), int(wholescr_x/2), "".join([str(wholescr_y), " ", str(wholescr_x)]))
    wholescr.refresh()
    curses.napms(300)
    splash_screen.print_splash(wholescr_y, wholescr_x)
    
    curses.napms(200)


    ui_screen = curses.newwin(wholescr_y, floor(wholescr_x/3), 0, 0)
    ui_screen_maxy, ui_screen_maxx = ui_screen.getmaxyx()
    ui_screen.border()

    game_map = curses.newwin(wholescr_y, wholescr_x-ui_screen_maxx, 0, ui_screen_maxx)
    game_map_maxy, game_map_maxx = game_map.getmaxyx()
    game_map.border()

    render = game_control.Renderque()
    render.setscreen(ui_screen)
    render.setscreen(game_map)
    
    class testobj():
        pos_y = 8
        pos_x = 8
        screen = None
        content = "Fuck me, it works!"
        def __init__(self, screen):
            self.screen = screen
        def draw(self):
            self.screen.addstr(self.pos_y, self.pos_x, self.content)
            
    my_obj = testobj(game_map)
    render.addontop(my_obj)
    render.renderpass()
            
            
    
    
    curses.napms(200)
    ui.popup("This is a test popup message", wholescr_y, wholescr_x)
    curses.napms(500)
    curses.napms(3000)















wrapper(main)


