name = input("Enter your full name :")
full_name = ""
if(name == ""):
    print("not valid name")
else:
    full_name = name

valid_age = ""
age = int(input("Enter your age :"))
if(age < 10 or age > 60):
    print("not valid age")
else:
    valid_age = age

city = input("Enter your city :")
skill = input("Enter your skill :")
skill_level = input("What is your skill level(Beginner/Intermediate/Advanced) :")

career_stage = "" 
if(age > 10 and age < 18):
    career_stage = "Student"
elif(age >= 18 and age <= 25):
    career_stage = "Early Professional"
elif(age > 25 and age < 60):
    career_stage = "Experienced Professional"

readiness_tag = ""
if(skill_level == "Beginner"):
    readiness_tag = "Foundation Stage"
elif(skill_level == "Intermediate"):
    readiness_tag = "Intern / Junior Ready"
elif(skill_level == "Advanced"):
    readiness_tag = "Production Ready"

recommendation = ""
if(skill_level == "Beginner"):
    recommendation = "Focus on core fundamentals and consistency"
elif(skill_level == "Intermediate"):
    recommendation = "Start building real life project"
elif(skill_level == "Advanced"):
    recommendation = "Contribute to production grade system"

print("\n" + "="*45)
print(f"{'CANDIDATE PROFILE CARD':^45}")
print("="*45)
print(f"{'Name':<15} : {full_name.title()}")
print(f"{'Age':<15} : {valid_age}")
print(f"{'City':<15} : {city.title()}")
print(f"{'Primary Skill':<15} : {skill}")
print(f"{'Skill Level':<15} : {skill_level}")
print("-" * 45)
print(f"{'Career Stage':<15} : {career_stage}")
print(f"{'Readiness Tag':<15} : {readiness_tag}")
print(f"{'Recommendation':<15} : {recommendation}")
print("="*45)