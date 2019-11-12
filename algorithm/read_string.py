# Messing around with python's function for string

a1 = "images/eng/menu/adddrop_1.gif"
a2 = "beat is beat or mate"
a3 = "yggdra.png"
a4 = "milanor.png"
a5 = "durant.jpg"
a6 = "MIL"
abc = [a1,a2,a3,a4,a5]
print(len(a1))
# print(a1.count("eng"))
# print(a2.count("beat",5))
# print(a2.count("beat",0,5))
print(a6.center(10,"-")) # it would centered the word for me
print(a6.encode())
print(a6.expandtabs())
print(a5.expandtabs())
print(a4.join(["AAA","BBB"]))
if a5.find("jpg"):
    print("DURANT!".replace("DURANT!","MILANOR!!"))
for i in abc:
    if i.endswith("png"):
        print(i)