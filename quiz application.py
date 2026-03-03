import time

def play_level(questions, level_name, marks, total_score, file):
    print("\n===== ", level_name, "Level =====")
    file.write("\n===== " + level_name + " Level =====\n")

    level_score = 0

    for i in range(len(questions)):
        print("\nQuestion", i + 1)
        print(questions[i]["text"])

        file.write("\nQuestion " + str(i+1) + "\n")
        file.write(questions[i]["text"] + "\n")

        for option in questions[i]["options"]:
            print(option)   # show options on screen only

        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        file.write("User Answer: " + user_answer + "\n")
        if user_answer == questions[i]["answer"]:
            level_score += marks
            print("Correct Answer")
            file.write("Correct Answer\n")
        else:
            print("Wrong Answer")
            print("Correct answer is:", questions[i]["answer"])
            file.write("Wrong Answer\n")

        print("Current Level Score:", level_score)
        file.write("Current Level Score: " + str(level_score) + "\n")

    total_score += level_score

    print("\nLevel Completed:", level_name)
    print("Level Score:", level_score)
    print("Total Score Till Now:", total_score)

    file.write("\nLevel Completed: " + level_name + "\n")
    file.write("Level Score: " + str(level_score) + "\n")
    file.write("Total Score Till Now: " + str(total_score) + "\n")

    return total_score


# ---------------- QUESTIONS ---------------- #

beginner = [
    {"text": "Python is a __ language.",
     "options": ["A. Low level", "B. High level", "C. Machine level", "D. Assembly"],
     "answer": "B"}
]

medium = [
    {"text": "The ability of one class to acquire methods from another class is called __.",
     "options": ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
     "answer": "A"}
]

hard = [
    {"text": "Which concept allows the same method name with different behavior?",
     "options": ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
     "answer": "C"}
]

# ---------------- MAIN PROGRAM ---------------- #

start_time = time.time()

file = open("result.txt", "w")

print("Welcome to Advanced Python Quiz Game")
file.write("Welcome to Advanced Python Quiz Game\n")

name = input("Enter your Name: ")
usn = input("Enter your USN: ")

file.write("Student Name: " + name + "\n")
file.write("USN: " + usn + "\n")

total_score = 0
max_score = 0
ended_level = "Completed All Levels"

# Beginner
max_score += len(beginner) * 2
total_score = play_level(beginner, "Beginner", 2, total_score, file)

choice = input("\nDo you want to continue to Medium Level? (yes/no): ").lower()
file.write("Continue to Medium: " + choice + "\n")

if choice != "yes":
    ended_level = "Ended at Beginner Level"

else:
    max_score += len(medium) * 5
    total_score = play_level(medium, "Medium", 5, total_score, file)

    choice = input("\nDo you want to continue to Hard Level? (yes/no): ").lower()
    file.write("Continue to Hard: " + choice + "\n")

    if choice != "yes":
        ended_level = "Ended at Medium Level"
    else:
        max_score += len(hard) * 10
        total_score = play_level(hard, "Hard", 10, total_score, file)

end_time = time.time()
time_taken = round(end_time - start_time, 2)

# ---------------- FINAL TABLE ---------------- #

print("\n==============================")
print("         FINAL RESULT         ")
print("==============================")
print(f"Name        : {name}")
print(f"USN         : {usn}")
print(f"Total Score : {total_score}")
print(f"Max Score   : {max_score}")
print(f"Time Taken  : {time_taken} seconds")
print(f"Status      : {ended_level}")
print("==============================")

file.write("\n==============================\n")
file.write("         FINAL RESULT         \n")
file.write("==============================\n")
file.write("Name        : " + name + "\n")
file.write("USN         : " + usn + "\n")
file.write("Total Score : " + str(total_score) + "\n")
file.write("Max Score   : " + str(max_score) + "\n")
file.write("Time Taken  : " + str(time_taken) + " seconds\n")
file.write("Status      : " + ended_level + "\n")
file.write("==============================\n")

file.close()