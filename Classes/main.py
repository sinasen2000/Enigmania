from Classes.game import Person, colors
from Classes.magic import Magic
from Classes.item import Item
import random

print("\n\n")


stun = Magic("Stun", 5, 800, "black")
meteor = Magic("Meteor", 20, 1500, "black")
hypnosis = Magic("Hypnosis", 10, 900, "black")
super_punch = Magic("SuperPunch", 5, 1000, "black")
element_bending = Magic("ElementBending", 40, 2000, "black")
cure = Magic("Cure", 15, 1000, "white")
super_cure = Magic("Super_Cure", 30, 3000, "white")

potion = Item("Potion", "potion", "heals 50 HP", 500)
super_potion = Item("Super Potion", "potion", "heals 250 HP", 2500)
elixir = Item("Elixir", "elixir", "refills the all HP", 9999)

shotgun = Item("Shotgun", "attack", "300 damage", 1500)

player_magics = [stun, meteor, hypnosis, super_punch, element_bending, cure, super_cure]
player_items = [{"item": potion, "quantity": 5}, {"item": super_potion, "quantity": 5}, {"item": elixir, "quantity": 5}, {"item": shotgun, "quantity": 5}]

enemy_magics = [stun, meteor, hypnosis, super_punch, element_bending]
player1 = Person("Manu :",  9000, 1000, 200, 30, player_magics, player_items)
player2 = Person("Zion :",  7000, 1000, 400, 30, player_magics, player_items)
player3 = Person("Jano :",  1000, 1000, 300, 30, player_magics, player_items)
enemy = Person("Ehmo :", 25000, 4800, 600, 50, enemy_magics, [])

players = [player1, player2, player3]

res = True
i = 0

print(colors.failure + colors.bold + "Welcome to the fight!" + colors.end)

while res:
    print("======================")



    for player in players:
        print("\n\n")
        print("NAME                  HP                                        MP")
        for player in players:
            player.get_info()

        print("\n")
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
        target = random.randrange(0, 2)
        enemy_dmg = enemy.damage_generator()
        players[target].damage_intake(enemy_dmg)
        print("Enemy attacked you for", enemy_dmg, "points of damage.")

        print("###################")
        print("Enemy Health:", colors.failure + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + colors.end)

    if enemy.get_hp() == 0:
        print(colors.okgreen + "You win!" + colors.end)
        res = False

    elif player.get_hp() == 0:
        print(colors.failure + "You died! Enemy won!" + colors.end)






