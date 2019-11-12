src = "TaeB"
box = []
src2 = ""

# put string into array (each letter)
for s in src:
    box.append(s)
print(box)

le = len(box)
for i in range(int(le/2)):
    temp = box[i]
    box[i] = box[le - (1 + i)]
    box[le - (1 + i)] = temp
for j in box:
    src2 += j 
print(src2)

# 1 2 3 4
# (1) 2 3 (4)
# 1 (2) (3) 4
