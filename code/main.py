from quiz.question import Question
from quiz.controller import QuizController
from quiz.ui import QuizUI


# Just deine 1 question for testing purposes
question = Question("Which Graph shows more gold medals for the UK?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "A", ["A", "", "", "","B"], "line")
question2 = Question("Which Graph shows more total medals for the USA?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "B", ["A", "", "", "", "B"], "line")
question3 = Question("Which Graph shows more gold medals for the UK?",
                    "assets/area-max-trial-1.png",
                    "assets/area-max-trial-2.png", "A", ["A", "", "", "", "B"], "line")
question4 = Question("Which Graph shows more total medals for the USA?",
                    "assets/area-max-trial-1.png",
                    "assets/area-max-trial-2.png", "B", ["A", "", "", "", "B"], "line")
question5 = Question("In which Graph did UK win less bronze medals?",
                    "assets/line-max-trial-3.png",
                    "assets/line-max-trial-4.png", "A", ["A", "", "", "", "B"], "line")
question6 = Question("What is the sum of the silver medals won by Germany in both graphs?",
                    "assets/line-max-trial-3.png",
                    "assets/line-max-trial-4.png", "20", ["10", "15", "20", "25", "30"], "line")
question7 = Question("In which Graph did UK win less bronze medals?",
                    "assets/area-max-trial-3.png",
                    "assets/area-max-trial-4.png", "A", ["A", "", "", "", "B"], "line")
question8 = Question("What is the sum of the silver medals won by Germany in both graphs?",
                    "assets/area-max-trial-3.png",
                    "assets/area-max-trial-4.png", "30", ["10", "15", "20", "25", "30"], "line")

question_list = []
question_list.append(question)
question_list.append(question2)
question_list.append(question3)
question_list.append(question4)
question_list.append(question5)
question_list.append(question6)
question_list.append(question7)
question_list.append(question8)

controller = QuizController(question_list)

QuizUI(controller)
