
import datetime

print("\n Welcome to the Daily Calorie Tracker CLI! ")
print("Track your meals, count your calories, and stay within your daily goal.\n")


meals = []
calories = []

num_meals = int(input("How many meals do you want to log today? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter meal {i+1} name: ")
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_amount)


total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))


if total_calories > daily_limit:
    status_message = "⚠️ You have exceeded your daily calorie limit!"
else:
    status_message = "✅ Great job! You are within your daily calorie limit."

print("\n---------------- Calorie Summary ----------------")
print("Meal Name\tCalories")
print("-----------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]:<15}\t{calories[i]:>6.2f}")

print("-----------------------------------------------")
print(f"Total:\t\t{total_calories:.2f}")
print(f"Average:\t{average_calories:.2f}")
print(status_message)
print("-------------------------------------------------\n")


save_log = input("Would you like to save this session to a file? (yes/no): ").strip().lower()

if save_log == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    calorie_tracker = "calorie_log.txt"
    with open(calorie_tracker, "w") as file:
        file.write("Daily Calorie Tracker Log\n")
        file.write(f"Date & Time: {timestamp}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("---------------------------------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}\t{calories[i]:>6.2f}\n")
        file.write("---------------------------------\n")
        file.write(f"Total:\t\t{total_calories:.2f}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write(f"Status: {status_message}\n")
    print(f"\n💾 Session saved successfully as '{calorie_tracker}'!")

print("\nThank you for using the Daily Calorie Tracker. Stay healthy! ")
