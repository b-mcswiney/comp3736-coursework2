from quiz.question import Question
from quiz.controller import QuizController
from quiz.ui import QuizUI

# Line max trial 1 and 2
question = Question("Which Graph shows more gold medals for GB?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "A", ["A", "", "", "","B"], "line")
question2 = Question("Which Graph shows more total medals for the USA?",
                    "assets/line-max-trial-1.png",
                    "assets/line-max-trial-2.png", "B", ["A", "", "", "", "B"], "line")

# Area max trial 1 and 2
question3 = Question("Which Graph shows more gold medals for GB?",
                    "assets/area-max-trial-1.png",
                    "assets/area-max-trial-2.png", "B", ["A", "", "", "", "B"], "area")
question4 = Question("Which Graph shows more total medals for the USA?",
                    "assets/area-max-trial-1.png",
                    "assets/area-max-trial-2.png", "B", ["A", "", "", "", "B"], "area")

# Line max trial 3 and 4
question5 = Question("In which Graph did GB win less bronze medals?",
                    "assets/line-max-trial-3.png", 
                    "assets/line-max-trial-4.png", "B", ["A", "", "", "", "B"], "line")
question6 = Question("What is the sum of the silver medals won by Germany in both graphs?",
                    "assets/line-max-trial-3.png",
                    "assets/line-max-trial-4.png", "44", ["38", "40", "44", "46", "48"], "line")

# Area max trial 3 and 4
question7 = Question("In which Graph did GB win less bronze medals?",
                    "assets/area-max-trial-3.png",
                    "assets/area-max-trial-4.png", "A", ["A", "", "", "", "B"], "area")
question8 = Question("What is the sum of the silver medals won by Germany in both graphs?",
                    "assets/area-max-trial-3.png",
                    "assets/area-max-trial-4.png", "37", ["33", "35", "37", "39", "41"], "area")

# line years trial 1 and 2
question9 = Question("In Graph A, which year shows the least amount of total medals gained?",
                    "assets/line-years-trial-1.png", # 109, 111, 112, 
                    "assets/line-years-trial-2.png", "Year 1", ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"], "line")
question10 = Question("In Graph B, which year shows the least amount of total medals gained??",
                    "assets/line-years-trial-1.png",
                    "assets/line-years-trial-2.png", "Year 2", ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"], "line")

# area years trial 1 and 2
question11 = Question("In Graph A, which year shows the least amount of total medals gained?",
                    "assets/area-years-trial-1.png",
                    "assets/area-years-trial-2.png", "Year 3", ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"], "area")
question12 = Question("In Graph B, which year shows the least amount of total medals gained?",
                    "assets/area-years-trial-1.png",
                    "assets/area-years-trial-2.png", "Year 4", ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"], "area")

# line years trial 3 and 4
question13 = Question("In Graph A, which country got the most medals?",
                    "assets/line-years-trial-3.png",
                    "assets/line-years-trial-4.png", "GB", ["GB", "AUS", "JP", "GER", ""], "line")
# area years trial 3 and 4
question14 = Question("In Graph A, which country got the 2nd highest amount of medals?",
                    "assets/area-years-trial-3.png",
                    "assets/area-years-trial-4.png", "GER", ["GB", "AUS", "JP", "GER", ""], "line")

# line country trial 1 and 2
question15 = Question("In Graph B, which country got the most medals?",
                    "assets/line-country-trial-1.png",
                    "assets/line-country-trial-2.png", "GB", ["GB", "AUS", "JP", "GER", ""], "line")
question16 = Question("In Graph B, which country got the 2nd highest amount of medals?",
                    "assets/line-max-trial-5.png",
                    "assets/line-max-trial-6.png", "AUS", ["GB", "AUS", "JP", "GER", ""], "line")

# area country trial 1 and 2
question17 = Question("In Graph A, which country got the most medals?",
                    "assets/area-max-trial-5.png",
                    "assets/area-max-trial-6.png", "GER", ["GB", "AUS", "JP", "GER", ""], "area")
question18 = Question("In Graph A, which country got the 2nd highest amount of medals?",
                    "assets/area-max-trial-5.png",
                    "assets/area-max-trial-6.png", "AUS", ["GB", "AUS", "JP", "GER", ""], "area")

# Comparison trials
question19 = Question("In Graph B, which country got the most medals?",
                    "assets/area-max-trial-5.png",
                    "assets/area-max-trial-6.png", "GER", ["GB", "AUS", "JP", "GER", ""], "area")
question20 = Question("In Graph B, which country got the 2nd highest amount of medals?",
                    "assets/area-max-trial-5.png",
                    "assets/area-max-trial-6.png", "GB", ["GB", "AUS", "JP", "GER", ""], "area")

question21 = Question("Which graphtype do you find easier to read??",
                    "assets/line-max-trial-1.png",
                    "assets/area-max-trial-1.png", "line", ["line", "", "", "", "area"], "")


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
