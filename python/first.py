enemy  = 10000
my_soldiers = 12000
All_army = 15000

if enemy > my_soldiers:
    print("We are going to lose")
elif my_soldiers > All_army:
    print("i won't need your army help")
elif enemy < my_soldiers:
    print("We are the winner")
else:
    print("I can't show my face to the king")