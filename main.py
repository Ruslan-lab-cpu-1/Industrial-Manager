# Variables
iron_ore = 0
iron = 0
smelted_iron = 0
smelted_copper = 0
copper_ore = 0
copper = 0
iron_mine = 100
copper_mine = 100
diesel = 100.0
wood = 0
forest = 100
materials1 = 100
materials2 = 10
blasts = 0
smelters = 0
coal = 0
coal_makers = 0
assemblers = 0

# Tasks
def mine_copper(amount):
    global copper_ore
    global copper_mine
    if copper_mine < amount:
        print(f"Cannot mine {amount} of copper. You can mine maximum {iron_mine} copper ore")
    else:
        copper_mine -= amount
        copper_ore += amount

def mine_iron(amount):
    global iron_ore
    global iron_mine
    if iron_mine < amount:
        print(f"Cannot mine {amount} of iron. You can mine maximum {iron_mine} iron ore")
    else:
        iron_mine -= amount
        iron_ore += amount

def cut_wood(amount):
    global wood
    global forest
    if forest < amount:
        print(f"Cannot mine {amount} of wood. You can cut maximum {forest} wood")
    else:
        forest -= amount
        wood += amount

def build_tier1(building):
    global materials1
    global coal_makers
    global smelters
    global blasts
    global assemblers
    min_for_blast = 15
    min_for_smelter = 15
    min_for_coaler = 10
    min_for_assembler = 10
    if building == "coal maker":
        if materials1 < min_for_coaler:
            print(f"Not enough materials I. Need 10, you have {materials1}.")
        else:
            materials1 -= min_for_coaler
            coal_makers += 1
            print("Building constructed.")

    elif building == "smelter":
        if materials1 < min_for_smelter:
            print(f"Not enough materials I. Need 15, you have {materials1}.")
        else:
            materials1 -= min_for_smelter
            smelters += 1
            print("Building constructed.")

    elif building == "blast furnace":
        if materials1 < min_for_blast:
            print(f"Not enough materials I. Need 15, you have {materials1}.")
        else:
            materials1 -= min_for_blast
            blasts += 1
            print("Building constructed.")

    elif building == "assembly i":
        if materials1 < min_for_assembler:
            print(f"Not enough materials I. Need 10, you have {materials1}.")
        else:
            materials1 -= min_for_assembler
            assemblers += 1
            print("Building constructed.")

    else:
        print(f"No building like {building}")

def operation():
    global wood
    global coal
    global coal_makers
    global smelted_iron
    global smelted_copper
    global smelters
    global assemblers
    global blasts
    global iron
    global copper
    global copper_ore
    global iron_ore
    global assemblers
    global materials1
    task_ = input("1. Make coal\n2. Cast iron\n3. Cast copper\n4. Make Materials I\n\nEnter task: ")
    if task_ == "1":
        if coal_makers < 1:
            print("Need at least 1 coal maker for making coal.")
        else:
            if wood < coal_makers * 10:
                print("Cannot make coal. Need (coal makers * 10) wood.")
            else:
                wood -= 10 * coal_makers
                coal += 10 * coal_makers
    if task_ == "2":
        if smelters < 1 and blasts < 1:
            print("Need at least 1 smelter and blast furnace for casting metal.")
        else:
            if iron_ore < (smelters + blasts) * 10:
                print("Cannot make iron. Need ((smelters + blast furnaces) * 10) iron ore.")
            else:
                iron_ore -= 10 * (smelters + blasts)
                iron += 10 * (smelters + blasts)
    if task_ == "3":
        if smelters < 1 and blasts < 1:
            print("Need at least 1 smelter and blast furnace for casting metal.")
        else:
            if copper_ore < (smelters + blasts) * 10:
                print("Cannot make copper. Need ((smelters + blast furnaces) * 10) copper ore.")
            else:
                copper_ore -= 10 * coal_makers
                copper += 10 * coal_makers
    if task_ == "4":
        if smelters < 1 and blasts < 1:
            print("Need at least 1 assembly I for making Materials I.")
        else:
            if iron < assemblers * 10 and wood < assemblers * 5:
                print("Cannot Materials I. Need (assembly I * 10) iron and (assembly I * 5) wood.")
            else:
                iron -= 10 * assemblers
                wood -= 5 * assemblers
                materials1 += 10 * assemblers

def show_resources():
    print("Iron mine:", iron_mine)
    print()
    print("Copper mine:", copper_mine)
    print()
    print("Forest: ", forest)
    print()
    print("Iron ore:", iron_ore)
    print()
    print("Copper ore:", copper_ore)
    print()
    print("Iron:", iron)
    print()
    print("Copper:", copper)
    print()
    print("Diesel:", diesel)
    print()
    print("Materials I:", materials1)
    print()
    print("Materials II:", materials2)
    print()
    print("Wood:", wood)
    print()
    print("Coal:", coal)
    print()
    print("Blast furnaces:", blasts)
    print()
    print("Smelters:", smelters)
    print()
    print("Coal maker:", coal_makers)
    print()
    print("Assembly I:", assemblers)
    print("\n\n")

# Game
while 1:
    show_resources()
    task = input("1. Mine copper\n2. Mine iron\n3. Build\n4. Cut wood\n5. Operation\n6. Exit\n\nEnter task: ")
    if task == "1":
        try:
            amount_ = int(input("Enter amount: "))
        except ValueError:
            print("Enter number!")
        else:
            mine_copper(amount_)

    elif task == "2":
        try:
            amount_ = int(input("Enter amount: "))
        except ValueError:
            print("Enter number!")
        else:
            mine_iron(amount_)

    elif task == "3":
        construction = input("Coal maker\nBlast furnace\nSmelter\nAssembly I\n\nEnter name of building: ").lower()
        build_tier1(construction)

    elif task == "4":
        try:
            amount_ = int(input("Enter amount: "))
        except ValueError:
            print("Enter number!")
        else:
            cut_wood(amount_)

    elif task == "5":
        operation()

    elif task == "6":
        exit("Exited")
