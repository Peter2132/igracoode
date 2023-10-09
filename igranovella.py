import random

places = ["в лесу", "на горе", "в замке"]
weapons = ["лук", "меч", "копье", "булава", "щит"]
armors = ["Нагрудник", "Шлем","Нагрудник + шлем"]
companions = ["Пёс", "Конь", "Пума", "Орёл"]


hero = {
    "место сражения": None,
    "оружие": None,
    "броня": None,
    "компаньон": None,
    "история_действий": []
}

def choose_companion():
    while True:
        print("Выбирите компаньона")
        for i, companion in enumerate(companions, 1):
            print (f"{i}. {companion}")

        try:
            choice = int(input("Введите номер компаньона: "))
            if 1 <=choice <=len(companions):
                hero["компаньон"] =companions[choice - 1]
                break
            else:
                print("Выберите предложенного компаньона.")
        except ValueError:
            print("Ошибка. Выбирите предложенного компаньона.")

def choose_place():
    while True:
        print("Выберите место сражения")
        for i, place in enumerate(places, 1):
            print (f"{i}. {place}")
        
        try:
            choice = int(input("Введите номер места событий: "))
            if 1 <= choice <= len(armors):
                hero["место сражения"] = places[choice - 1]
                break
            else:
                print("Выберите предлеженное место.")
        except ValueError:
            print("Ошибка. Выбирите предложенные предметы.")

def choose_armor():
    while True:
        print("Выберите броню для героя:")
        for i, armor in enumerate(armors, 1):
            print(f"{i}. {armor}")

        try:
            choice = int(input("Введите номер брони: "))
            if 1 <= choice <= len(armors):
                hero["броня"] = armors[choice - 1]
                break
            else:
                print("Выбирите предложенные предметы.")
        except ValueError:
            print("Ошибка. Выбирите предложенные предметы.")

def choose_weapon():
    while True:
        print("Выберите оружие для сражения с драконом:")
        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon}")

        try:
            choice = int(input("Введите номер оружия: "))
            if 1 <= choice <= len(weapons):
                hero["оружие"] = weapons[choice - 1]
                break
            else:
                print("Выбирите предложенные предметы.")
        except ValueError:
            print("Ошибка. Выбирите предложенные предметы.")


def battle():
    choose_place()
    choose_armor()
    choose_weapon()
    choose_companion()
    while True:
        hero_choose = input("Герой говорит: 1.Смерть тебе чудовище, 2. Беги пока не поздно чудовище. Ваш выбор (1 или 2): ")

        if hero_choose not in ["1", "2"]:
            print("Пожалуйста, введите 1 или 2 ")
        else:
            if hero_choose == "1":
                outcome = random.choice(["Победа героя", "Проигрыш"])
            elif hero_choose == "2":
                outcome = random.choice(["Победа героя, Чудовищи не захотело уходить и проиграло.", "Проигрыш, Чудовищи не захотело уходить и победило.", ])

            print(outcome)
            break


def main():
    while True:
        battle()
        replay = input("Хотите ещё раз сыграть? (да/нет): ")
        if replay.lower() != "да":
            print("Вы выбрали: ")
            print(f"Место сражения: {hero['место сражения']}")
            print(f"Броня: {hero['броня']}")
            print(f"Оружие: {hero['оружие']}")
            print(f"Компаньон: {hero['компаньон']}")
            break
                
if __name__ == "__main__":
    main()