from quiz.question import Question
from quiz.controller import QuizController
from quiz.ui import QuizUI

# Line max trial 1 and 2
question = Question("Which Graph shows more gold medals for GB?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "A", ["A", "", "", "","B"], "line")
question2 = Question("Which Graph shows more total medals for the USA?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "A", ["A", "", "", "", "B"], "line")

# Area max trial 1 and 2
question3 = Question("Which Graph shows more gold medals for GB?",
                    "assets/area-max-trial-1.png",
                    "assets/area-max-trial-2.png", "A", ["A", "", "", "", "B"], "area")
question4 = Question("Which Graph shows more total medals for the USA?",
                    "assets/area-max-trial-1.png",
                    "assets/area-max-trial-2.png", "A", ["A", "", "", "", "B"], "area")

# Line max trial 3 and 4
question5 = Question("In which Graph did GB win less bronze medals?",
                    "assets/line-max-trial-3.png", 
                    "assets/line-max-trial-4.png", "B", ["A", "", "", "", "B"], "line")
question6 = Question("What is the sum of the silver medals won by Germany in both graphs?",
                    "assets/line-max-trial-3.png",
                    "assets/line-max-trial-4.png", "25", ["13", "25", "31", "35", "38"], "line")

# Area max trial 3 and 4
question7 = Question("In which Graph did GB win less bronze medals?",
                    "assets/area-max-trial-3.png",
                    "assets/area-max-trial-4.png", "B", ["A", "", "", "", "B"], "area")
question8 = Question("What is the sum of the silver medals won by Germany in both graphs?",
                    "assets/area-max-trial-3.png",
                    "assets/area-max-trial-4.png", "31", ["29", "23", "27", "31", "35"], "area")

# line years trial 1 and 2
question9 = Question("which year shows the least amount of total medals gained?",
                    "assets/line-years-trial-1.png", # Graph 2 shown
                    "assets/line-years-trial-2.png", "Year 3", ["", "Year 1", "Year 2", "Year 3", ""], "line")
question10 = Question("Which year shows the most amount of total medals gained??",
                    "assets/line-years-trial-1.png", # Graph 1 shown
                    "assets/line-years-trial-2.png", "Year 2", ["", "Year 1", "Year 2", "Year 3", ""], "line")

# area years trial 1 and 2
question11 = Question("Which year shows the least amount of total medals gained?",
                    "assets/area-years-trial-1.png", # Graph 2 shown
                    "assets/area-years-trial-2.png", "Year 2", ["", "Year 1", "Year 2", "Year 3", ""], "area")
question12 = Question("Which year shows the most amount of total medals gained?",
                    "assets/area-years-trial-1.png", # Graph 1 shown
                    "assets/area-years-trial-2.png", "Year 1", ["", "Year 1", "Year 2", "Year 3", ""], "area")

# line years trial 3 and 4
question13 = Question("Which year shows the most gold medals?",
                    "assets/line-years-trial-3.png", # Graph 2 shown
                    "assets/line-years-trial-4.png", "Year 1", ["", "Year 1", "Year 2", "Year 3", ""], "line")
# area years trial 3 and 4
question14 = Question("Which year shows the most gold medals?",
                    "assets/area-years-trial-3.png", # Graph 2 shown
                    "assets/area-years-trial-4.png", "Year 1", ["", "Year 1", "Year 2", "Year 3", ""], "area")

# line country trial 1 and 2
question15 = Question("Which country got the most medals?",
                    "assets/line-country-trial-1.png", # Graph 1 shown
                    "assets/line-country-trial-2.png", "AUS", ["GB", "AUS", "JP", "GER", ""], "line")
question16 = Question("Which country got the 2nd highest amount of silver medals?",
                    "assets/line-country-trial-1.png", # Graph 1 shown
                    "assets/line-country-trial-2.png", "JP", ["GB", "AUS", "JP", "GER", ""], "line")

# area country trial 1 and 2
question17 = Question("In Graph A, which country got the most medals?",
                    "assets/area-country-trial-1.png", # Graph 1 shown
                    "assets/area-country-trial-2.png", "GER", ["GB", "AUS", "JP", "GER", ""], "area")
question18 = Question("In Graph B, which country got the 2nd highest amount of silver medals?",
                    "assets/area-country-trial-1.png", # graph 2 shown
                    "assets/area-country-trial-2.png", "GER", ["GB", "AUS", "JP", "GER", ""], "area")

# Comparison trials
question19 = Question("Do these graphs have the same datasets?",
                    "assets/line-same-trial-1.png",
                    "assets/area-same-trial-1.png", "Yes", ["Yes", "", "", "", "No"], "mix")
question20 = Question("Do these graphs have the same datasets?",
                    "assets/line-max-trial-1.png",
                    "assets/area-max-trial-1.png", "No", ["Yes", "", "", "", "No"], "mix")

question21 = Question("Which graphtype do you find easier to read??",
                    "assets/line-max-trial-2.png",
                    "assets/area-max-trial-2.png", "", ["line", "", "", "", "area"], "N/A")


question_list = []
question_list.append(question)
question_list.append(question2)
question_list.append(question3)
question_list.append(question4)
question_list.append(question5)
question_list.append(question6)
question_list.append(question7)
question_list.append(question8)
question_list.append(question9)
question_list.append(question10)
question_list.append(question11)
question_list.append(question12)
question_list.append(question13)
question_list.append(question14)
question_list.append(question15)
question_list.append(question16)
question_list.append(question17)
question_list.append(question18)
question_list.append(question19)
question_list.append(question20)
question_list.append(question21)

controller = QuizController(question_list)

QuizUI(controller)
