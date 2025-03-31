import random,time
from colorama import Fore

monsters = ['Врач', 'Уборщик', 'Неудачный пациент', 'Эксперимент химика', 'Ничего']

def palataRoom():
    items = ['Бинты','Скальпель','Одежду пациента','Фонарик','Скотч','Ничего']
    randomItems = random.choice(items)
    randomMonster = random.choice(monsters)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы зашли в палату.")
    time.sleep(3)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы нашли {randomItems}.")
    time.sleep(3)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы увидели {randomMonster}.")
    time.sleep(3)
    if randomItems == 'Скальпель':
        print(f"\n{Fore.YELLOW}Вы отбились от {randomMonster}.")
        time.sleep(3)
        return True
    elif randomItems == 'Фонарик':
        print(f"\n{Fore.YELLOW}Вы отбились от {randomMonster}.")
        time.sleep(3)
        return True
    elif randomItems == 'Одежду пациента':
        print(f"\n{Fore.YELLOW}Вы замаскировались под пациента.")
        time.sleep(3)
        return True
    elif randomMonster == 'Ничего':
        print(f"\n{Fore.BLACK}Вы пошли дальше.")
        time.sleep(3)
        return True
    else:
        print(f"\n{Fore.RED}Вы погибли.")
        time.sleep(1.2)
        return False

def stolovayaRoom():
    items = ['Плесневелый хлеб','Кухонный нож','Осколок тарелки',"Ложка"'Ничего']
    randomItems = random.choice(items)
    randomMonster = random.choice(monsters)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы зашли в Столовую.")
    time.sleep(3)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы нашли {randomItems}.")
    time.sleep(3)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы увидели {randomMonster}.")
    time.sleep(3)
    if randomItems == 'Кухонный нож':
        print(f"\n{Fore.YELLOW}Вы отбились от {randomMonster}.")
        time.sleep(3)
        return True
    elif randomItems == 'Осколок тарелки':
        print(f"\n{Fore.YELLOW}Вы отбились от {randomMonster}.")
        time.sleep(3)
        return True
    elif randomMonster == 'Ничего':
        print(f"\n{Fore.BLACK}Вы пошли дальше.")
        time.sleep(3)
        return True
    else:
        print(f"\n{Fore.RED}Вы погибли.")
        time.sleep(1.2)
        return False

def nurseRoom():
    items = ['Халат врача','Медикаменты','Шприц','Ничего']
    randomItems = random.choice(items)
    randomMonster = random.choice(monsters)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы зашли в комнату врача.")
    time.sleep(3)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы нашли {randomItems}.")
    time.sleep(3)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы увидели {randomMonster}.")
    time.sleep(3)
    if randomItems == 'Шприц':
        print(f"\n{Fore.YELLOW}Вы отбились от {randomMonster}.")
        time.sleep(3)
        return True
    elif randomItems == 'Халат врача':
        print(f"\n{Fore.YELLOW}Вы замаскировались под врача.")
        time.sleep(3)
        return True
    elif randomMonster == 'Ничего':
        print(f"\n{Fore.BLACK}Вы пошли дальше.")
        time.sleep(3)
        return True
    else:
        print(f"\n{Fore.RED}Вы погибли.")
        time.sleep(1.2)
        return False

def receptionRoom():
    items = ['Стекло от монитора','Ткань','Ручку','Ничего']
    randomItems = random.choice(items)
    randomMonster = random.choice(monsters)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы зашли в приемную.")
    time.sleep(3)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы нашли {randomItems}.")
    time.sleep(3)
    print(f"\n{Fore.LIGHTMAGENTA_EX}Вы увидели {randomMonster}.")
    time.sleep(3)
    if randomItems == 'Стекло от монитора':
        print(f"\n{Fore.YELLOW}Вы отбились от {randomMonster}.")
        time.sleep(3)
        return True
    elif randomItems == 'Ручку':
        print(f"\n{Fore.YELLOW}Вы отвлекли {randomMonster} и спрятались.")
        time.sleep(3)
        return True
    elif randomMonster == 'Ничего':
        print(f"\n{Fore.BLACK}Вы пошли дальше.")
        time.sleep(3)
        return True
    else:
        print(f"\n{Fore.RED}Вы погибли.")
        time.sleep(1.2)
        return False

def streetRoom():
    print(f"\n{Fore.BLACK}Вы покинули больницу.")
    return False

def hospitalRoom():
    while True:
        print(f"\n{Fore.RED}   Вы вошли|вышли в коридор.                 ")
        print(f"\n{Fore.BLUE}         Палата                 ")
        print(f"\n{Fore.BLUE}        Столовая                 ")
        print(f"\n{Fore.BLUE}      Комната врача                 ")
        print(f"\n{Fore.BLUE}         Приемная                 ")
        print(f"\n{Fore.BLUE}     Выход из больницы                 ")
        room = input(f"{Fore.RED}  Выберите комнату: ")
        if room == 'Палата':
            if not palataRoom():
                break
        elif room == 'Столовая':
            if not stolovayaRoom():
                break
        elif room == 'Комната врача':
            if not nurseRoom():
                break
        elif room == 'Приемная':
            if not receptionRoom():
                break
        elif room == 'Выход из больницы':
            if not streetRoom():
                break
        else:
            print(f"{Fore.BLUE}Такой комнаты нет.")
            time.sleep(2)
hospitalRoom()