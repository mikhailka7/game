from random import randint
inventory = {
    "resources":0,
    "weapon":[]
}
weapons = ["нож","пистолет","автомат","гранатомёт"]
def start_school():
    ress = 0
    one_floor_res = ["парту","тумбу","шкаф","полочку","столовую"]
    print("ты в школе")
    if inventory["weapon"] == []:
        print(f'у тебя пока нет оружий')
    else:
        print(f'из оружий у тебя только {inventory["weapon"]}')
    while True:
        csm = randint(0, 1)
        r_th = randint(0,4)
        if input(f"ты видешь {one_floor_res[r_th]} хочешь обыскать (да/нет)") == 'да':
            if csm == 1:
                print("на тебя нападает монстр")
                if inventory["weapon"] != []:
                    print("ты убил монстра, можешь дальше продолжать искать ресурсы")
                else:
                    print("тебя убили 🦴🦴🦴")
                    inventory["weapon"]=[]
                    inventory["resources"]=0
                    break
            r_res = randint(1,30)
            if r_res >= 20:
                r_weap = randint(0,3)
                print(f"поздравляю ты нашел оружие - {weapons[r_weap]}")
                inventory["weapon"].append(weapons[r_weap])
            else:
                print(f"ты нашел {r_res} рессурсов, они будут сложены тебе в инвентарь")
                ress+=r_res
            if input("хочешь выйти из школы") == 'да':
                break
    inventory["resources"]+=ress
