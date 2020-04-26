water, milk, beans, cups, money = 400, 540, 120, 9, 550
total_list = [water, milk, beans, cups, money]


def ask(question: str):
    return input(f"{question}\n")


def listing(total):
    print("The coffee machine has:")
    print(total[0], "of water")
    print(total[1], "of milk")
    print(total[2], "of coffee beans")
    print(total[3], "of disposable cups")
    print(f"${total[4]}, of money")

def make_coffee(total,type_coffee=0):
    if type_coffee == 1 and total[0] >= 250 and

# listing()
# Меню
while True:

    action = ask("Write action (buy, fill, take, remaining, exit):")
    print()

    if action == "remaining":
        listing(total_list)

    elif action == "exit":
        break

    elif action == "fill":
        total_list[0] += int(ask("Write how many ml of water do you want to add:"))
        total_list[1] += int(ask("Write how many ml of milk do you want to add:"))
        total_list[2] += int(ask("Write how many grams of coffee beans do you want to add:"))
        total_list[3] += int(ask("Write how many disposable cups of coffee do you want to add:"))


    elif action == "take":
        print(f"I gave you ${money}")
        money = 0

    elif action == "buy":
        coffee = int(ask("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
        if coffee == 1:
            water -= 250
            beans -= 16
            money += 4
        elif coffee == 2:
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
        else:
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
        cups -= 1

    listing()
