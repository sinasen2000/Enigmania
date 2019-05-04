from Classes.game import Person, colors

magic = [{"name": "Stun", "cost": 5, "damage": 15},
         {"name": "Meteor", "cost": 20, "damage": 55},
         {"name": "Hypnosis", "cost": 10, "damage": 35},
         {"name": "SuperPunch", "cost": 5, "damage": 25},
         {"name": "ElementBending", "cost": 40, "damage": 100}]
player = Person(500, 50, 40, 30, magic)
enemy = Person(700, 50, 40, 30, magic)

res = True
i = 0

print(colors.failure + colors.bold + "Welcome to the fight!" + colors.end)

while res:
    print("======================")
    player.select_action()
    choice = input("Choose action: (Type 1 or 2)")
    index = int(choice) - 1

    if index == 0:
        dmg = player.damage_generator()
        enemy.damage_intake(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        choice2 = input("Choose a magic type to perform: (Type the number)")
        index2 = int(choice2) - 1
        magic_dmg = player.superpower_generator(index2)
        magic_name = player.get_magic_name(index2)
        magic_cost = player.get_magic_cost(index2)

        current_mp = player.get_mp()

        if magic_cost > current_mp:
            print(colors.failure + "\nNot enough Magic Points\n" + colors.end)
            continue

        player.reduce_mp(magic_cost)
        enemy.damage_intake(magic_dmg)
        print(colors.okblue + "\n" + magic_name + "gives the enemy ", magic_dmg, "amount of damage.")



    enemy_choice = 1
    enemy_dmg = enemy.damage_generator()
    player.damage_intake(enemy_dmg)
    print("Enemy attacked you for", enemy_dmg, "points of damage.")

    print("###################")
    print("Enemy Health:", colors.failure + str(enemy.get_hp()) + "/" + str(player.get_max_hp()) + colors.end)
    print("Your Health:", colors.okgreen + str(player.get_hp()) + "/" + str(player.get_max_hp()) + colors.end)

    if enemy.get_hp() == 0:
        print(colors.okgreen + "You win!" + colors.end)
        res = False
    elif player.get_hp() == 0:
        print(colors.failure + "You died! Enemy won!" + colors.end)






