def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    if 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

user_name=input("Enter your full name: ")
birth_year_str=input("Enter your birth year: ")
birth_year=int(birth_year_str)

current_age = 2025 - birth_year

hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)
user_profile = {
    "Name": user_name,
    "Age": current_age,
    "Life_stage": life_stage,
    "Hobbies": hobbies
}

print("")
print("---")
print("Profile summary:")
print(f"Name: {user_profile['Name']}")
print(f"Age: {user_profile['Age']}")
print(f"Life_stage: {user_profile['Life_stage']}")
if not user_profile['Hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['Hobbies'])}):")
    for hobby in user_profile['Hobbies']:
        print(f"- {hobby}")
print("---")