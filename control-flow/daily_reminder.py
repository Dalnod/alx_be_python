task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if  time_bound == "yes":
    match priority:
        case "high":
            print(f"'{task}' is a {priority} task that requires immediate attention today!")
        case "medium":
            print(f"'{task}' is a {priority} task, please find time to sort it out today.")
        case "low":
            print(f"'{task}' is a {priority} task. but you have to make sure you do it before the day runs out.")


elif time_bound == "no":
    match priority:
        case "high":
            print(f"'{task}' is a {priority} task that you need to do.")
        case "medium":
            print(f"'{task}' is a {priority} task, please find time to sort it out.")
        case "low":
            print(f"'{task}' is a {priority} task. Consider completing it when you have free time.")

else:
    print("Input yes or no for for time bound")