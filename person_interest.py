person_interest = {}
flag = True
while flag:
    name = input("Enter your name: ")
    interest = input(" What would you like to do? ")

    person_interest[name] = interest

    repeat = input("Is there is any one how tell me your interest? (yes/no)")
    if repeat == 'no':
        flag = False

print("\n...person_interest...")
for name, interest in person_interest.items():
    print(f"{name} would like to {interest} to do.")

print(person_interest)
