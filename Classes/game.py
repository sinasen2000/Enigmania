import random

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
    def __init__(self, hp, mp, atk, defs, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.lowatk = atk - 10
        self.highatk = atk + 10
        self.defs = defs
        self.magic = magic
        self.actions = ["Attack", "Magic"]

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
        return self.magic[i]["name"]

    def select_action(self):
        i = 1
        print(colors.okblue + colors.bold + "Actions" + colors.end)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(colors.okblue + colors.bold + "Magic Options" + colors.end)
        for power in self.magic:
            print(str(i) + ":", power["name"], "(cost:", str(power["cost"]) + ")")
            i += 1
