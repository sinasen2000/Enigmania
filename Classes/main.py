from Classes.game import Person, colors
from Classes.magic import Magic
from Classes.item import Item

print("\n\n")
print("NAME                       HP                            MP")
print("                 ------------------------        ----------")
print(colors.bold + "Matrushka:      " + colors.okgreen+ "|████████████████████████|      " + colors.end + colors.bold+ colors.okblue+ "|██████████|"+ colors.end)

print("\n\n")

stun = Magic("Stun", 5, 15, "black")
meteor = Magic("Meteor", 20, 55, "black")
hypnosis = Magic("Hypnosis", 10, 35, "black")
super_punch = Magic("SuperPunch", 5, 25, "black")
element_bending = Magic("ElementBending", 40, 100, "black")
cure = Magic("Cure", 15, 100, "white")
super_cure = Magic("Super_Cure", 30, 300, "white")

potion = Item("Potion", "potion", "heals 50 HP", 50)
super_potion = Item("Super Potion", "potion", "heals 250 HP", 250)
elixir = Item("Elixir", "elixir", "refills the all HP", 9999)

shotgun = Item("Shotgun", "attack", "300 damage", 300)

player_magics = [stun, meteor, hypnosis, super_punch, element_bending, cure, super_cure]
player_items = [{"item": potion, "quantity": 5}, {"item": super_potion, "quantity": 5}, {"item": elixir, "quantity": 5}, {"item": shotgun, "quantity": 5}]

enemy_magics = [stun, meteor, hypnosis, super_punch, element_bending]
player = Person(500, 100, 40, 30, player_magics, player_items)
enemy = Person(1500, 100, 40, 30, enemy_magics, [])


res = True
i = 0

print(colors.failure + colors.bold + "Welcome to the fight!" + colors.end)

while res:
    print("======================")
    player.select_action()
    choice = input("Choose action: (Type 1 or 2)(or 0 when you want to go to go back.)")
    index = int(choice) - 1

    if index == 0:
        dmg = player.damage_generator()
        enemy.damage_intake(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        choice2 = int(input("Choose a magic type to perform: (Type the number)(or 0 if you want to go back)")) - 1
        if choice2 == -1:
            continue
        magic_power = player.magic[choice2]
        magic_dmg = magic_power.generate_damage()
        current_mp = player.get_mp()

        if magic_power.cost > current_mp:
            print(colors.failure + "\nNot enough Magic Points\n" + colors.end)
            continue

        player.reduce_mp(magic_power.cost)

        if magic_power.type == "white":
            player.heal(magic_dmg)
            print(colors.okblue + "\n" + magic_power.name + " heals for " + str(magic_dmg) + " HP." + colors.end)
        elif magic_power.type == "black":
            enemy.damage_intake(magic_dmg)
            print(colors.okblue + "\n" + magic_power.name + " gives the enemy ", magic_dmg, "amount of damage.")
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: (Type the number)(or 0 if you want to go back)")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(colors.failure + "\n" + "None Left!" + colors.end)

        player.items[item_choice]["quantity"] -= 1



        if item.type == "potion":
            player.heal(item.property)
            print(colors.okgreen + "\n" + item.name + ": heals for " + str(item.property) + " HP", "Current HP:", str(player.hp) +"/"+ str(player.maxhp) + colors.end)
        elif item.type == "elixir":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(item.name, "fully restored your HP/MP.", "Your HP: ", str(player.hp) + ",", " Your MP:", str(player.mp), "Your HP:", str(player.hp) +"/"+ str(player.maxhp))
        elif item.type == "attack":
            enemy.damage_intake(item.property)
            print(colors.failure + "You attacked the enemy with", item.name, "for:", str(item.property),  "HP." + colors.end)

    enemy_choice = 1
    enemy_dmg = enemy.damage_generator()
    player.damage_intake(enemy_dmg)
    print("Enemy attacked you for", enemy_dmg, "points of damage.")

    print("###################")
    print("Enemy Health:", colors.failure + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + colors.end)
    print("Your Health:", colors.okgreen + str(player.get_hp()) + "/" + str(player.get_max_hp()) + colors.end)
    print("Your Magic Points:", colors.okblue + str(player.get_mp()) + "/" + str(player.get_max_mp()) + colors.end)

    if enemy.get_hp() == 0:
        print(colors.okgreen + "You win!" + colors.end)
        res = False
    elif player.get_hp() == 0:
        print(colors.failure + "You died! Enemy won!" + colors.end)






