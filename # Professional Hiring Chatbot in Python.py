# Professional Hiring Chatbot in Python

print("\n🤖 Welcome to the Hiring Chatbot")
print("Please answer the following questions honestly.\n")
print("and feel calm during interview.\n")

# 1. Basic Information
name = input("Full Name: ").strip()
email = input("Email Address: ").strip()

print(f"\nThank you, {name}. Let's continue.\n")

# 2. Education Check
print("Education Level:")
print("1. Intermediate")
print("2. Graduation")
print("3. Masters")

edu_choice = input("Select option (1/2/3): ")

if edu_choice == "1":
    print("\n❌ Sorry, graduation is required for this position.")
    print("Application terminated.")
    exit()

# 3. Experience
experience = input("\nHow many years of professional experience do you have? (Enter number): ")

# 4. Skills Selection
print("\nSelect your primary skill (choose ONE):")
print("1. Marketing")
print("2. Web Development")
print("3. Frontend Development")
print("4. Backend Development")
print("5. Digital Product Creation")
print("6. E-commerce Management")

skill_choice = input("Enter option (1-6): ")

skills_dict = {
    "1": "Marketing",
    "2": "Web Development",
    "3": "Frontend Development",
    "4": "Backend Development",
    "5": "Digital Product Creation",
    "6": "E-commerce Management"
}

if skill_choice not in skills_dict:
    print("\n❌ Invalid selection. Application rejected.")
    exit()

selected_skill = skills_dict[skill_choice]

# 5. Availability
availability = input("\nAre you available for full-time work? (yes/no): ").lower()
if availability != "yes":
    print("\n❌ This role requires full-time availability.")
    exit()

# 6. Reference Check
reference = input("\nDo you have any professional reference? (yes/no): ").lower()

if reference == "yes":
    ref_name = input("Reference Name: ")
    ref_contact = input("Reference Contact Info: ")
else:
    ref_name = "Not Provided"
    ref_contact = "Not Provided"

# 7. Final Decision
print("\n🔍 Reviewing your application...\n")

print("🎉 CONGRATULATIONS!")
print(f"Dear {name}, you are SELECTED for the position.")
print(f"Role Based on Skill: {selected_skill}")
print("💰 Basic Salary: 50,000 PKR")
print("📄 Contract Duration: 1 Year")
print("📅 Joining Date: 1st January")

print("\n📌 Reference Status:", ref_name)
print("📧 HR Team will contact you via email.")

print("\n✅ Application Successfully Completed.")
