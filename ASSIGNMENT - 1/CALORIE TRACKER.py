# ----------------------------------------------------------
# Project Title : Daily Calorie Tracker CLI
# Author        : SANIA KAMBOJ
# Roll No       : 2501730319
# ----------------------------------------------------------

import datetime

print("\n=== Welcome to the Daily Calorie Tracker CLI ===")
print("Track your meals, calculate total calories, and compare with your daily limit.\n")


meals = []
calories = []

n = int(input("How many meals do you want to log today? "))

for i in range(n):
    meal_name = input(f"\nEnter name of meal {i+1}: ")
    cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(cal)


total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))


if total_calories > daily_limit:
    status_message = f"WARNING: You exceeded your daily limit by {total_calories - daily_limit:.2f} calories!"
else:
    status_message = f"SUCCESS: You are within your daily limit. Remaining: {daily_limit - total_calories:.2f} calories."


print("\n\n========= DAILY CALORIE SUMMARY =========")
print("Meal Name\t\tCalories")
print("-----------------------------------------")
for meal, cal in zip(meals, calories):
    print(f"{meal:<16}\t{cal:>8.2f}")
print("-----------------------------------------")
print(f"Total:\t\t\t{total_calories:.2f}")
print(f"Average per meal:\t{average_calories:.2f}")
print(status_message)
print("=========================================\n")

save = input("Do you want to save this session log? (yes/no): ").strip().lower()
if save == "yes":
    filename = "calorie_log.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("=== Daily Calorie Tracker Log ===\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("----------------------------------\n")
        for meal, cal in zip(meals, calories):
            file.write(f"{meal:<16}\t{cal:>8.2f}\n")
        file.write("----------------------------------\n")
        file.write(f"Total: {total_calories:.2f}\n")
        file.write(f"Average per meal: {average_calories:.2f}\n")
        file.write(status_message + "\n")
    print(f"\nSession log saved successfully to '{filename}'\n")
else:
    print("\nSession not saved. Goodbye!\n")

print("Thank you for using the Daily Calorie Tracker CLI!")

