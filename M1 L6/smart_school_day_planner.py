#SMART SCHOOL DAY PLANNER

print("Answer 3 quick questions and I will plan your day!\n")

day      = input("What day is it?").strip().capitalize()
weather  = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is your homework done? (yes / no): ").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-" * 35)

# PART 1: classify the day
if day in ("Saturday", "Sunday"):
    print("Its Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type    : First day of the week. Pack your weekly planner.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Regular school day. Stay focused!")
elif day == "Friday":
    print("Day type    : Last school day. Return library books today.")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

# PART 2: IF sunny AND homework done
if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and homework is done!")
# PART 3: IF rainy OR cloudy
if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Pack your umbrella - it may get wet outside.")

# PART 4: IF homework NOT done
if not (homework == "yes"):
    print("Homework    : Not done yet. Finish it before going out!")

# PART 5 -- Combining AND + OR + NOT together
if weather == "rainy" and not (homework == "yes"):
    print("Best plan   : Stay in, finish homework, then watch your favourite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print()
print("Plan complete! Have a wonderful day!")
