#This is main application
import curses
import splash_screen
from curses import wrapper
from math import floor


def main(wholescr):
    curses.curs_set(0)
    wholescr_y, wholescr_x = wholescr.getmaxyx()
    wholescr.addstr(int(wholescr_y/2), int(wholescr_x/2), "".join([str(wholescr_y), " ", str(wholescr_x)]))
    wholescr.refresh()
    splash_screen.print_splash(wholescr_y, wholescr_x)
    def popup(mess):
        width = len(mess)+4
        height = 3

        popup = curses.newwin(height, width, floor(wholescr_y/2)-2, floor(wholescr_x/2)-floor(width/2))
        popup.border()
        popup.addstr(1, 2, mess)
        popup.refresh()


    curses.napms(200)


    ui_screen = curses.newwin(wholescr_y, floor(wholescr_x/3), 0, 0)
    ui_screen_maxy, ui_screen_maxx = ui_screen.getmaxyx()
    ui_screen.addstr(2, 1, "".join([str(ui_screen_maxy), " ", str(ui_screen_maxx)]))
    ui_screen.border()
    ui_screen.refresh()

    


    curses.napms(200)

    game_map = curses.newwin(wholescr_y, wholescr_x-ui_screen_maxx, 0, ui_screen_maxx)
    game_map_maxy, game_map_maxx = game_map.getmaxyx()
    game_map.addstr(2, 1, "".join([str(game_map_maxy), " ", str(game_map_maxx)]))
    game_map.border()
    game_map.refresh()

    curses.napms(200)
    ui_screen.addstr(1,1, "Test UI Window")
    ui_screen.refresh()
    curses.napms(200)
    game_map.addstr(1,1, "Test game map area")
    game_map.refresh()
    curses.napms(200)
    popup("This is a test popup message")
    curses.napms(500)
    #wholescr.clear()
    
    #wholescr.refresh()
    curses.napms(3000)















wrapper(main)


