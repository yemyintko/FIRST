My_money = 10000
jacket = 2500
shoses = 2000
pant  = 3000
hat  = 3000
all_clothes = (jacket + shoses + pant)
print("Today is my birthday! dad said i can buy what ever i want.")

if My_money >= (all_clothes + hat):
    print("I am wearing my new clothes tomorrow.")
elif all_clothes <= My_money:
    print("I will buy  all of these.")
elif My_money == (all_clothes + hat):
    print("I don't have any money left.")
else:
    print("I will buy these later.")

toys = 1500
dad_money = 15000
lent_money = (- (all_clothes + hat + toys))
stuffs = (all_clothes + hat + toys)

if lent_money == dad_money:
    print("Dad can give me some money.")
elif (My_money + lent_money) > stuffs:
    print("Is my birthday after all! right dad.")
else:
    print("Next week i will come back for these.")

print("Dad i hungry i go to the restaurant.Ok")
print("Dad, You can order what ever you want.")

ice_cream = 500
chicken_pasta = 1500
tomato_soup = 1000
strawberry_dessert = 2000
print("waiter, what do you want today!sir.")
left_money = (My_money + dad_money) - stuffs
food = (ice_cream + chicken_pasta + tomato_soup + strawberry_dessert)

if left_money == food:
    print("Dad, This so much i don't have money left for the dishes.")
elif left_money < food:
    print("This restaurant is expensive for us.")
elif food != left_money:
    print("Dad, I want all the dishes which my son want to order.")
else:
    print("Let go home.")