import curses
from math import floor
splash = open("resources/misc/splash_screen", "r")


def print_splash(wholescr_y, wholescr_x):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    global splash
    logo = splash.read()
    logo_h = 8
    logo_w = 36
    """for line in splash:
        if len(line) > logo_w:
            logo_w = len(line)
        logo_h += 1"""
    
    spl_scr = curses.newwin(logo_h+2, logo_w, floor(wholescr_y/2)-5, floor(wholescr_x/2)-floor(logo_w/2))
    #spl_scr.border()
    spl_scr.addstr(0, 0, "LOADING")
    spl_scr.refresh()
    curses.napms(200)
    spl_scr.addstr(0, 0, logo, curses.color_pair(1))
    spl_scr.addstr(logo_h+1, 1, "(pre-alpha) author:Pawel Hordyniak", curses.color_pair(2))
    spl_scr.refresh()
    curses.napms(1000)