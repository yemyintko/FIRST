marks = int(input("What is your exam marks"))
full_mark = 100

if marks >= 80 and marks <= full_mark:
    print("You are in gread A.")
elif marks >= 60 and marks <= 79:
    print("You are in gread B.")
elif marks >= 40 and marks <= 59:
    print("You are in gread C.")
elif marks <40:
    print("You fail.")
else:
    print("error!")