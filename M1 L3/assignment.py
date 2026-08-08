# Assignment: School Club Member Badge
name=input("enter your name ")
club=input("enter your club name ")

# Store Details Using Different Data Types Create variables 
member_number= 7
points_earned= "excellent"
event_count= 3
meeting_hours= 4.5
active_status= True

print("\n Name:", name, "-> type:", type(name))
print("Club:", club, "-> type:", type(club))
print("Member Number:", member_number, "-> type:", type(member_number))
print("Points Earned:", points_earned, "-> type:", type(points_earned))
print("Event Count:", event_count, "-> type:", type(event_count))
print("Meeting Hours:", meeting_hours, "-> type:", type(meeting_hours))
print("Is Active:", active_status, "-> type:", type(active_status))

member_number_text = str(member_number)
event_count_text = str(event_count)
points_text = str(points_earned)
status_text = str(active_status)
 
print("\nMember Number as text:", member_number_text, "-> type:", type(member_number_text))
print("Event Count as text:", event_count_text, "-> type:", type(event_count_text))
print("Points as text:", points_text, "-> type:", type(points_text))
print("Status as text:", status_text, "-> type:", type(status_text))
 

#create a badge code
first_three = name[0:3]
last_letter = name[-1:]
badge_code= first_three + last_letter
print("badge code is", badge_code)

#Reverse the Club Name
reverse= club[::-1]

#Join everything together to build the final badge message
badge_line_1 = "CLUB MEMBER " + badge_code.upper()
badge_line_2 = "ID: " + member_number_text + " | EVENTS: " + event_count_text
badge_line_3 = "POINTS: " + points_text + " | ACTIVE: " + status_text
badge_line_4 = "SECRET CLUB CODE: " + reverse.upper()

#Print the complete school club badge
print("")
print("===== SCHOOL CLUB MEMBER BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("====================================")

