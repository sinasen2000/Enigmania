import random
from Classes.magic import Magic

class colors:
    top = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    failure = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underlined = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, defs, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.lowatk = atk - 10
        self.highatk = atk + 10
        self.defs = defs
        self.items = items
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]

    def damage_generator(self):
        return random.randrange(self.lowatk, self.highatk)

    def superpower_generator(self, i):
        magic_low = self.magic[i]["damage"] - 5
        magic_high = self.magic[i]["damage"] + 5
        return random.randrange(magic_low, magic_high)

    def damage_intake(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, heal_pts):
        self.hp += heal_pts
        if self.hp >= self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_magic_name(self, i):
        return self.magic[i]["name"]

    def get_magic_cost(self, i):
        return self.magic[i]["cost"]

    def select_action(self):
        i = 1
        print(colors.okblue + colors.bold + "Actions" + colors.end)
        for item in self.actions:
            print("      " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(colors.okblue + colors.bold + "Magic Options" + colors.end)
        for power in self.magic:
            print("      " + str(i) + ":",  power.name, "(cost:", str(power.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print(colors.okgreen + colors.bold + "Items: " + colors.end)
        for item in self.items:
            print("      " + str(i) + ": "+ item["item"].name, item["item"].description, "(x" + str(item["quantity"]) + ")")
            i += 1

    def get_info(self):
        hp_bar = ""
        bar_length = (self.hp / self.maxhp) * 100 / 4
        mp_bar = ""
        mp_length = (self.mp / self.maxmp) * 100 / 10
        #empty_bars =

        while bar_length > 0:
            hp_bar += "█"
            bar_length -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_length > 0:
            mp_bar += "█"
            mp_length -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string



        print("                      -------------------------                 ----------")
        print(colors.bold + self.name + "      " +
              current_hp + "|" + colors.okgreen + hp_bar +colors.end + "|"  + "      " +
              current_mp + "|" + colors.okblue + mp_bar + colors.end + "|")