import random as rd
gacha = ['hamon','pokemon','jojo','teddy']
mything = []
answer = input('press anything to use the gacha')
while (answer!='q'):
    print('your item :',mything)
    if (len(gacha)==0):
        print('congrat you obtain all the item')
        quit()
    randomindex=rd.choice(gacha)
    print('Item that you got is ',randomindex)
    mything.append(randomindex)
    gacha.remove(randomindex)
    print('thing that left in the box: '+str(gacha))
    while(True):
        answer2=input('1.add thing to the gacha\n2.add nothing to gacha\ninput: ')
        if (answer2=='1'):
            addthing=input('type the thing you like to add: ')
            gacha.append(addthing)
            addmore=input('add more thing?If add type anything if not q')
            if (addmore!='q'):
                break
        else:
            break
    choice=input('continue the gacha type anything or quit type q')
    print('thing left in the box: ',str(gacha),'\nthing you have : ',str(mything))
    if (choice=='q'):
        print('thank for using the services')
        exit()            