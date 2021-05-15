from random import randint
class color:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

# introduction part
print(color.red + "_"*128)
print(color.blue + color.bold + " "*55 +": DiCE GaME :" + color.end)
player = input("NAME: ")
com_1 = 0
pla_1 = 0
game = 0

#body part
x = True
press = 1
y = True
while y:
    dice_no = int(input(color.darkcyan + "DICE'S range:  "+ color.end))
    if (dice_no >= 4):
        y = False
    else:
        print("DICE's RANGE must be greater than 4")
        y = True
while x:
    game += 1
    print(color.red + " " * 55 + ": NEW GAME : ",game, color.end)
    print(color.blue + "_" * 128)
    for j in range(press):
        com = str(randint(1, dice_no))
        print(color.blue + " " * 55 + "Comuter Turn: " + color.darkcyan + color.bold + com)
        for i in range(press):
            pla = str(randint(1,dice_no))
            print(color.blue + " "*54,player," Turn: " +color.darkcyan + color.bold + pla + color.end)
            if ( com > pla):
                com_1 += 1
                print(color.bold + color.red + "\n"+ " " * 55 + " Computer WON !")
                print(color.blue + "_" * 128)
            elif( com == pla):
                com_1 +=1
                pla_1 +=1
                print(color.bold + color.red + "\n"+" " * 55 + " Match TIE !")
                print(color.blue + "_" * 128)
            else:
                pla_1 += 1
                print(color.bold + color.red + "\n"+ " " * 55 +" You WON !")
                print(color.blue + "_" * 128)
        break
    dec = input("Want to Play Again ?")
    if (dec=='yes' or dec=='Yes' or dec=='Yeah' or dec=='yeah'):
        x = True
    else:
        x = False

#Result Part
print(color.red + "_"*128)
print(color.darkcyan + "\n"+" "*60 + "SCORE")
print(color.darkcyan + color.bold + " "*55 + "Computer: " + str(com_1))
print(color.darkcyan + color.bold + " "*56 ,player,": "+ str(pla_1))
