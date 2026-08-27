# SECRET AGENT BADGE

# 1. Get information from the user
name = input("Enter your name: ")
gadget = input("Enter your favorite gadget: ")
agent_number = int(input("Enter your agent number: "))

# 2. Different data types
speed = 9.5          # float
active = True        # boolean

# 3. Indexing and slicing
first_letter = name[0]
code_name = name[:3] + first_letter

# 4. Reverse the gadget using slicing
secret_gadget = gadget[::-1]

# 5. Create the badge using concatenation
badge = "AGENT " + code_name.upper() + \
        " | ID: " + str(agent_number) + \
        " | SPEED: " + str(speed) + \
        " | ACTIVE: " + str(active) + \
        " | GADGET: " + secret_gadget.upper()

# 6. Display badge
print("\n===== SECRET AGENT BADGE =====")
print(badge)
print("==============================")