print("Enter a Number (Numerator): ")
num_numerator = int(input())
print("Enter a Number (denominator): ")
num_denominator = int(input())

if num_numerator %num_denominator ==0:
  print("\n" +str(num_numerator)+ " is divisible by " +str(num_denominator))
else:
  print("\n" +str(num_numerator)+ " is not divisible by " +str(num_denominator))