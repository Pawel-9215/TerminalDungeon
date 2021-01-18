# This should be the place for deck related things from the very beginning
import ui
import player
import game_control


class DeckView(game_control.Scene):
    def __init__(self, windows, name, engine, player: player.Player, escape: game_control.Scene):
        super().__init__(windows, name, engine)
        self.current_player = player
        self.escape = escape
        self.max_y, self.max_x = self.windows[0].getmaxyx()
        self.startpos = 3
        self.description = None
        if len(self.current_player.deck) == 0:
            self.deck = ["No cards in deck"]
        else:
            self.deck = self.current_player.deck
        self.rotator = ui.Rotator(self.windows[0], self.deck, 3, int(self.max_x/2-4))
        self.buttons = {
            "↑":[self.rotator.rotate, [-1]],
            "↓":[self.rotator.rotate, [1]],
            "Destroy Card":[self.destroy_card, []],
            "Back": [self.engine.change_scene, [self.escape]],
        }
        self.print_content()

    def print_content(self):
        self.renderable_objects.append(self.rotator)
        z = self.startpos
        for i, button in enumerate(self.buttons):
            if i in [1, 2]:
                z += 1
            else:
                pass
            self.menu_buttons.append(ui.button(self.windows[0], 
                                    z,
                                    int(self.max_x/2-6),
                                    button,
                                    button,
                                    self.buttons[button][0],
                                    self.buttons[button][1]))
            z += 1
                            
        for button in self.menu_buttons:
            self.renderable_objects.append(button)
        self.menu_buttons[self.focused_item].is_focused = True
        
        self.updatable_objects.append(self)

        self.description = CardDescription(self.windows[0], z+1, 3)
        self.update_description()
        self.renderable_objects.append(self.description)
    
    def update(self, key):
        self.button_toggle(key)
        self.update_description()

    def update_description(self):
        if len(self.current_player.deck) == 0:
            self.description.set_description(["Deck is empty"])
        else:
            self.description.set_description(self.deck[self.rotator.choosen_item].print_description())

    def destroy_card(self):
        if len(self.current_player.deck) > 0:
            self.current_player.deck.pop(self.rotator.choosen_item)

        if len(self.current_player.deck) == 0:
            self.deck = ["No cards in deck"]
        else:
            self.deck = self.current_player.deck
        
        self.update_rotator()


    def update_rotator(self):
        self.rotator.items = []
        for item in self.deck:
            self.rotator.items.append(str(item))

class CardDescription():
    def __init__(self, window, y, x):
        self.window = window
        self.y = y
        self.x = x
        self.description = ["test1", "test2", "test3"]

    def set_description(self, description):
        self.description = description

    def draw(self):
        i = 0
        for item in self.description:
            if i < 8:
                self.window.addstr(self.y+i, self.x, item)
            i += 1
