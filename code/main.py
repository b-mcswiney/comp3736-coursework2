from quiz.question import Question
from quiz.controller import QuizController
from quiz.ui import QuizUI


# Just deine 1 question for testing purposes
question = Question("Which Graph shows more gold medals for the UK?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "A", "line")
question2 = Question("Which Graph shows more total medals for the USA?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "B", "line")
question3 = Question("Which Graph shows more gold medals for the UK?",
                    "assets/area-max-trial-1.png",
                    "assets/area-max-trial-2.png", "A", "line")
question4 = Question("Which Graph shows more total medals for the USA?",
                    "assets/area-max-trial-1.png",
                    "assets/area-max-trial-2.png", "B", "line")
question_list = []
question_list.append(question)
question_list.append(question2)

question_list.append(question3)
question_list.append(question4)

controller = QuizController(question_list)

QuizUI(controller)
