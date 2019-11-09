choices = ["a","b","c"]
fish01 = "fish01"
fish02 = "fish02"
fish03 = "fish03"

def inputChecker(array,prompt):
    user_input = input(prompt)
    is_good = False # break loop helper
    for i in array:
        if user_input.lower() == i:
            print("Good")
            is_good = True
            break
    if not is_good:
        print("NO GOOD")

print("Go out from dungeon the command line game.")
# inputChecker(choices, "choose: ")
print("The first one {0} and second one {1}".format(fish01,fish02))
print("Today temperature is {0:.3f} degree".format(28.123456789))
print("{:*^30}".format("Fish"))
print("WUT {0:1} WOT".format("FISHFISH"))
print("Beat"[0:1])