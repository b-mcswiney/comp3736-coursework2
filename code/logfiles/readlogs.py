import datetime
import matplotlib.pyplot as plt

def readfile(filename):
    file = open(filename, "r")

    rows = []

    # take each line in as a list object
    for line in file:
        # Remove whitespace
        line = line.replace(" ", "")
        rows.append(line.split((",")))

    # Convert parameters into a list
    for row in rows:
        # remove end of line character
        row[4] = row[4][:-3]

        # put params into a list
        row[4] = row[4].split(";")

    return rows

def count_correct_answers(filename):
    rows = readfile(filename)

    question_counts = {}

    for row in rows:
        question_id = row[2] 
        correct_answers = row[4]

        count_true = sum('correct=True' in answer for answer in correct_answers)

        if question_id in question_counts:
            question_counts[question_id] += count_true
        else:
            question_counts[question_id] = count_true

    return question_counts

# filename = "all-experiments.csv"
# result = count_correct_answers(filename)

def user_opinion_bar():
    user_data = [5, 5]
    names = ["area", "line"]

    plt.barh(names, user_data)
    plt.title("Participant graph preference")
    plt.ylabel("Chart type")
    plt.xlabel("Number of user votes")

    plt.savefig("user-votes.png", bbox_inches="tight")

user_opinion_bar()    


# # Display the counts for each question
# for question_id, count in result.items():
#     pass
#     # print(f"{question_id}: {count} correct=True")




