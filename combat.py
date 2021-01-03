import game_control
import player
import ui
import random
import curses
import cards


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

        # card data
        self.player_unused = self.current_player.deck.copy()
        random.shuffle(self.player_unused)
        self.player_hand = []
        self.deal_hand()
        self.player_used = []

        # mods from cards
        # each player should be able to have
        # only one mod at a time

        # player mods:
        self.player_defence_mod = 0
        self.player_attack_mod = 0
        self.player_mod_clock = 0
        self.player_poison_clock = 0

        # enemy mods:
        self.enemy_defence_mod = 0
        self.enemy_attack_mod = 0
        self.enemy_mod_clock = 0
        self.enemy_poison_clock = 0

        self.situation_report = SitRaport(self.windows[0], self)
        self.button_names = ["Attack", "Defend", "Card 1", "Card 2", "Card 3", "End Turn"]
        self.player_defences = 0
        self.enemy_defences = 0
        self.player_AP = self.current_player.action_points
        self.enemy_AP = self.current_enemy.action_points
        self.buttons_on_pressed = {
            "Attack": [self.player_attack, []],
            "Defend": [self.player_defend, []],
            "Card 1": [self.choose_card, [0]],
            "Card 2": [self.choose_card, [1]],
            "Card 3": [self.choose_card, [2]],
            "End Turn": [self.end_turn, []],
        }

        self.draw_content()

    # card possibilities:

    def heal(self, who: player.Character, points):
        # this function can be used by healing cards
        if points+who.current_health >= who.health:
            who.current_health = who.health
        else:
            who.current_health += points

    def poison(self, who: player.Character, how_long):
        # sets character in poisoned mode

        if who == self.current_player:
            self.player_poison_clock = how_long

        elif who == self.current_enemy:
            self.enemy_poison_clock = how_long

    def card_attack(self, who: player.Character, how_hard):
        # self.situation_report.generate_line("Attack was called")
        defence = who.defence_points
        blow = how_hard - defence
        if blow > 0:
            who.current_health -= blow

    def deal_hand(self):
        while len(self.player_hand) < 3 and len(self.player_unused) > 0:
            self.player_hand.append(self.player_unused.pop(0))
        else:
            return 0

    def deal_card(self, card: cards.Card, dealer: player.Character):
        card_effect = {"attack": self.card_attack,
                       "heal": self.heal,
                       "poison": self.poison}

        who = {"player": self.current_player,
                "enemy": self.current_enemy}

        # check if dealer have enough AP:

        if dealer is self.current_player:
            if self.player_AP >= card.AP_cost:
                self.player_AP -= card.AP_cost
                card_effects = card.on_deal()
                self.situation_report.generate_line(self.current_player.short_name + " is dealing " + card.name)

                for effect in card_effects:
                    card_effect[effect](who[card_effects[effect][0]], card_effects[effect][1])
                    # self.situation_report.generate_line(effect + " " + str(card_effects[effect]))
            else:
                pass
            self.check_win_condition()

    def choose_card(self, card_no):
        if len(self.player_hand) == 0:
            # card slot empty - not enough cards in hand
            self.situation_report.generate_line("Hand slot empty")
        elif len(self.player_hand) <= card_no:
            # card slot empty - not enough cards in hand
            self.situation_report.generate_line("Hand slot empty")
        else:
            self.deal_card(self.player_hand[card_no], self.current_player)
            self.player_used.append(self.player_hand.pop(card_no))

    # end of card functions

    def calculate_turn_buffs(self):
        # this function is to caluclate uffs and debuffs in between rounds
        if self.player_poison_clock > 0:
            self.current_player.current_health -= 1
            self.player_poison_clock -= 1
        if self.enemy_poison_clock > 0:
            self.current_enemy.health -= 1
            self.enemy_poison_clock -= 1
        if self.player_mod_clock > 0:
            self.player_mod_clock -= 1
        elif self.player_mod_clock == 0:
            self.player_attack_mod = 0
            self.player_defence_mod = 0
        if self.enemy_mod_clock > 0:
            self.enemy_mod_clock -= 1
        elif self.enemy_mod_clock == 0:
            self.enemy_attack_mod = 0
            self.enemy_defence_mod = 0

    def player_win(self):
        self.current_player.exp += self.current_enemy.EXP_value
        self.current_enemy.vacate_position()
        self.escape.mobs.remove(self.current_enemy)
        self.escape.updatable_objects.remove(self.current_enemy)
        self.current_enemy.remove_self()
        self.engine.change_scene(self.escape)

    def player_loose(self):
        self.situation_report.generate_line("YOU DIED!")
        self.engine.renderer.renderpass()
        curses.napms(1000)
        self.engine.change_scene(self.engine.base_menu)

    def end_turn(self):
        self.enemy_defences = 0
        self.enemy_AP = self.current_enemy.action_points
        self.enemy_turn()
        self.player_AP = self.current_player.action_points
        self.player_defences = 0
        self.calculate_turn_buffs()
        self.deal_hand()

    def enemy_turn(self):
        self.engine.renderer.renderpass()
        curses.napms(500)

        # health percentage:
        health_percent = round((self.current_enemy.current_health / self.current_enemy.health) * 100)

        # roll to check if attacks or defends
        if random.randint(1, 100) <= health_percent:
            set_to_attack = True
        else:
            set_to_attack = False

        # attack
        if set_to_attack:
            self.enemy_attack()
        elif set_to_attack is False and self.enemy_AP >= 2:
            self.enemy_defend()
        else:
            self.enemy_attack()
        if self.enemy_AP >= 1:
            self.enemy_turn()
        else:
            pass

    def player_defend(self):

        cost = 2
        if self.player_AP >= cost:
            self.player_AP -= cost
            self.player_defences += 1
            self.situation_report.generate_line(self.current_player.short_name + " is prepairing to defend.")

    def enemy_defend(self):

        cost = 2
        if self.enemy_AP >= cost:
            self.enemy_AP -= cost
            self.enemy_defences += 1
            self.situation_report.generate_line(self.current_enemy.short_name + " is prepairing to defend. ")

    def armour_check(self, character):

        if character == "enemy":
            character_armour = self.current_enemy
        elif character == "player":
            character_armour = self.current_player
        else:
            character_armour = "error"
            print("smth went wrong.")
            print("armour check is neither enemy nor player")
            quit()

        bodypart_armour = {}

        if character_armour.arm_head is None:
            bodypart_armour["head"] = 0
        else:
            bodypart_armour["head"] = character_armour.arm_head.defence_points

        if character_armour.arm_torso is None:
            bodypart_armour["torso"] = 0
        else:
            bodypart_armour["torso"] = character_armour.arm_torso.defence_points

        if character_armour.arm_hands is None:
            bodypart_armour["hands"] = 0
        else:
            bodypart_armour["hands"] = character_armour.arm_hands.defence_points

        if character_armour.arm_legs is None:
            bodypart_armour["legs"] = 0
        else:
            bodypart_armour["legs"] = character_armour.arm_legs.defence_points

        return bodypart_armour

    def player_attack(self):
        # enemy bodypart armour:
        bodypart_armour = self.armour_check("enemy")

        cost = 1
        if self.player_AP >= cost:
            self.player_AP -= cost
            # check if hit
            roll_k100 = random.randint(1, 100)
            self.situation_report.generate_line(self.current_player.short_name + " rolls k100: " + str(roll_k100))
            if roll_k100 > self.current_player.melee_skill:
                hit = False  # Miss
                text = self.current_player.short_name + " attacks and MISS! " + str(roll_k100) + ">" \
                       + str(self.current_player.melee_skill)
                self.situation_report.generate_line(text)
                body_target = "none"
            else:
                hit = True  # Hit!
                body_target = random.choice(["head", "torso", "hands", "legs"])
                text = self.current_player.short_name + " attacks and HITS his " + body_target + \
                       str(roll_k100) + "<" + str(self.current_player.melee_skill)
                self.situation_report.generate_line(text)

            if hit:
                # players attack:
                # roll D4
                roll_d4 = random.randint(1, 4)
                if self.current_player.weapon is not None:
                    attack_strengh = self.current_player.hit_points + self.current_player.weapon.weapon_attack() \
                                     + roll_d4
                else:
                    attack_strengh = self.current_player.hit_points + roll_d4
                attack_strengh += self.player_attack_mod

                # enemys defence:
                if self.enemy_defences > 0:
                    self.enemy_defences -= 1
                    enemy_defence = self.current_enemy.defence_points + round(self.current_enemy.hit_points / 2) \
                                    + bodypart_armour[body_target] + random.randint(1, 4)

                else:
                    enemy_defence = self.current_enemy.defence_points + bodypart_armour[body_target]
                enemy_defence += self.enemy_defence_mod

                text = self.current_player.short_name + " hits for: " + str(attack_strengh) + " " + \
                       self.current_enemy.short_name + " defends: " + str(enemy_defence)

                self.situation_report.generate_line(text)

                if attack_strengh - enemy_defence > 0:
                    self.current_enemy.current_health -= attack_strengh - enemy_defence
        self.check_win_condition()

    def check_win_condition(self):
        if self.current_enemy.current_health <= 0:
            self.situation_report.generate_line(self.current_enemy.short_name + " was slain")
            self.engine.renderer.renderpass()
            curses.napms(1000)
            self.player_win()

    def enemy_attack(self):
        # enemy bodypart armour:
        bodypart_armour = self.armour_check("player")

        cost = 1
        if self.enemy_AP >= cost:
            self.enemy_AP -= cost
            # check if hit
            roll_k100 = random.randint(1, 100)
            self.situation_report.generate_line(self.current_enemy.short_name + " rolls k100: " + str(roll_k100))
            if roll_k100 > self.current_enemy.melee_skill:
                hit = False  # Miss
                text = self.current_enemy.short_name + " attacks and MISS! " + \
                       str(roll_k100) + ">" + str(self.current_enemy.melee_skill)
                self.situation_report.generate_line(text)
                body_target = "None"
            else:
                hit = True  # Hit!
                body_target = random.choice(["head", "torso", "hands", "legs"])
                text = self.current_enemy.short_name + " attacks and HITS his " + body_target + \
                       str(roll_k100) + "<" + str(self.current_enemy.melee_skill)
                self.situation_report.generate_line(text)

            if hit:
                # enemys attack:
                # roll D4:
                roll_D4 = random.randint(1, 4)
                if self.current_enemy.weapon is not None:
                    attack_strengh = self.current_enemy.hit_points + self.current_enemy.weapon.weapon_attack() + roll_D4
                else:
                    attack_strengh = self.current_enemy.hit_points + roll_D4

                # players defence:
                if self.player_defences > 0:
                    self.player_defences -= 1
                    player_defence = self.current_player.defence_points + round(self.current_player.hit_points / 2) + \
                                     bodypart_armour[body_target] + random.randint(1, 4)
                else:
                    player_defence = self.current_player.defence_points + bodypart_armour[body_target]

                text = self.current_enemy.short_name + " hits for: " + str(attack_strengh) + " " + \
                       self.current_player.short_name + " defends: " + str(player_defence)

                self.situation_report.generate_line(text)

                if attack_strengh - player_defence > 0:
                    self.current_player.current_health -= attack_strengh - player_defence
        if self.current_player.current_health <= 0:
            self.player_loose()

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
                          min_y + num + extra,
                          center_x - int(len(button) / 2),
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

        current_AP_str = "AP left : [" + str(self.combat_screen.player_AP) + "]"
        self.window.addstr(min_y, center_x - int(len(current_AP_str) / 2), current_AP_str)

        # Name
        self.window.addstr(min_y + 1, min_x + 1, "NAME: " + self.current_player.name)

        # Parameters
        self.window.addstr(min_y + 2, min_x + 1, (
                "HEALTH: " + str(self.current_player.current_health) + "/" + str(self.current_player.health)))
        self.window.addstr(min_y + 3, min_x + 1, ("MELEE: " + str(self.current_player.melee_skill)))
        self.window.addstr(min_y + 4, min_x + 1,
                           ("AP: " + str(self.combat_screen.player_AP) + "/" + str(self.current_player.action_points)))
        self.window.addstr(min_y + 5, min_x + 1, ("HIT POINTS: " + str(self.current_player.hit_points)))
        # endurance situation:
        if self.combat_screen.player_defences > 0:
            endurance_str = "DEFENCE POINTS: " + \
                            str(self.current_player.defence_points) + " + " + str(
                self.combat_screen.player_defences) + "xDEF: " + \
                            str(self.current_player.hit_points)
        else:
            endurance_str = "DEFENCE: " + str(self.current_player.defence_points)
        self.window.addstr(min_y + 6, min_x + 1, endurance_str)

        # inventory
        # weapon
        armour_l1 = "HEAD: [" + str(self.current_player.arm_head) + "] TORSO: [" + str(
            self.current_player.arm_torso) + "]"
        armour_l2 = "HANDS: [" + str(self.current_player.arm_hands) + "] LEGS: [" + str(
            self.current_player.arm_legs) + "]"

        card_names = ["", "", ""]
        for i in range(3):
            if i < len(self.combat_screen.player_hand):
                card_names[i] = self.combat_screen.player_hand[i].name + "[AP:" + str(
                    self.combat_screen.player_hand[i].AP_cost) + "]"
            else:
                card_names[i] = "empty"

        self.window.addstr(min_y + 7, min_x + 1, ("WEAPON: [" + str(self.current_player.weapon) + "]"))
        self.window.addstr(min_y + 8, min_x + 1, armour_l1)
        self.window.addstr(min_y + 9, min_x + 1, armour_l2)
        deck_len = str(len(self.combat_screen.player_unused))
        cementary = str(len(self.combat_screen.player_used))
        self.window.addstr(min_y + 10, min_x + 1, "DECK: [%s/%s]" % (deck_len, cementary))
        self.window.addstr(min_y + 11, min_x + 1, "HAND: [1: " + card_names[0])
        self.window.addstr(min_y + 12, min_x + 8, "2: " + card_names[1])
        self.window.addstr(min_y + 13, min_x + 8, "3: " + card_names[2])

    def update(self, key):
        pass


class CombatEnemyStats:
    def __init__(self, window, current_enemy: player.Character, combat_screen: CombatScreen):
        self.window = window
        self.current_enemy = current_enemy
        self.combat_screen = combat_screen
        self.window_y, self.window_x = window.getmaxyx()
        self.defences = 0

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
        ap = "AP: " + str(self.combat_screen.enemy_AP) + "/" + str(self.current_enemy.action_points)
        strengh = "HIT POINTS: " + str(self.current_enemy.hit_points)
        if self.combat_screen.enemy_defences > 0:
            endurance = str(self.combat_screen.enemy_defences) + "xDEF: " + \
                        str(self.current_enemy.hit_points) + " DEFENCE POINTS: " + str(
                self.current_enemy.defence_points)
        else:
            endurance = "DEFENCE POINTS: " + str(self.current_enemy.defence_points)
        weapon = "WEAPON: [" + str(self.current_enemy.weapon) + "]"

        armour_l1 = "HEAD: [" + str(self.current_enemy.arm_head) + "] " + "TORSO: [" + str(
            self.current_enemy.arm_torso) + "]"
        armour_l2 = "HANDS: [" + str(self.current_enemy.arm_hands) + "] " + "LEGS: [" + str(
            self.current_enemy.arm_legs) + "]"

        self.window.addstr(min_y + 1, max_x - len(name), name)
        self.window.addstr(min_y + 2, max_x - len(health), health)
        self.window.addstr(min_y + 3, max_x - len(melee), melee)
        self.window.addstr(min_y + 4, max_x - len(ap), ap)
        self.window.addstr(min_y + 5, max_x - len(strengh), strengh)
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

    def generate_line(self, text):

        new_line = "[->" + text + " " * (self.max_x - 5 - len(text)) + "]"
        # cascade
        for i in range(len(self.lines) - 1, -1, -1):
            if i != 0:
                self.lines[i] = self.lines[i - 1]
            else:
                self.lines[0] = new_line

        pass

    def clean_dialogue(self):
        empty_line = "[->" + " " * (self.max_x - 5) + "]"

        # calculate how many lines we have
        no_of_lines = self.max_y - self.min_y
        for i in range(no_of_lines):
            self.lines[i] = empty_line

    def draw(self):

        for line in self.lines:
            self.window.addstr(self.max_y - line, self.min_x, self.lines[line], curses.color_pair(1))
