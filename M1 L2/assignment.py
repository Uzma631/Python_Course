# Assignment: Storing birthdays
import keyword
personal_name=input("Enter your name")
goal_name=input("Enter your personal goals")
target_month=input("Enter your target month")
daily_minutes= 30

print("\nName: ",personal_name)
print("Goal name: ",goal_name)
print("Target Month: ",target_month)
print("Daily Practice: ", daily_minutes, "minutes")

print("\nMy Personal Goal Plan\n")
print("Goal status", end=" ")
print("Not started")
 
print("Progress Reminder:", end=" - ")
print("Practice every day!")
 
# Display the complete goal summary
print("\n",personal_name,"plans to work on",goal_name,"for",daily_minutes ,"minutes every day.")
 
# Print Python's reserved words
print("\nPython keywords are...\n")
print(keyword.kwlist)
