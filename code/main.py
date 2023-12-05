from quiz.question import Question
from quiz.controller import QuizController
from quiz.ui import QuizUI


# Just deine 1 question for testing purposes
question = Question("Which Graph shows more wins for the UK?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "B", "line")
question2 = Question("Great googily moogily", "test", "test", "A", "area")
question_list = []
question_list.append(question)
question_list.append(question2)

controller = QuizController(question_list)

QuizUI(controller)
