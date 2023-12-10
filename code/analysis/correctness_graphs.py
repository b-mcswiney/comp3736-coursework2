import matplotlib.pyplot as plt

data = {
    'question 1': 10,
    'question 2': 10,
    'question 3': 9,
    'question 4': 10,
    'question 5': 10,
    'question 6': 10,
    'question 7': 10,
    'question 8': 2,
    'question 9': 8,
    'question 10': 9,
    'question 11': 10,
    'question 12': 9,
    'question 13': 10,
    'question 14': 10,
    'question 15': 1,
    'question 16': 10,
    'question 17': 10,
    'question 18': 9,
    'question 19': 7,
    'question 20': 10,
}

questions = list(data.keys())
correct_answers = list(data.values())

plt.figure(figsize=(10, 6))
plt.bar(questions, correct_answers, color='green')
plt.title('Correct Answers for Each Question')
plt.xlabel('Questions')
plt.ylabel('Number of Correct Answers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('correct_answers_bar_chart.png')

plt.show()
