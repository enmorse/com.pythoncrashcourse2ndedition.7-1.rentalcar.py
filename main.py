# Write a program that asks the user what kind of
# rental car they would like. Print a message about
# that car, such as "Let me see if I can find you a
# Subaru.
prompt = input("What kind of rental car would you "
               "like to rent?: ")
message = f"Let me see if I can find a {prompt.title()}."

print(message)
