#ACTIVIITY FARM HARVEST CALCULATOR
field1=120
field2=40
field3=50
field4=80
field5=100

total= field1 + field2 + field3 + field4 + field5
average=total/5
print(f"total harvest is {total} kg")
print(f"average harvest per field is {average} kg")

#total earnings
price_per_kg = 15
earnings = total * price_per_kg
print(f"total earnings {earnings}")

bags     = total // 25
leftover = total % 25
print("Full bags packed  :", bags)
print("Leftover grain  :", leftover, "kg")

#comparision with last year
last_year=500
print("better than last year", total > last_year)
print("same as last year", total== last_year)
print("at least as good", total >= last_year)

#bonus crop
total += 30
print("After bonus crop :", total, "kg")

# Subtract 15 kg saved as seeds for next season
total -= 15
print("After seed reserve :", total, "kg")

# Final bag count after all adjustments
bags = total // 25
print("Final bags packed :", bags)
