# Library Visit Planner

print("### Library Visit Planner ###")
print("Answer 3 quick questions and I will plan your library visit!\n")

day       = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather   = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
book_due  = input("Do you have a book to return? (yes / no): ").strip().lower()

print()
print(f"### Your Library Plan for {day} ###")
print("-" * 35)

# PART 1: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type    : Weekend - a good time for a relaxed library visit!")
elif day == "Monday":
    print("Day type    : Start of the week. Check your reading list.")
elif day == "Friday":
    print("Day type    : Last school day. Return books before the weekend.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Regular school day. Plan a short library visit.")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

# PART 2: sunny AND book due
if weather == "sunny" and book_due == "yes":
    print("Library tip : Great weather! Return your book and borrow a new one.")

# PART 3: rainy OR cloudy
if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Carry an umbrella if you are going to the library.")

# PART 4: IF  book NOT due
if not (book_due == "yes"):
    print("Book status : No book return needed today. You can browse new books.")

# PART 5: Combining AND + OR + NOT together
if weather == "rainy" and book_due == "yes":
    print("Best plan   : Visit the library carefully and return your book on time.")
elif weather == "sunny" and book_due == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : Stop by the library after school and return your book.")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect day for a longer reading session at the library!")
else:
    print("Best plan   : Check your schedule and plan a simple library visit.")

print()
print("Library plan complete! Happy reading!")
