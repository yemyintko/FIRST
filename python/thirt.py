marks = int(input("What is your exam marks"))
gread_A = 100
gread_B = 79
gread_C = 59
gread_F = 40
if marks is 100 or gread_A > marks:
    print("You are gread A.")
elif marks is 79 or marks < gread_B:
    print("You are gread B.")
elif marks is 59 or marks > gread_C:
    print("You are gread C.")
else:
    print("You fail")