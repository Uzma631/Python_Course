# Classroom Points Calculator

team1 = 1000
team2 = 95
team3 = 120
team4 = 90
team5 = 85
# Calculate total and average points
total = team1 + team2 + team3 + team4 + team5
average = total / 5
 
print(f"Total points: {total}")
print(f"Average per team  {average}")
 
# Each point gives 2 reward stars
stars_per_point = 2
reward_stars = total * stars_per_point
print("Total reward stars :", reward_stars)

# Pack reward stars into boxes of 25 stars each
boxes = reward_stars // 25
leftover = reward_stars % 25
 
print(f"Full boxes packed {boxes} ")
print(f"Leftover stars {leftover} ")
 
# Compare this week's points with last week's points
last_week = 400
 
print("Better than last week? :", total > last_week)
print("Same as last week?     :", total == last_week)
print("At least as good?      :", total >= last_week)
 
# Bonus challenge adds 30 points to the total
total += 30
print("After bonus points :", total)
 
# 15 points are removed for missed tasks
total -= 15
print("After missed tasks :", total)
 
# Final reward box count after all changes
reward_stars = total * stars_per_point
boxes = reward_stars // 25
 
print("Final boxes packed :", boxes)
