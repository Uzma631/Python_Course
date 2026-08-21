#python code for membership operator
print("Enter Marks Obtained in 5 Subjects:")


science = int(input())
maths = int(input())
computer = int(input())
english = int(input())
history = int(input())

tot = science + maths + computer + english + history
avg = int(tot / 5)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input!")

elif avg in range(91, 101):
    print("Your Grade is A1")

elif avg in range(81, 91):
    print("Your Grade is A2")

elif avg in range(71, 81):
    print("Your Grade is B1")

elif avg in range(61, 71):
    print("Your Grade is B2")

elif avg in range(51, 61):
    print("Your Grade is C1")

elif avg in range(41, 51):
    print("Your Grade is C2")

elif avg in range(33, 41):
    print("Your Grade is D")

elif avg in range(21, 33):
    print("Your Grade is E1")

elif avg in range(0, 21):
    print("Your Grade is E2")
