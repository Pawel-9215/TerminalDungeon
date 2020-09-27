import game_control
import player
import ui


class CombatScreen(game_control.Scene):
    def __init__(self, windows,
                 name: str, engine: object,
                 escape,
                 current_player: player.Player,
                 current_enemy: player.Character):
        super().__init__(windows, name, engine)
        self.window_y, self.window_x = windows[0].getmaxyx()
        self.current_player = current_player
        self.current_enemy = current_enemy
        self.escape = escape
        self.player_sheet = CombatPlayerStats(windows[0], self.current_player, self)
        self.enemy_sheet = CombatEnemyStats(windows[0], self.current_enemy, self)
        self.situation_report = SitRaport(self.windows[0], self)
        self.button_names = ["Attack", "Defend", "Card 1", "Card 2", "Card 3", "End Turn"]
        self.buttons_on_pressed = {
            "Attack": [print, ["Attack"]],
            "Defend": [print, ["Defend"]],
            "Card 1": [print, ["Card 1"]],
            "Card 2": [print, ["Card 2"]],
            "Card 3": [print, ["Card 3"]],
            "End Turn": [print, ["End Turn"]],
        }

        self.draw_content()

    def draw_content(self):

        center_x = int(self.window_x / 2)
        min_y = 2

        self.updatable_objects.append(self)
        self.renderable_objects.append(self.player_sheet)
        self.renderable_objects.append(self.enemy_sheet)
        self.renderable_objects.append(self.situation_report)

        for num, button in enumerate(self.button_names):
            if button == "End Turn":
                extra = 1
            else:
                extra = 0
            self.menu_buttons.append(
                ui.button(self.windows[0],
                          min_y+num+extra,
                          center_x-int(len(button)/2),
                          button,
                          button,
                          self.buttons_on_pressed[button][0],
                          self.buttons_on_pressed[button][1])
            )
        for btn in self.menu_buttons:
            self.renderable_objects.append(btn)

        self.menu_buttons[self.focused_item].is_focused = True

    def update(self, key):
        self.button_toggle(key)
        # debug:
        if key == "l":
            self.engine.change_scene(self.escape)
        else:
            pass


class CombatPlayerStats:
    def __init__(self, window, current_player: player.Player, combat_screen: CombatScreen):
        self.window = window
        self.current_player = current_player
        self.combat_screen = combat_screen
        self.window_y, self.window_x = window.getmaxyx()
        self.current_action_points = self.current_player.action_points
        self.defences = 0

    def draw(self):
        min_y = 1
        max_y = self.window_y - 1
        min_x = 1
        max_x = self.window_x - 1
        center_y = int(self.window_y / 2)
        center_x = int(self.window_x / 2)

        current_AP_str = "AP left : ["+str(self.current_action_points)+"]"
        self.window.addstr(min_y, center_x-int(len(current_AP_str)/2), current_AP_str)

        # Name
        self.window.addstr(min_y + 1, min_x + 1, "NAME: " + self.current_player.name)

        # Parameters
        self.window.addstr(min_y + 2, min_x + 1, (
                "HEALTH: " + str(self.current_player.current_health) + "/" + str(self.current_player.health)))
        self.window.addstr(min_y + 3, min_x + 1, ("MELEE: " + str(self.current_player.melee_skill)))
        self.window.addstr(min_y + 4, min_x + 1,
                           ("AP: " + str(self.current_action_points) + "/" + str(self.current_player.action_points)))
        self.window.addstr(min_y + 5, min_x + 1, ("STRENGHT: " + str(self.current_player.strenght)))
        # endurance situation:
        if self.defences > 0:
            endurance_str = "ENDURANCE: " + str(self.current_player.endurance)+" + DEF: "+str(self.current_player.strenght)+" x "+str(self.defences)
        else:
            endurance_str = "ENDURANCE: " + str(self.current_player.endurance)
        self.window.addstr(min_y + 6, min_x + 1, endurance_str)

        # inventory
        # weapon
        armour_l1 = "HEAD: [" + str(self.current_player.arm_head) + "] TORSO: [" + str(
            self.current_player.arm_torso) + "]"
        armour_l2 = "HANDS: [" + str(self.current_player.arm_hands) + "] LEGS: [" + str(
            self.current_player.arm_legs) + "]"

        self.window.addstr(min_y + 7, min_x + 1, ("WEAPON: [" + str(self.current_player.weapon) + "]"))
        self.window.addstr(min_y + 8, min_x + 1, armour_l1)
        self.window.addstr(min_y + 9, min_x + 1, armour_l2)
        self.window.addstr(min_y + 10, min_x + 1, "DECK: [0]")
        self.window.addstr(min_y + 11, min_x + 1, "HAND: [1: Placeholder,")
        self.window.addstr(min_y + 12, min_x + 8, "2: Placeholder,")
        self.window.addstr(min_y + 13, min_x + 8, "3: Placeholder]")

    def update(self, key):
        pass


class CombatEnemyStats:
    def __init__(self, window, current_enemy: player.Character, combat_screen: CombatScreen):
        self.window = window
        self.current_enemy = current_enemy
        self.combat_screen = combat_screen
        self.window_y, self.window_x = window.getmaxyx()
        self.current_action_points = self.current_enemy.action_points

    def draw(self):
        min_y = 1
        max_y = self.window_y - 1
        min_x = 1
        max_x = self.window_x - 2
        center_y = int(self.window_y / 2)
        center_x = int(self.window_x / 2)

        # String shortcuts
        name = "NAME: " + self.current_enemy.name
        health = "HEALTH: " + str(self.current_enemy.current_health) + "/" + str(self.current_enemy.health)
        melee = "MELEE: " + str(self.current_enemy.melee_skill)
        ap = "AP: " + str(self.current_action_points) + "/" + str(self.current_enemy.action_points)
        strenght = "STRENGHT: " + str(self.current_enemy.strenght)
        endurance = "ENDURANCE: " + str(self.current_enemy.endurance)
        weapon = "WEAPON: [" + str(self.current_enemy.weapon) + "]"

        armour_l1 = "HEAD: [" + str(self.current_enemy.arm_head) + "] " + "TORSO: [" + str(
            self.current_enemy.arm_torso) + "]"
        armour_l2 = "HANDS: [" + str(self.current_enemy.arm_hands) + "] " + "LEGS: [" + str(
            self.current_enemy.arm_legs) + "]"

        self.window.addstr(min_y + 1, max_x - len(name), name)
        self.window.addstr(min_y + 2, max_x - len(health), health)
        self.window.addstr(min_y + 3, max_x - len(melee), melee)
        self.window.addstr(min_y + 4, max_x - len(ap), ap)
        self.window.addstr(min_y + 5, max_x - len(strenght), strenght)
        self.window.addstr(min_y + 6, max_x - len(endurance), endurance)
        self.window.addstr(min_y + 7, max_x - len(weapon), weapon)
        self.window.addstr(min_y + 8, max_x - len(armour_l1), armour_l1)
        self.window.addstr(min_y + 9, max_x - len(armour_l2), armour_l2)

    def update(self):
        pass

class SitRaport:
    def __init__(self, window, combat_screen: CombatScreen):
        self.window = window
        self.combat_screen = combat_screen
        self.window_y, self.window_x = window.getmaxyx()
        self.max_y = self.window_y - 2
        self.min_y = 14
        self.min_x = 1
        self.max_x = self.window_x - 1
        self.lines = {}
        self.clean_dialogue()

    def generate_line(self):
        pass

    def clean_dialogue(self):
        empty_line = "[->"+" "*(self.max_x-5)+"]"

        # calculate how many lines we have
        no_of_lines = self.max_y - self.min_y
        for i in range(no_of_lines):
            self.lines[i] = empty_line

    def draw(self):

        for line in self.lines:
            self.window.addstr(self.max_y-line, self.min_x, self.lines[line])



