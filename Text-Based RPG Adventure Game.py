import random
def creathero(hero):
    level = 1
    match hero:
        case "warrior":
            return {"name": "Warrior", "health": 100, "attack": 15, "defense": 10, "level": level, "gold": 2}
        case "mage":
            return {"name": "Mage", "health": 70, "attack": 25, "defense": 5, "level": level, "gold": 2}
        case "rogue":
            return {"name": "Rogue", "health": 80, "attack": 12, "defense": 8, "level": level, "gold": 2}   
        case _:
            return {"name": hero, "health": 50, "attack": 10, "defense": 5, "level": level}


def displayStats(hero):
    print("-" * 40)
    print(f"Hero: {hero['name']},\nLevel: {hero['level']},\nHealth: {hero['health']},\nAttack: {hero['attack']},\nDefense: {hero['defense']},\nGold: {hero['gold']}")
    print("-" * 40)

def creatmonster():
    encounter =random.choice(["troll","pheonix","oger"])
    match encounter:
        case "troll":
            return{
                "monster name": "Troll", "health": 60, "attack": 10, "defense": 8
            }
        case "pheonix":
            return{"monster name": "Pheonix", "health": 100, "attack": 20, "defense": 10}
        case "oger":
            return{
                "monster name": "Oger", "health": 80, "attack":15 , "defense": 8
            }
        
def explor(hero):
    encounter = random.choice(["monster", "treasure", "nothing"])

    match encounter:
        case "monster":
            print("You encountered a monster!")
            monster=creatmonster()
            battle(monster,hero)
        case "treasure":
            print("You found a treasure chest!")
            return openTreasure(hero)
        case "nothing":
            print("Nothing happened. You continue exploring...")


def battle(monster,hero):
    print(f"You are battling a {monster['monster name']}!")
    while True:
        print(f"the {hero['name']} attacks the {monster['monster name']} for {hero['attack']} damage!")
        monster["health"] -= hero["attack"] - monster["defense"]
        print(f"the {monster['monster name']} attacks the {hero['name']} for {monster['attack']} damage!")
        hero["health"] -= monster["attack"] - hero["defense"]
        if hero["health"] <= 0:
            print(f"The {hero['name']} has been defeated!")
            goldsystem(hero)    
            if checkgameover(hero):
                print("You have been defeated. Game Over.")
                break
            
            
        else:
            print(f"The {monster['monster name']} has been defeated!")
            hero["health"] +=50
            hero["gold"] += 1
            checklevelup(hero)
            break
            

def checkdefeat(hero):
    return hero["health"] <= 0

def checklevelup(hero):
    if hero["health"] > 100:
        hero["level"] += 1
        hero["attack"] += 5
        hero["defense"] += 5

def checkgameover(hero):
    return hero["health"] <= 0 and hero["gold"] <= 0

def goldsystem(hero):
    if hero["gold"] >=1:
        print("You have enough gold to buy a health potion!")
        interaction = input("Do you want to buy a health potion for 1 gold? (yes/no): ")
        if interaction.lower() == "yes":
            hero["gold"] -= 1
            hero["health"] += 25
            print("You bought a health potion and restored 25 health!")
    else:
        print("You don't have enough gold to buy a health potion.")

def openTreasure(hero):
    treasure=random.choice(["gold", "health potion","artifact"])
    match treasure:
        case "gold":
            print("You found 2 gold coins!")
            hero["gold"] += 2
        case "health potion":
            print("You found a health potion and gained 20 health!")
            hero["health"] += 20
        case "artifact":
            print("You found a mysterious artifact!")
        case _:
            print("The treasure chest was empty.") 
    return treasure
def main():
    print("Welcome to the Text-Based RPG Adventure Game!")
    hero_name = input("Enter your hero's name: ")
    hero_class = input("Choose your hero class (Warrior, Mage, Rogue): ")
    hero = creathero(hero_class.lower())
    print("-" * 40)
    print(f"Welcome, {hero_name} the {hero['name']}! Your adventure begins now.")
    displayStats(hero)
    while True:
        action= input("1: Explore\n2: View Stats\n3: Exit Game\nChoose an action: ")
        match action:
            case "1":
                if explor(hero) == "artifact":
                    print("Congratulations!")
                    break
                else:displayStats(hero)
            case "2":
                displayStats(hero)
            case "3":
                print("Thanks for playing! Goodbye!")
                break
            case _:
                print("Invalid action. Please choose a valid option.")

main()