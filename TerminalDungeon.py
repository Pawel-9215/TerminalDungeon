# This is main application body
import curses
import splash_screen
import ui
import game_control
import main_menu
from curses import wrapper
from math import floor


def main(wholescr):
    curses.curs_set(0)
    wholescr_y, wholescr_x = wholescr.getmaxyx()
    wholescr.addstr(int(wholescr_y / 2), int(wholescr_x / 2), "".join([str(wholescr_y), " ", str(wholescr_x)]))
    wholescr.refresh()
    curses.napms(300)
    splash_screen.print_splash(wholescr_y, wholescr_x)
    curses.napms(200)

    ui_screen = curses.newwin(wholescr_y, floor(wholescr_x / 3), 0, 0)
    ui_screen_maxy, ui_screen_maxx = ui_screen.getmaxyx()
    ui_screen.border()
    ui_screen.refresh()

    # test git integration

    wholescr.clear()
    label1 = ui.Label(wholescr, "This is LABEL-1", 5, 5)
    label2 = ui.Label(wholescr, "This is LABEL-2", 6, 5)
    label1.draw()
    wholescr.refresh()
    curses.napms(1000)
    wholescr.clear()
    label2.draw()
    wholescr.refresh()
    curses.napms(1000)

    game_map = curses.newwin(wholescr_y, wholescr_x - ui_screen_maxx, 0, ui_screen_maxx)
    game_map_maxy, game_map_maxx = game_map.getmaxyx()
    game_map.border()
    game_map.refresh()

    render = game_control.Renderque()
    update = game_control.Updateque()
    input_control = game_control.Keyboard()

    manager = game_control.Scene_Manager(render, update)
    manager.input_controller = input_control

    menu = main_menu.Mainmenu([wholescr], wholescr, manager)
    menu.draw_item_list()
    credits1 = main_menu.Credits([wholescr], wholescr, manager)
    credits1.print_content()
    # Game conrol classes

    colors = ui.ColorInit()

    render.scene = credits1
    # update.updatepass("up")
    render.renderpass()

    curses.napms(2000)


"""
    wholescr.clear()
    #manager.change_scene(menu)
    curses.napms(2000)
    wholescr.clear()
    manager.change_scene(credits1)
    
    curses.napms(2000)
    wholescr.clear()
    """
"""
    while True:
        manager.input_controller.key_listen()
        manager.updater.updatepass(input_control.last_pressed)
        manager.renderer.renderpass()
"""

wrapper(main)
